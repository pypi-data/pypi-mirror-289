import logging
from ctypes import (
    byref,
    c_bool,
    c_char_p,
    c_float,
    c_int,
    CDLL,
    create_string_buffer,
    sizeof,
    c_uint64,
)
from enum import IntEnum
from typing import Mapping

import atexit

from .dalsa_c_data import CameraInfo, decode_pchar, encode_str, decode_bytes
from .dalsa_error import check_status
from .dalsa_frame_buffer import DalsaFrameBuffer
from ..gev.camera_array_config import FACTORY_CALIBRATION_SET
from ..gev.px_format import PxFormat

DALSA_SO_PATH = "/opt/GigeV/dalsa.so"


class TimerState(IntEnum):
    WAITING_FOR_FIRST_SIGNAL = 1
    WAITING_FOR_SECOND_SIGNAL = 2
    ACTIVE = 3
    STOPPED = 4


class DalsaCamera:
    def __init__(self, driver, cam: CameraInfo, px_format: PxFormat, log_suffix: str) -> None:
        self.driver = driver
        self.px_format = px_format
        self.log = logging.getLogger(f"{self.__class__.__name__}.{log_suffix}")
        self.index = cam.index
        self.serial = decode_pchar(cam.serial)
        self.metadata = {
            "serial": self.serial,
            "model": self.feature_string(b"DeviceModelName"),
            "device_version": self.feature_string(b"DeviceVersion"),
            "firmware_version": self.feature_string(b"DeviceFirmwareVersion"),
        }
        self.frame_buffer = DalsaFrameBuffer(px_format)
        self.log.debug(repr(self.metadata))

    def _check(self, status: int):
        check_status(self.driver, status)

    def feature_float(self, feature: bytes) -> float:
        result = c_float()
        self._check(self.driver.get_float_feature(self.index, feature, byref(result)))
        return result.value

    def feature_int(self, feature: bytes) -> int:
        result = c_int()
        self._check(self.driver.get_int_feature(self.index, feature, byref(result)))
        return result.value

    def feature_string(self, feature: bytes) -> str:
        result = create_string_buffer(256)
        self._check(self.driver.get_string_feature(self.index, feature, result, sizeof(result)))
        return decode_bytes(result.value)

    def start_acquisition(self, start_time: float):
        self.log.debug("Starting")
        epoch_micros = int(start_time * (10**6))
        self._check(self.driver.start_acquisition(self.index, c_uint64(epoch_micros)))
        self.log.debug("Started")

    def wait_for_image(self, timeout: float) -> tuple[DalsaFrameBuffer, int]:
        wait_timeout_milliseconds = int(timeout * 1000)
        wait_error = self.driver.wait_for_image(
            self.index, byref(self.frame_buffer.buffer), byref(self.frame_buffer.stats), wait_timeout_milliseconds
        )
        return self.frame_buffer, wait_error

    def image_done(self):
        self._check(self.driver.release_image(self.index, self.frame_buffer.buffer))

    def set_exposure(self, exposure_micros: float):
        self._check(self.driver.set_exposure(self.index, c_float(exposure_micros)))

    def stop_acquisition(self):
        self.driver.stop_acquisition(self.index)

    def download_file(self, file_name: bytes) -> bytes:
        data_len = c_int()
        self._check(self.driver.get_file_size(self.index, file_name, byref(data_len)))
        data = create_string_buffer(data_len.value)
        self._check(self.driver.download_file(self.index, file_name, data, sizeof(data)))
        return data.raw

    def upload_file(self, file_name: bytes, data: bytes):
        self.log.info(f"Uploading file to {file_name} of size {len(data):,}b")
        self._check(self.driver.upload_file(self.index, file_name, data, len(data)))

    def close(self):
        self.driver.close_camera(self.index)

    def reset(self):
        self._check(self.driver.reset_camera(self.index))

    def start_timed_line_counter(self, line: bytes, input_voltage: bytes, update_time: float):
        update_micros = round(update_time * 1_000_000)
        self._check(self.driver.start_timed_line_counter(self.index, line, input_voltage, update_micros))

    def start_line_timer(self, line: bytes, input_voltage: bytes, max_time: float):
        max_micros = round(max_time * 1_000_000)
        self._check(self.driver.start_line_timer(self.index, line, input_voltage, max_micros))

    def get_counter_state(self) -> tuple[int, float]:
        count = c_int()
        timer_micros = c_int()
        self._check(self.driver.get_counter_state(self.index, byref(count), byref(timer_micros)))
        return count.value, timer_micros.value / 1_000_000

    def get_timer_state_time(self) -> tuple[TimerState, float | None]:
        timer_micros_or_state = c_int()
        self._check(self.driver.get_timer(self.index, byref(timer_micros_or_state)))
        if timer_micros_or_state.value >= 0:
            return TimerState.ACTIVE, timer_micros_or_state.value / 1_000_000
        state = timer_micros_or_state.value
        if state == -1:
            self.log.debug("Timer hasn't seen first signal")
            return TimerState.WAITING_FOR_FIRST_SIGNAL, None
        elif state == -2:
            self.log.debug("Timer hasn't seen second signal")
            return TimerState.WAITING_FOR_SECOND_SIGNAL, None
        return TimerState.STOPPED, None


