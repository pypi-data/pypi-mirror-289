import logging
from enum import Enum
from threading import Event, RLock
from typing import Callable

import atexit
import numpy as np
from time import monotonic, time

from .dalsa_api import DalsaCamera, TimerState
from .dalsa_c_data import decode_bytes
from .dalsa_calibration_image import (
    CALIBRATION_GAIN_MULTIPLIER,
    dalsa_calibration_gain_rgb_views,
    dalsa_calibration_offset_rgb_views,
    decode_dalsa_calibration_image,
    calibration_set_filename,
)
from .dalsa_error import format_dalsa_status, DalsaException, GEV_COMMS_ERRORS
from .dalsa_frame_buffer import DalsaFrameBuffer
from ..frame.frame import Frame
from ..gev.cam_error import CamError
from ..gev.camera_array_config import CameraArrayConfig
from ..gev.frame_id_tracking import FrameIdTracking
from ..log.metrics import metrics
from ..log.trace import tracer
from ..process.data_vehicle import DataVehicle
from ..process.producer import ProducerImpl
from ..process.thread import start_thread
from ..strip.rendering import Rendering

REPORT_METRICS_PERIOD = 60
TIMER_MAX_TIME = 16.777215

DONT_REPORT_ABOVE_TEMP = 2**24
DONT_REPORT_BELOW_TEMP = -100

ErrorListener = Callable[[str], None]
CounterListener = Callable[[int], None]
FrequencyListener = Callable[[float], None]
WorkerTask = Callable[[], None]


class InputVoltage(Enum):
    V3_3 = "Threshold_for_3V3"
    V5 = "Threshold_for_5V"
    V12 = "Threshold_for_12V"
    V24 = "Threshold_for_24V"


