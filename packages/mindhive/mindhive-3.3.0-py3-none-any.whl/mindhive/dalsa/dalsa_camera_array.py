import logging
from typing import Sequence

from .dalsa_api import dalsa_api, DalsaCamera
from .dalsa_c_data import CameraInfo, decode_pchar
from .dalsa_camera_producer import DalsaCameraProducer
from .dalsa_error import DalsaException, GEVLIB_ERROR_DEVICE_NOT_FOUND
from .dalsa_px_format import DALSA_LAYOUT_MAP_FORMAT
from ..gev.cam_error import CamerasOffException, CamerasMissingException
from ..gev.camera_array_config import CameraArrayConfig
from ..gev.camera_network import check_network, get_packet_size
from ..log.metrics import metrics

log = logging.getLogger(__name__)


def open_dalsa_camera_array(config: CameraArrayConfig) -> Sequence[DalsaCamera]:
    def get_camera_infos() -> Sequence[CameraInfo]:
        try:
            found_serials = set(dalsa_api().serial_map_cam_info.keys())
        except DalsaException as err:
            if err.status == GEVLIB_ERROR_DEVICE_NOT_FOUND:
                raise CamerasOffException()
            raise
        wanted_serials = set(config.serials)
        missing_serials = wanted_serials - found_serials
        if missing_serials == wanted_serials:
            raise CamerasOffException()
        for i, serial in enumerate(config.serials):
            tags = [f"index:{i}", f"serial:{serial}"]
            cam_found = serial in found_serials
            if not cam_found:
                metrics.increment("camera.comms_error_count", tags=tags)
            metrics.gauge("camera.online", int(cam_found), tags=tags)
        if missing_serials:
            raise CamerasMissingException([config.serials.index(s) for s in missing_serials])
        result = [dalsa_api().serial_map_cam_info[serial] for serial in config.serials]
        if log.isEnabledFor(logging.INFO):
            for cam in result:
                serial = decode_pchar(cam.serial)
                log.info(f"Found {serial}: {cam.address.compressed} on {cam.interface_name} idx: {cam.index}")
        return result

    def check_and_open(cam_idx: int, cam: CameraInfo) -> DalsaCamera:
        packet_size = get_packet_size(cam.interface_name)
        check_network(cam.address.compressed, packet_size, cam.interface_name)
        log.debug(f"Opening {cam_idx}")
        return dalsa_api().open_camera(
            cam,
            str(cam_idx),
            config.sync,
            config.frame_height,
            config.line_rate,
            config.exposure_micros,
            config.gain[cam_idx],
            config.reversed[cam_idx],
            DALSA_LAYOUT_MAP_FORMAT[config.px_layout],
            config.calibration_set,
            packet_size,
        )

    camera_infos = get_camera_infos()
    return [check_and_open(i, cam) for i, cam in enumerate(camera_infos)]


def open_dalsa_camera_producer_array(
    config: CameraArrayConfig,
    missing_frames_fatal=True,
) -> Sequence[DalsaCameraProducer]:
    return [
        DalsaCameraProducer(i, gev_cam, config, missing_frames_fatal)
        for i, gev_cam in enumerate(open_dalsa_camera_array(config))
    ]
