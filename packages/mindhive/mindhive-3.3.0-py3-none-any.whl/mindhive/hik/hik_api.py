import logging
from ctypes import (
    byref,
    c_bool,
    c_char_p,
    c_float,
    c_int,
    c_int64,
    CDLL,
    create_string_buffer,
    sizeof,
    c_uint64,
    c_uint,
    c_size_t,
)
from pathlib import Path
from typing import Mapping, Sequence
import ipaddress
from time import sleep

import atexit

from ..gev.px_format import PxFormat
from .hik_c_data import CameraInfo, encode_str, decode_bytes, MatchInfoNetDetect
from .hik_error import (
    check_status,
    MV_E_PARAMETER,
    MV_E_HANDLE,
    MV_E_CALL_ORDER,
    format_hik_status,
    normalize_hik_status,
)
from .hik_frame import HikFrame

HIK_SO_PATH = "/opt/MVS/lib/hik.so"

HIK4K_PREAMP_GAINS = [
    1.0,
    1.4,
    1.6,
    2.4,
    3.2,
]

HIK4K_RGB_STANDARD_BALANCE_RATIOS = [1148, 1024, 1828]
HIK4K_WRGB_CALIBRATION_TARGETS_FOR_WHITE = [4095, 3674, 4106, 2301]

# Note: these do not match exactly tags in Datadog, there they are lowercase '_' instead of ' '
KNOWN_FIRMWARE_VERSIONS = {
    "V3.4.51 211101708339 21101401",
    "V3.4.61 220818871572 22081721",
    # Below is intentionally removed as we don't want to run this version of the FW
    # See https://mindhive.myjetbrains.com/youtrack/issue/TG-1764/HIK-firmware-issues
    "V3.4.62 2306191052294 23061702",
}

CAMERA_RESET_INTERVAL = 10  # sec


def calc_preamp_gain_and_exposure(log, exposure_micros, gain):
    try:
        preamp_gain = min(g for g in HIK4K_PREAMP_GAINS if g >= gain)
    except ValueError:
        raise RuntimeError(f"Gain: {gain:.2f} exceeds maximum preamp gain: {max(HIK4K_PREAMP_GAINS):.1f}")
    gain_exposure_factor = gain / preamp_gain
    adjusted_exposure_micros = exposure_micros * gain_exposure_factor
    if gain != 1:
        log.info(
            f"Splitting gain: {gain:.2f} into preamp: x{preamp_gain:.1f} and exposure factor: {gain_exposure_factor:.2f}"
        )
    return adjusted_exposure_micros, preamp_gain