class DalsaCameraProducer(ProducerImpl[Frame]):
    def __init__(
        self,
        cam_idx: int,
        cam: DalsaCamera,
        config: CameraArrayConfig,
        missing_frames_fatal=True,
    ) -> None:
        super().__init__()
        self.cam_idx = cam_idx
        self.cam = cam
        self.px_format = cam.px_format
        self.time_per_frame = config.time_per_frame
        self.calibration_set = config.calibration_set
        self.missing_frames_fatal = missing_frames_fatal
        self._stop_event = Event()
        self._started_event = Event()
        self.error_listeners: list[ErrorListener] = []
        self.start_ts: float | None = None
        self.start_monotonic: float | None = None
        self.start_device_ts: float | None = None
        self.last_frame_id: int | None = None
        self.last_metrics_ts: float | None = None
        self.counter_listener: CounterListener | None = None
        self.counter_poll_time: float | None = None
        self.counter_start_ts: float | None = None
        self.freq_listener: FrequencyListener | None = None
        self.freq_poll_time: float | None = None
        self.freq_next_poll_ts: float | None = None
        self.worker_tasks: list[WorkerTask] = []
        self.worker_tasks_lock = RLock()
        atexit.register(self._stop)
        self.metric_tags = [f"index:{cam_idx}", *(f"{k}:{v}" for k, v in self.cam.metadata.items())]
        self.frame_id_tracking = FrameIdTracking(missing_frames_fatal, self.log, self.metric_tags)
        self.log.info(repr(self.metric_tags))
        metrics.gauge("camera.gain", config.gain[cam_idx], self.metric_tags)
        self._maybe_report_metrics()

    @property
    def differentiator(self) -> str | None:
        return str(self.cam_idx)

    @property
    def serial(self):
        return self.cam.serial

    def on_error(self, listener: ErrorListener):
        self.error_listeners.append(listener)

    def start(self, coordination_time: float):
        self.start_ts = coordination_time
        start_thread(self.log, self._worker, self._close)

    def wait_for_started(self):
        self._started_event.wait()

    @property
    def started(self):
        return self._started_event.is_set()

    @property
    def stopping(self):
        return self._stop_event.is_set()

    def set_exposure(self, exposure_micros: float):
        def execute():
            self.cam.set_exposure(exposure_micros)

        with self.worker_tasks_lock:
            self.worker_tasks.append(execute)

    def on_poll_pulse_counter(
        self,
        listener: CounterListener,
        voltage: InputVoltage,
        poll_time: float,
        line_num=1,
    ):
        if self.counter_listener is not None or self.freq_listener is not None:
            raise NotImplementedError("Can only have one counter/timer listener")
        self.counter_listener = listener
        self.counter_poll_time = poll_time
        self.cam.start_timed_line_counter(f"Line{line_num}".encode(), voltage.value.encode("ascii"), poll_time)
        self.counter_start_ts = monotonic()
        self.log.info("Setup counter")

    def on_pulse_frequency(
        self,
        listener: FrequencyListener,
        voltage: InputVoltage,
        poll_time: float,
        max_time_between_pulses=TIMER_MAX_TIME,
        line_num=1,
    ):
        if self.counter_listener is not None or self.freq_listener is not None:
            raise NotImplementedError("Can only have one counter/timer listener")
        self.freq_listener = listener
        self.freq_poll_time = poll_time
        self.cam.start_line_timer(f"Line{line_num}".encode(), voltage.value.encode("ascii"), max_time_between_pulses)
        self.freq_next_poll_ts = monotonic() + poll_time
        self.log.info("Setup frequency")

    def _worker(self):
        try:
            try:
                self._synchronize_start_camera()
                self.log.info("Started")
            finally:
                self._started_event.set()  # So no one is waiting for this and blocked forever
            self.start_monotonic = monotonic()
            while not self.stopping:
                with tracer.trace(f"{self.name}.frame"):
                    done_extra_processing = (  # noqa
                        self._process_worker_tasks()
                        or self._maybe_read_counter()
                        or self._maybe_read_freq()
                        or self._maybe_report_metrics()
                    )
                    frame_buffer, wait_error = self._wait_for_image()
                    try:
                        if self.stopping:
                            break
                        frame = self._process_image(frame_buffer, wait_error)
                        if frame:
                            self._push(DataVehicle(frame))
                    finally:
                        self.cam.image_done()
        except DalsaException as err:
            if err.status in GEV_COMMS_ERRORS:
                metrics.increment("camera.comms_error_count", tags=self.metric_tags)
            raise

    def stop(self):
        self._stop()
        self.cam.stop_acquisition()

    def reboot(self):
        self._stop()
        self.cam.reset()

    def _close(self):
        self._stop()
        self.cam.close()

    def _stop(self):
        if self._stop_event.is_set():
            return
        atexit.unregister(self._stop)
        self._stop_event.set()

    @tracer.wrap()
    def _wait_for_image(self) -> tuple[DalsaFrameBuffer, int]:
        return self.cam.wait_for_image(timeout=4 * self.time_per_frame)

    @tracer.wrap()
    def _process_image(self, frame_buffer: DalsaFrameBuffer, wait_error: int) -> Frame | None:
        now = time()
        metrics.gauge("camera.frame.buffers.used", frame_buffer.used_count, self.metric_tags)
        if wait_error:
            if wait_error in GEV_COMMS_ERRORS:
                metrics.increment("camera.comms_error_count", tags=self.metric_tags)
            error_src = "GEVLIB_ERROR" if wait_error < 0 else "GEV_FRAME_STATUS"
            self._record_recoverable_error(
                f"{error_src}: {format_dalsa_status(wait_error)}, last frame: {self.last_frame_id}"
            )
            return None
        metrics.increment("camera.frame.count", 1, self.metric_tags)
        if frame_buffer.trashed_count:
            raise CamError(f"Running too slow, {frame_buffer.trashed_count} buffers have been trashed")
        if frame_buffer.used_count > 2 and self.start_ts:
            lifetime_seconds = now - self.start_ts
            # We expect used buffers when first starting
            level = logging.DEBUG if lifetime_seconds < 10 else logging.WARNING
            self.log.log(level, f"Buffers used: {frame_buffer.used_count}")
        if not frame_buffer.has_contents:
            raise CamError(f"Buffer is empty, last frame: {self.last_frame_id}")
        snapshot = frame_buffer.snapshot()
        device_ts = snapshot.device_micros / 1_000_000
        frame_id = self.frame_id_tracking.calc_frame_id(snapshot.id)
        self._device_clock_metrics(device_ts)
        metrics.gauge("camera.frame.device_id", snapshot.id, self.metric_tags)
        metrics.gauge("camera.frame.id", frame_id, self.metric_tags)
        metrics.gauge("camera.uptime", device_ts, self.metric_tags)
        frame = Frame(self.cam_idx, frame_id, now - self.time_per_frame, snapshot.image, Rendering.color)
        self.last_frame_id = frame_id
        return frame

    @tracer.wrap()
    def _synchronize_start_camera(self):
        assert self.start_ts
        remaining_seconds = self.start_ts - time()
        self.log.debug(f"Waiting for start, remaining: {remaining_seconds:.3f}s")
        if remaining_seconds < 0:
            raise CamError(f"start_time already passed by {-remaining_seconds}s")
        self.cam.start_acquisition(self.start_ts)

    @tracer.wrap()
    def _maybe_read_counter(self) -> bool:
        if self.counter_listener is None:
            return False
        assert self.counter_start_ts
        assert self.counter_poll_time
        if monotonic() < (self.counter_start_ts + self.counter_poll_time + 0.01):
            return False
        self.log.debug("Reading counter")
        count, ahead_time = self.cam.get_counter_state()
        self.counter_start_ts = monotonic() - ahead_time
        self.log.debug(f"Read counter: {count}")
        metrics.increment("camera.counter.update_count", 1, self.metric_tags)
        metrics.gauge("camera.counter.count", count, self.metric_tags)
        metrics.gauge("camera.counter.ahead_time", ahead_time, self.metric_tags)
        self.counter_listener(count)
        return True

    @tracer.wrap()
    def _maybe_read_freq(self) -> bool:
        if self.freq_listener is None:
            return False
        assert self.freq_next_poll_ts
        assert self.freq_poll_time
        now = monotonic()
        if now < self.freq_next_poll_ts:
            return False
        self.log.debug("Reading timer")
        state, timer_time = self.cam.get_timer_state_time()
        self.freq_next_poll_ts = now + self.freq_poll_time
        metrics.gauge("camera.timer.state", state.value, self.metric_tags)
        metrics.increment("camera.timer.update_count", 1, self.metric_tags)
        self.log.debug(f"Timer state: {state.name}")
        if timer_time is not None:
            metrics.gauge("camera.timer.time", timer_time, self.metric_tags)
        if state in {TimerState.ACTIVE, TimerState.STOPPED}:
            freq = 1 / timer_time if timer_time else 0
            self.log.debug(f"Read frequency: {freq:.3f}Hz")
            metrics.gauge("camera.timer.frequency", freq, self.metric_tags)
            self.freq_listener(freq)
        return True

    @tracer.wrap()
    def _maybe_report_metrics(self) -> bool:
        if self.last_metrics_ts and monotonic() < (self.last_metrics_ts + REPORT_METRICS_PERIOD):
            return False
        self.log.debug("Reporting metrics")
        first_time = self.last_metrics_ts is None
        if first_time and self.calibration_set is not None:
            calibration_bytes = self.cam.download_file(calibration_set_filename(self.calibration_set))
            calibration_img = decode_dalsa_calibration_image(calibration_bytes)
            for label, gain, offset in zip(
                ["red", "green", "blue"],
                dalsa_calibration_gain_rgb_views(calibration_img),
                dalsa_calibration_offset_rgb_views(calibration_img),
            ):
                tags = self.metric_tags + [f"channel:{label}"]
                scaled_gain = float(np.median(gain) / CALIBRATION_GAIN_MULTIPLIER)
                metrics.gauge("camera.calibration.gain.median", scaled_gain, tags)
                metrics.gauge("camera.calibration.offset.abs_total", np.sum(np.abs(offset)), tags)
        temp = self.cam.feature_float(b"DeviceTemperature")
        if DONT_REPORT_BELOW_TEMP < temp < DONT_REPORT_ABOVE_TEMP:
            metrics.gauge("camera.temp", temp, self.metric_tags)
        else:
            self.log.debug(f"Ignoring stupid camera temp: {temp}")
        status_all = 0
        for feature in [b"deviceBISTStatus", b"sensorStatus", b"OverheatedStatus"]:
            status = self.cam.feature_int(feature)
            if status != 0:
                status_all = status
                self._record_recoverable_error(f"{decode_bytes(feature)}: {self.cam.feature_string(feature)}")
        metrics.gauge("camera.status", status_all, self.metric_tags)
        metrics.gauge("camera.online", 1, self.metric_tags)
        self.last_metrics_ts = monotonic()
        return True

    def _device_clock_metrics(self, device_ts: float):
        assert self.start_monotonic
        if self.start_device_ts is None:
            self.start_device_ts = device_ts - self.time_per_frame
        local_elapsed = monotonic() - self.start_monotonic
        device_elapsed = device_ts - self.start_device_ts
        device_clock_factor = device_elapsed / local_elapsed
        metrics.gauge("camera.device_clock.factor", device_clock_factor - 1, self.metric_tags)

    @tracer.wrap()
    def _process_worker_tasks(self) -> bool:
        with self.worker_tasks_lock:
            tasks = list(self.worker_tasks)
            self.worker_tasks.clear()
        if not tasks:
            return False
        for task in tasks:
            task()
        return True

    def _record_recoverable_error(self, message: str):
        self.log.error(message)
        for listener in self.error_listeners:
            listener(message)
