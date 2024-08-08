import ipaddress
import logging
import os
from typing import Sequence

from .hik_api import hik_api, HikCamera
from .hik_c_data import CameraInfo
from .hik_camera_producer import HikCameraProducer
from .hik_px_format import HIK_LAYOUT_MAP_FORMAT
from ..gev.cam_error import CamerasOffException, CamerasMissingException
from ..gev.camera_array_config import CameraArrayConfig, CameraNetworkType
from ..gev.camera_network import get_packet_size, check_network
from ..log.metrics import metrics

log = logging.getLogger(__name__)

SWITCH_IP = os.getenv("CABINET_SWITCH_IP")


def open_hik_camera_array(config: CameraArrayConfig) -> Sequence[HikCamera]:
    # noinspection DuplicatedCode
    def get_camera_infos() -> Sequence[CameraInfo]:
        found_serials = set(hik_api().serials)
        if not found_serials:
            raise CamerasOffException()
        wanted_serials = set(config.serials)
        missing_serials = wanted_serials - found_serials
        if missing_serials:
            log.error(f"Wanted cameras: {wanted_serials}, found: {found_serials}, missing: {missing_serials}")
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
        result = [hik_api().serial_map_cam_info[serial] for serial in config.serials]
        if log.isEnabledFor(logging.INFO):
            for cam in result:
                log.info(f"Found {cam.serial}: {cam.address.compressed} on {cam.interface_name} idx: {cam.index}")
        return result

    def check_interface(interface_name: str):
        # HIK cameras don't respond to large pings, so ping switch instead
        if not SWITCH_IP:
            log.debug("Skipping mtu check as no switch ip")
            return
        packet_size = get_packet_size(interface_name)
        check_network(SWITCH_IP, packet_size, interface_name)

    def get_ip_gateway_netmask(addr):
        addr = ipaddress.ip_interface(addr)
        ipaddr = addr.ip.compressed
        netmask = addr.netmask.compressed
        gateway = ipaddr
        return ipaddr, netmask, gateway

    def check_cam_network(cam_idx: int, cam: CameraInfo):
        if config.network_type == CameraNetworkType.STATIC:
            if cam_idx > 0:
                raise RuntimeError("Only a single camera is currently supported by static network mode")

            cam_cidr = os.getenv("CAMERA_CIDR", None)
            if not cam_cidr:
                raise RuntimeError(f"CIDR address not provided for camera {cam_idx}")

            ipaddr, netmask, gateway = get_ip_gateway_netmask(cam_cidr)
            if not ipaddr == cam.address.compressed:
                log.debug(f"Changing camera ip address: {cam.address.compressed} => {ipaddr}")
                hik_api().set_static_ip_addr(cam, ipaddr, netmask, gateway)
                raise RuntimeError(f"Camera {cam_idx} static ip address changed to  {ipaddr}")

        else:
            temp_cidr = os.getenv("CAMERA_TEMP_CIDR", None)
            if cam.address.is_link_local or (temp_cidr and temp_cidr[0] == cam.address.compressed):
                if not temp_cidr:
                    raise RuntimeError("Link local address: Temporary CIDR address not provided")
                ipaddr, netmask, gateway = get_ip_gateway_netmask(temp_cidr)
                log.debug(f"Camera {cam_idx}: setting temp IP address {ipaddr} {netmask} {gateway}")
                hik_api().set_static_ip_addr(cam, ipaddr, netmask, gateway)
                hik_api().open_camera_basic(cam)
                hik_api().set_dhcp_addr(cam)
                raise RuntimeError(f"Camera {cam_idx} changed to DHCP mode")

    def open_cam(cam_idx: int, cam: CameraInfo) -> HikCamera:
        check_cam_network(cam_idx, cam)

        log.debug(f"Opening {cam_idx}")
        packet_size = get_packet_size(cam.interface_name)
        px_format = HIK_LAYOUT_MAP_FORMAT[config.px_layout]
        if px_format.mono:
            return hik_api().open_camera_mono(
                cam,
                str(cam_idx),
                config.frame_height,
                config.line_rate,
                config.exposure_micros,
                config.gain[cam_idx],
                config.reversed[cam_idx],
                px_format,
                config.calibration_set,
                packet_size,
            )
        return hik_api().open_camera_color(
            cam,
            str(cam_idx),
            config.frame_height,
            config.line_rate,
            config.exposure_micros,
            config.gain[cam_idx],
            config.reversed[cam_idx],
            config.reverse_scan_direction[cam_idx],
            px_format,
            config.calibration_set,
            config.white_balance_rgb_factors[cam_idx],
            packet_size,
        )

    camera_infos = get_camera_infos()
    for if_name in set(cam.interface_name for cam in camera_infos):
        check_interface(if_name)
    return [open_cam(i, cam) for i, cam in enumerate(camera_infos)]


def open_hik_camera_producer_array(
    config: CameraArrayConfig,
    missing_frames_fatal=True,
    report_metrics=True,
    differentiator: str | None = None,
) -> Sequence[HikCameraProducer]:
    return [
        HikCameraProducer(
            i,
            gev_cam,
            config,
            missing_frames_fatal=missing_frames_fatal,
            report_metrics=report_metrics,
            differentiator=f"{differentiator}.{i}" if differentiator else f"{i}",
        )
        for i, gev_cam in enumerate(open_hik_camera_array(config))
    ]