class HikCamera:
    def __init__(
        self,
        driver,
        cam: CameraInfo,
        px_format: PxFormat,
        log_suffix: str,
        calibrated_exposure: float,
        calibrated_gain: float,
    ) -> None:
        self.log = logging.getLogger(f"{self.__class__.__name__}.{log_suffix}")
        self.driver = driver
        self.cam = cam
        self.px_format = px_format
        self.index = cam.index
        self.serial = cam.serial
        self.calibrated_exposure = calibrated_exposure
        self.calibrated_gain = calibrated_gain
        self.gain_proportion = 1.0
        firmware_version = self.feature_string(b"DeviceFirmwareVersion")
        if firmware_version not in KNOWN_FIRMWARE_VERSIONS:
            raise ValueError(f"Camera {cam.serial} has un-tested firmware version: '{firmware_version}'")
        self.metadata = {
            "serial": self.serial,
            "model": self.feature_string(b"DeviceModelName"),
            "device_version": self.feature_string(b"DeviceVersion"),
            "firmware_version": firmware_version,
        }
        self.frame_buffer = HikFrame(px_format)

    def _check(self, status: int):
        check_status(self.driver, status, self.cam)

    def feature_float(self, feature: bytes) -> float:
        result = c_float()
        self._check(self.driver.get_float_feature(self.index, feature, byref(result)))
        return result.value

    def feature_int(self, feature: bytes) -> int:
        result = c_int64()
        self._check(self.driver.get_int_feature(self.index, feature, byref(result)))
        return result.value

    def feature_string(self, feature: bytes) -> str:
        result = create_string_buffer(256)
        self._check(self.driver.get_string_feature(self.index, feature, result, c_size_t(sizeof(result))))
        return decode_bytes(result.value)

    def feature_download_all(self, filename: str):
        self._check(self.driver.download_all_features(self.index, encode_str(filename)))

    def start_acquisition(self, start_time: float):
        self.log.debug("Starting")
        epoch_micros = int(start_time * (10**6))
        self._check(self.driver.start_acquisition(self.index, c_uint64(epoch_micros)))
        self.log.debug("Started")

    def wait_for_image(self, timeout: float) -> tuple[HikFrame, int]:
        wait_error = self.driver.wait_for_image(self.index, byref(self.frame_buffer.frame), c_uint(int(timeout * 1000)))
        return self.frame_buffer, normalize_hik_status(wait_error)

    def image_done(self):
        status = self.driver.release_image(self.index, byref(self.frame_buffer.frame))
        if normalize_hik_status(status) in {MV_E_PARAMETER, MV_E_HANDLE, MV_E_CALL_ORDER}:
            self.log.warning(f"Ignore error in image_done: {format_hik_status(MV_E_CALL_ORDER)}")
            return
        self._check(status)

    def get_net_metrics(self) -> MatchInfoNetDetect:
        result = MatchInfoNetDetect()
        self._check(self.driver.get_net_metrics(self.index, byref(result)))
        return result

    def config_dual_line_trigger(self, input_line: int):
        self._check(self.driver.config_dual_line_trigger(self.index, input_line))

    def calibrate(self, wrgb_targets: Sequence[float]):
        rgb_int_targets = [
            round(factor * white_target)
            for factor, white_target in zip(wrgb_targets, HIK4K_WRGB_CALIBRATION_TARGETS_FOR_WHITE)
        ]
        self._check(self.driver.calibrate(self.index, *rgb_int_targets))

    def set_calibration_enable(self, enable: bool):
        self._check(self.driver.set_calibration_enable(self.index, enable))

    def stop_acquisition(self):
        self.driver.stop_acquisition(self.index)

    def download_file_to_disk(self, dev_filename: str, local_filename: str | Path) -> None:
        self._check(self.driver.download_file(self.index, encode_str(dev_filename), encode_str(str(local_filename))))

    def upload_file_from_disk(self, dev_filename: str, local_filename: str | Path) -> None:
        self._check(self.driver.upload_file(self.index, encode_str(dev_filename), encode_str(str(local_filename))))

    def close(self):
        self.driver.close_camera(self.index)

    def reset(self):
        self._check(self.driver.reset_camera(self.index))

    def get_encoder_value(self):
        return self.feature_int(b"ResultingTriggerLineRate")

    def encoder_setup(self, encoder_line: int, multiplier: int):
        self._check(self.driver.config_encoder(c_int(self.index), int(encoder_line), c_int(multiplier)))

    def update_exposure(self, gain_proportion: float = 1.0):
        if gain_proportion == self.gain_proportion:
            self.log.info(f"Gain alter unchanged: {self.gain_proportion}")
            return
        self.log.info(f"Gain alter: {self.gain_proportion}")
        adjusted_exposure_micros, preamp_gain = calc_preamp_gain_and_exposure(
            self.log, self.calibrated_exposure, self.calibrated_gain * gain_proportion
        )
        self.gain_proportion = gain_proportion
        self._check(
            self.driver.config_exposure(
                c_int(self.index),
                c_float(adjusted_exposure_micros),
                c_int(round(preamp_gain * 1000)),
            )
        )

    def get_exposure_value(self):
        return self.feature_float(b"ExposureTime")


