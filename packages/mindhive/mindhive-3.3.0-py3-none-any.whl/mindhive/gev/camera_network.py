import logging
import os

import ping3
import psutil
from ping3 import ping
from ping3.errors import PingError

PING_PACKET_HEADER_SIZE = 28
STANDARD_NIC_MTU = 1500

SKIP_PING_ENV_VAR = "SKIP_PING"

log = logging.getLogger(__name__)

_interface_stats = None

ping3.EXCEPTIONS = True


def get_packet_size(interface_name: str) -> int:
    global _interface_stats
    if _interface_stats is None:
        _interface_stats = psutil.net_if_stats()
    packet_size = min(_interface_stats[interface_name].mtu, 9000)
    if packet_size <= STANDARD_NIC_MTU:
        log.warning(
            f"Interface: {interface_name} MTU: {packet_size} seems low, has NIC being configured for jumbo frames?"
        )
    return packet_size


def check_network(ip: str, packet_size: int, interface: str):
    if os.getenv(SKIP_PING_ENV_VAR):
        return
    log.debug(f"Testing camera: {ip} for packet size: {packet_size} on: {interface}")
    try:
        ping(ip, timeout=1, interface=interface, size=packet_size - PING_PACKET_HEADER_SIZE)
    except PingError:
        raise RuntimeError(f"Packet size: {packet_size} test for camera: {ip} on: {interface} failed")
