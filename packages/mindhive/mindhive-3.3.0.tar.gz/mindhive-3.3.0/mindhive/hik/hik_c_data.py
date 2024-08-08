import socket
from ctypes import c_char_p, Structure, c_uint, c_ushort, c_int64, c_float, c_uint8, POINTER
from ipaddress import IPv4Address
from typing import Mapping

from psutil import net_if_addrs


def decode_bytes(b: bytes) -> str:
    return b.decode("ascii")


def decode_pchar(pchar) -> str:
    return pchar.decode("ascii")


def encode_str(s: str | None) -> bytes | None:
    if s is None:
        return None
    return s.encode("ascii")


class FrameOutInfo(Structure):
    _fields_ = [
        ("nWidth", c_ushort),
        ("nHeight", c_ushort),
        ("enPixelType", c_int64),
        ("nFrameNum", c_uint),
        ("nDevTimeStampHigh", c_uint),
        ("nDevTimeStampLow", c_uint),
        ("nReserved0", c_uint),
        ("nHostTimeStamp", c_int64),
        ("nFrameLen", c_uint),
        ("nSecondCount", c_uint),
        ("nCycleCount", c_uint),
        ("nCycleOffset", c_uint),
        ("fGain", c_float),
        ("fExposureTime", c_float),
        ("nAverageBrightness", c_uint),
        ("nRed", c_uint),
        ("nGreen", c_uint),
        ("nBlue", c_uint),
        ("nFrameCounter", c_uint),
        ("nTriggerIndex", c_uint),
        ("nInput", c_uint),
        ("nOutput", c_uint),
        ("nOffsetX", c_ushort),
        ("nOffsetY", c_ushort),
        ("nChunkWidth", c_ushort),
        ("nChunkHeight", c_ushort),
        ("nLostPacket", c_uint),
        ("nReserved", c_uint * 39),
    ]


class MatchInfoNetDetect(Structure):
    _fields_ = [
        ("nReceivedDataSize", c_int64),
        ("nLostPacketCount", c_int64),
        ("nLostFrameCount", c_uint),
        ("nNetRecvFrameCount", c_uint),
        ("nRequestResendPacketCount", c_int64),
        ("nResendPacketCount", c_int64),
    ]


class FrameOut(Structure):
    _fields_ = [
        ("pBufAddr", POINTER(c_uint8)),
        ("stFrameInfo", FrameOutInfo),
        ("nReserved", c_uint * 16),
    ]


_interface_ip_map_name = None


def get_interface_ip_map_name() -> Mapping[IPv4Address, str]:
    global _interface_ip_map_name
    if _interface_ip_map_name is None:
        _interface_ip_map_name = {}
        for name, addrs in net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AddressFamily.AF_INET:
                    _interface_ip_map_name[IPv4Address(addr.address)] = name
    return _interface_ip_map_name


class CameraInfo(Structure):
    _fields_ = [
        ("index", c_uint),
        ("ipAddr", c_uint),
        ("_serial", c_char_p),
        ("interfaceIp", c_uint),
    ]

    @property
    def address(self) -> IPv4Address:
        return IPv4Address(self.ipAddr)

    @property
    def serial(self) -> str:
        return decode_pchar(self._serial)

    @property
    def interface_name(self) -> str:
        return get_interface_ip_map_name()[IPv4Address(self.interfaceIp)]
