from tempfile import NamedTemporaryFile
from threading import Event, RLock
from time import monotonic, time, sleep
from typing import Callable, Sequence

import numpy as np

from .hik_api import HikCamera, hik_api
from .hik_c_data import MatchInfoNetDetect
from .hik_calibration_image import (
    calibration_set_filename,
    decode_hik_calibration_data,
    hik_calibration_gain_rgb_views,
    CALIBRATION_GAIN_MULTIPLIER,
)
from .hik_error import format_hik_status, HikException, GEV_COMMS_ERRORS, MV_E_PARAMETER, MV_E_NO_DATA
from .hik_frame import HikFrame
from ..frame.frame import Frame
from ..gev.cam_error import CamError
from ..gev.camera_array_config import CameraArrayConfig
from ..gev.frame_id_tracking import FrameIdTracking
from ..gev.px_format import PxFormat
from ..log.metrics import metrics
from ..log.trace import tracer
from ..process.data_vehicle import DataVehicle
from ..process.producer import ProducerImpl
from ..process.thread import start_thread
from ..strip.rendering import Rendering

REPORT_METRICS_PERIOD = 9

ErrorListener = Callable[[str], None]
WorkerTask = Callable[[], None]
PersistentWorkerTask = Callable[[], bool]


class HikCameraProducer(ProducerImpl[Frame]):
    def __init__(
        self,
        cam_idx: int,
        cam: HikCamera,
        config: CameraArrayConfig,
        *,
        missing_frames_fatal=True,
        report_metrics=True,
        differentiator: str | None = None,
    ) -> None:
        self._differentiator = differentiator
        super().__init__()
        self.cam_idx = cam_idx
        self.cam = cam
        self.time_per_frame = config.time_per_frame
        self.missing_frames_fatal = missing_frames_fatal
        self.report_metrics = report_metrics
        self._stop_event = Event()
        self._started_event = Event()
        self.error_listeners: list[ErrorListener] = []
        self.start_ts: float | None = None
        self.last_frame_id: int | None = None
        self.last_metrics_ts: float | None = None
        self.worker_tasks: list[WorkerTask] = []
        self.worker_tasks_lock = RLock()
        self.persistent_worker_tasks: list[PersistentWorkerTask] = []
        self.persistent_worker_tasks_lock = RLock()
        self.metric_tags = [f"index:{cam_idx}"] + [f"{k}:{v}" for k, v in self.cam.metadata.items()]
        self.log.info(f"HIK metadata/tags: {self.metric_tags!r}")
        self.frame_id_tracking = FrameIdTracking(missing_frames_fatal, self.log, self.metric_tags)
        self.last_net_metrics: MatchInfoNetDetect = MatchInfoNetDetect()
        if report_metrics:
            metrics.gauge("camera.gain", config.gain[cam_idx], self.metric_tags)
            metrics.gauge("camera.gain_proportion", self.cam.gain_proportion, self.metric_tags)
            if config.calibration_set:
                self._calibration_metrics(config.calibration_set)
            self._maybe_report_metrics()

    @property
    def differentiator(self) -> str | None:
        return self._differentiator

    @property
    def serial(self) -> str:
        return self.cam.serial

    @property
    def px_format(self) -> PxFormat:
        return self.cam.px_format

    def on_error(self, listener: ErrorListener):
        self.error_listeners.append(listener)

    def config_dual_line_trigger(self, input_line: int):
        assert not self.started
        self.cam.config_dual_line_trigger(input_line)

    def start(self, coordination_time: float):
        self._stop_event.clear()
        self.last_net_metrics = MatchInfoNetDetect()
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

    def _worker(self):
        try:
            try:
                self._synchronize_start_camera()
                self.log.info("Started")
            finally:
                self._started_event.set()  # So no one is waiting for this and blocked forever
            while not self.stopping:
                with tracer.trace(f"{self.name}.frame"):
                    if self._process_worker_tasks():
                        if self.stopping:
                            break
                    elif self._process_persistent_worker_tasks():
                        if self.stopping:
                            break
                    else:
                        self._maybe_report_metrics()
                    raw_frame, wait_error = self._wait_for_image()
                    if hik_api().shutting_down:
                        self.log.info("shutting_down detected during _wait_for_image(), so stopping")
                        self._stop()
                        break
                    if self.stopping:
                        break
                    try:
                        if raw_frame.lost_packet_count:
                            self.log.warning(f"Lost packet count: {raw_frame.lost_packet_count}")
                        metrics.increment("camera.lost_packet_count", raw_frame.lost_packet_count, self.metric_tags)
                        if wait_error:
                            if wait_error in GEV_COMMS_ERRORS:
                                metrics.increment("camera.comms_error_count", tags=self.metric_tags)
                            elif wait_error != MV_E_NO_DATA:
                                raise HikException(wait_error, "_wait_for_image()", self.serial)
                            self._record_recoverable_error(
                                f"Wait error: {format_hik_status(wait_error)}, last frame: {self.last_frame_id}"
                            )
                            continue
                        self._push(DataVehicle(self._process_image(raw_frame)))
                    finally:
                        if wait_error != MV_E_NO_DATA:
                            self.cam.image_done()
        except HikException as err:
            if self.stopping:
                self.log.info(f"Ignoring error while stopping: {err}", exc_info=True)
                return
            if err.status in GEV_COMMS_ERRORS:
                metrics.increment("camera.comms_error_count", tags=self.metric_tags)
            raise
        finally:
            self._started_event.clear()

    def set_calibration_enable(self, enable: bool):
        def execute():
            self.cam.set_calibration_enable(enable)

        self._add_worker_task(execute)

    def calibrate(self, wrgb_targets: Sequence[float], complete_callback: Callable[[], None] | None = None):
        def execute():
            self.cam.calibrate(wrgb_targets)
            sleep(4)
            self.cam.set_calibration_enable(True)
            if complete_callback:
                complete_callback()

        self._add_worker_task(execute)

    def copy_calibration_set(self, src_set: int, dest_set: int, complete_callback: Callable[[], None] | None = None):
        def execute():
            self.cam.stop_acquisition()
            with NamedTemporaryFile("wb") as f:
                self.log.info(f"Downloading calibration set {src_set} to: {f.name}")
                self.cam.download_file_to_disk(calibration_set_filename(src_set), f.name)
                self.log.info(f"Upload calibration set {dest_set} from: {f.name}")
                self.cam.upload_file_from_disk(calibration_set_filename(dest_set), f.name)
            self.stop()
            self.log.info("Copy complete")
            if complete_callback:
                complete_callback()

        self._add_worker_task(execute)

    def _add_worker_task(self, execute: WorkerTask):
        with self.worker_tasks_lock:
            self.worker_tasks.append(execute)

    def _add_persistent_worker_task(self, execute: PersistentWorkerTask):
        with self.persistent_worker_tasks_lock:
            self.persistent_worker_tasks.append(execute)

    def stop(self):
        self._stop()
        self.cam.stop_acquisition()

    def reboot(self):
        def execute():
            self.log.info("Rebooting")
            self.cam.reset()
            self._stop()

        self._add_worker_task(execute)

    def _close(self):
        self._stop()
        self.cam.close()

    def _stop(self):
        self._stop_event.set()

    def _wait_for_image(self) -> tuple[HikFrame, int]:
        return self.cam.wait_for_image(timeout=4 * self.time_per_frame)

    def _process_image(self, frame: HikFrame) -> Frame:
        metrics.increment("camera.frame.count", 1, self.metric_tags)
        if not frame.has_contents:
            raise CamError(f"Buffer is empty, last frame: {self.last_frame_id}")
        snapshot = frame.snapshot()
        frame_id = self.frame_id_tracking.calc_frame_id(snapshot.id)
        metrics.gauge("camera.frame.id", frame_id, self.metric_tags)
        self.last_frame_id = frame_id
        return Frame(
            self.cam_idx,
            frame_id,
            snapshot.frame_time - self.time_per_frame,
            snapshot.image,
            Rendering.mono if frame.px_format.mono else Rendering.color,
        )

    def _synchronize_start_camera(self):
        assert self.start_ts
        remaining_seconds = self.start_ts - time()
        self.log.debug(f"Waiting for start, remaining: {remaining_seconds:.3f}s")
        if remaining_seconds < 0:
            raise CamError(f"start_time already passed by {-remaining_seconds}s")
        self.cam.start_acquisition(self.start_ts)

    def _calibration_metrics(self, calibration_set: int):
        try:
            with NamedTemporaryFile("rb") as f:
                self.cam.download_file_to_disk(calibration_set_filename(calibration_set), f.name)
                calibration_bytes = f.read()
            try:
                calibration_img = decode_hik_calibration_data(calibration_bytes)
            except ValueError:
                self.log.info(f"Ignoring error in decoding HIK calibration", exc_info=True)
                return
            for label, gain in zip(
                ["red", "green", "blue"],
                hik_calibration_gain_rgb_views(calibration_img),
            ):
                tags = self.metric_tags + [f"channel:{label}"]
                scaled_median = np.median(gain) / CALIBRATION_GAIN_MULTIPLIER
                scaled_max = np.max(gain) / CALIBRATION_GAIN_MULTIPLIER
                metrics.gauge("camera.calibration.gain.median", float(scaled_median), tags)
                metrics.gauge("camera.calibration.gain.max", float(scaled_max), tags)
        except HikException as err:
            if err.status == MV_E_PARAMETER:
                self.log.debug(f"Calibration set: {calibration_set} does not exist")

    def _maybe_report_metrics(self) -> bool:
        if not self.report_metrics:
            return False
        if self.last_metrics_ts and monotonic() < (self.last_metrics_ts + REPORT_METRICS_PERIOD):
            return False
        self.log.debug("Reporting metrics")
        metrics.gauge("camera.online", 1, self.metric_tags)
        metrics.gauge("camera.uptime", self.cam.feature_int(b"DeviceUptime"), self.metric_tags)
        if self.started:
            net_metrics = self.cam.get_net_metrics()
            for field_name, metric_name in {
                "nReceivedDataSize": "received_data",
                "nLostPacketCount": "lost_packet_count",  # Also received in frame data
                "nLostFrameCount": "lost_frame_count",
                "nNetRecvFrameCount": "received_frame_count",
                "nRequestResendPacketCount": "request_resend_packet_count",
                "nResendPacketCount": "resend_packet_count",
            }.items():
                metrics.increment(
                    f"camera.net.{metric_name}",
                    getattr(net_metrics, field_name) - getattr(self.last_net_metrics, field_name),
                    self.metric_tags,
                )
            self.last_net_metrics = net_metrics

        self.last_metrics_ts = monotonic()
        return True

    def _process_worker_tasks(self) -> bool:
        with self.worker_tasks_lock:
            tasks = list(self.worker_tasks)
            self.worker_tasks.clear()
        if not tasks:
            return False
        for task in tasks:
            if self.stopping:
                break
            task()
        return True

    @tracer.wrap()
    def _process_persistent_worker_tasks(self) -> bool:
        with self.persistent_worker_tasks_lock:
            tasks = list(self.persistent_worker_tasks)
        if not tasks:
            return False
        for task in tasks:
            if self.stopping:
                break
            task()
        return True

    def _record_recoverable_error(self, message: str):
        self.log.warning(message)
        for listener in self.error_listeners:
            listener(message)

    def update_exposure(self, gain_proportion: float):
        metrics.gauge("camera.gain_proportion", gain_proportion, self.metric_tags)
        self.cam.update_exposure(gain_proportion)