class _HikApi:
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
        self.driver = CDLL(HIK_SO_PATH)
        self.driver.get_last_failed_func.restype = c_char_p
        self.shutting_down = False
        atexit.register(self._teardown)
        self.load_cameras()

    def load_cameras(self):
        max_cams = self.driver.get_max_cameras()
        c_cameras = (CameraInfo * max_cams)()
        c_cam_count = c_uint()
        self.log.debug(f"Polling cameras with max count: {max_cams}")
        self._check(self.driver.get_cameras(c_cameras, c_uint(max_cams), byref(c_cam_count)), None)
        self.log.debug(f"Found camera count: {c_cam_count.value}")
        self.serial_map_cam_info: Mapping[str, CameraInfo] = {cam.serial: cam for cam in c_cameras[: c_cam_count.value]}
        self.serials = set(self.serial_map_cam_info.keys())

    def reset_camera(self, cam: CameraInfo):
        self._check(self.driver.reset_camera(cam.index), cam)
        sleep(CAMERA_RESET_INTERVAL)
        self._check(self.driver.close_camera(cam.index), cam)

    def set_dhcp_addr(self, cam: CameraInfo):
        self._check(self.driver.set_dhcp_mode(c_int(cam.index)), cam)
        self.reset_camera(cam)

    def set_linklocal_addr(self, cam: CameraInfo):
        self._check(self.driver.set_linklocal_addr(c_int(cam.index)), cam)
        self.reset_camera(cam)

    def set_static_ip_addr(self, cam: CameraInfo, ip: str, netmask: str, gateway: str):
        nIP = int(ipaddress.ip_address(ip))
        nNetMask = int(ipaddress.ip_address(netmask))
        nGateway = int(ipaddress.ip_address(gateway))
        self._check(self.driver.set_static_ip_addr(c_int(cam.index), c_int(nIP), c_int(nNetMask), c_int(nGateway)), cam)

    def open_camera_basic(self, cam: CameraInfo):
        self._check(self.driver.open_camera(cam.index), cam)

    def open_camera_color(
        self,
        cam: CameraInfo,
        log_suffix: str,
        frame_height: int,
        line_rate: float,
        exposure_micros: float,
        gain: float,
        reverse_x: bool,
        reverse_scan_direction: bool,
        px_format: PxFormat,
        calibration_set: int | None,
        white_balance_rgb_factors: tuple[float, float, float],
        packet_size: int,
    ) -> HikCamera:
        self.log.debug(f"Opening {cam.serial}")
        adjusted_exposure_micros, preamp_gain = calc_preamp_gain_and_exposure(self.log, exposure_micros, gain)
        int_rgb_balance_ratios = [
            round(factor * ratio) for factor, ratio in zip(white_balance_rgb_factors, HIK4K_RGB_STANDARD_BALANCE_RATIOS)
        ]
        self._check(self.driver.open_camera(cam.index), cam)
        self._check(
            self.driver.config_color_camera(
                c_int(cam.index),
                c_int(frame_height),
                c_float(line_rate),
                c_float(adjusted_exposure_micros),
                c_int(round(preamp_gain * 1000)),
                c_bool(reverse_x),
                c_bool(reverse_scan_direction),
                c_int(px_format.code),
                c_bool(px_format.binning),
                encode_str(None if calibration_set is None else f"UserPRNUC{calibration_set}"),
                *(c_int(int_ratio) for int_ratio in int_rgb_balance_ratios),
                c_int(packet_size),
            ),
            cam,
        )
        self.log.debug(f"Opened {cam.serial}")
        return HikCamera(self.driver, cam, px_format, log_suffix, exposure_micros, gain)

    def open_camera_mono(
        self,
        cam: CameraInfo,
        log_suffix: str,
        frame_height: int,
        line_rate: float,
        exposure_micros: float,
        gain: float,
        reverse_x: bool,
        # reverse_scan_direction: bool,
        px_format: PxFormat,
        calibration_set: int | None,
        # white_balance_rgb_factors: tuple[float, float, float],
        packet_size: int,
    ) -> HikCamera:
        self.log.debug(f"Opening {cam.serial} a mono camera")
        adjusted_exposure_micros, preamp_gain = calc_preamp_gain_and_exposure(self.log, exposure_micros, gain)
        self._check(self.driver.open_camera(cam.index), cam)
        self._check(
            self.driver.config_mono_camera(
                c_int(cam.index),
                c_int(frame_height),
                c_float(line_rate),
                c_float(adjusted_exposure_micros),
                c_int(round(preamp_gain * 1000)),
                c_bool(reverse_x),
                # c_bool(reverse_scan_direction),
                c_int(px_format.code),
                c_bool(px_format.binning),
                encode_str(None if calibration_set is None else f"UserPRNUC{calibration_set}"),
                # *(c_int(int_ratio) for int_ratio in int_rgb_balance_ratios),
                c_int(packet_size),
            ),
            cam,
        )
        self.log.debug(f"Opened {cam.serial}")
        return HikCamera(self.driver, cam, px_format, log_suffix, exposure_micros, gain)

    def config_dual_line_trigger(self, cam: CameraInfo, input_line: int):
        self._check(self.driver.config_dual_line_trigger(c_int(cam.index), c_int(input_line)), cam)

    def _check(self, status: int, cam: CameraInfo | None):
        check_status(self.driver, status, cam)

    def _teardown(self):
        self.log.info(f"Teardown start")
        self.shutting_down = True
        self.driver.teardown()
        self.log.info("Teardown complete")


_api: _HikApi | None = None


def hik_api() -> _HikApi:
    global _api
    if _api is None:
        _api = _HikApi()
    return _api  # noqa