class _DalsaApi:
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
        self.driver = CDLL(DALSA_SO_PATH)
        self.driver.get_last_failed_func.restype = c_char_p
        self._check(self.driver.initialize())
        atexit.register(self._teardown)
        max_cams = self.driver.get_max_cameras()
        cam_info_array_type = CameraInfo * max_cams
        c_cameras = cam_info_array_type()
        c_cam_count = c_int()
        self.log.debug("Polling cameras")
        self._check(self.driver.get_cameras(c_cameras, max_cams, byref(c_cam_count)))
        c_cameras = c_cameras[: c_cam_count.value]
        self.serial_map_cam_info: Mapping[str, CameraInfo] = {decode_pchar(cam.serial): cam for cam in c_cameras}
        self.serials = set(self.serial_map_cam_info.keys())

    def open_camera(
        self,
        cam: CameraInfo,
        log_suffix: str,
        sync: bool,
        frame_height: int,
        line_rate: float,
        exposure_micros: float,
        gain: float,
        reverse: bool,
        px_format: PxFormat,
        calibration_set: int | None,
        packet_size: int,
    ) -> DalsaCamera:
        self.log.debug(f"Opening {cam.serial}")
        if gain < 1:
            self.log.debug(f"Reducing exposure on {cam.serial} to implement gain < 1.0")
            exposure_micros = exposure_micros * gain
            gain = 1
        self._check(self.driver.open_camera(cam.index))
        if calibration_set is None:
            calibration_set_name = None
        elif calibration_set == FACTORY_CALIBRATION_SET:
            calibration_set_name = "FactoryFlatfield"
        else:
            calibration_set_name = f"UserFlatfield{calibration_set}"
        self._check(
            self.driver.config_camera(
                c_int(cam.index),
                c_bool(sync),
                c_int(frame_height),
                c_float(line_rate),
                c_float(exposure_micros),
                c_float(gain),
                c_bool(reverse),
                c_int(px_format.code),
                c_bool(px_format.binning),
                encode_str(calibration_set_name),
                c_int(packet_size),
            )
        )
        self.log.debug(f"Opened {cam.serial}")
        return DalsaCamera(self.driver, cam, px_format, log_suffix)

    def _check(self, status: int):
        check_status(self.driver, status)

    def _teardown(self):
        self.log.debug(f"Teardown start")
        self.driver.teardown()
        self.log.info("Teardown complete")


_api: _DalsaApi | None = None


def dalsa_api() -> _DalsaApi:
    global _api
    if _api is None:
        _api = _DalsaApi()
    return _api  # noqa
