import logging
import socket
from collections import defaultdict
from struct import calcsize, pack, unpack
from typing import Callable

from .tcp_client import binary_socket
from ..process.thread import start_thread

PACKET_FORMAT = ">BI8s"
PACKET_LENGTH = calcsize(PACKET_FORMAT)


class FrameListener:
    def __init__(self, data_format: str, listener: Callable) -> None:
        self.data_format = data_format
        self.listener = listener
        self.data_len = calcsize(data_format)

    def process(self, data: bytes):
        self.listener(*unpack(self.data_format, data[: self.data_len]))


class UsrCanet200:
    def __init__(self, host: str = "USR-CANET200", *, keep_alive_frame_id: int | None = None) -> None:
        self.log = logging.getLogger(self.__class__.__name__)
        self.keep_alive_frame_id = keep_alive_frame_id
        self.socket = binary_socket(host, 20001, timeout=5 * 60 if keep_alive_frame_id else None)
        start_thread(self.log, self._receive_worker)
        self.id_map_listeners: dict[int, list[FrameListener]] = defaultdict(list)

    def on_frame(self, frame_id: int, data_format: str, listener: Callable):
        self.id_map_listeners[frame_id].append(FrameListener(data_format, listener))

    def send(self, frame_id: int, data: bytes):
        if not (1 <= len(data) <= 8):
            raise RuntimeError(f"Invalid data length: {len(data)}")
        msg = pack(PACKET_FORMAT, len(data), frame_id, data)
        self.socket.sendall(msg)
        self.log.debug(f"Sent frame: {msg!r}")

    def _receive_worker(self):
        accumulated = b""
        while True:
            try:
                chunk = self.socket.recv(PACKET_LENGTH - len(accumulated))
            except socket.timeout:
                if accumulated:
                    raise RuntimeError("Socket timed out part way through a packet")
                if self.keep_alive_frame_id:
                    self.send(self.keep_alive_frame_id, b"\x00")
                continue
            if not chunk:
                raise RuntimeError("Socket connection broken")
            accumulated += chunk
            if len(accumulated) < PACKET_LENGTH:
                continue
            self.log.debug(f"Got frame: {accumulated!r}")
            info, frame_id, data = unpack(PACKET_FORMAT, accumulated)
            accumulated = b""
            for listener in self.id_map_listeners[frame_id]:
                listener.process(data)
