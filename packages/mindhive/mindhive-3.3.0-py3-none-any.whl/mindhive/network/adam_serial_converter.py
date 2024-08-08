import logging
from socket import timeout
from typing import Callable

from time import sleep, monotonic

from .tcp_client import text_stream, binary_socket
from ..process.thread import start_thread

DATA_PORT = 5300
CONTROL_PORT = 5400

PING_PERIOD = 2


class Adam4571:
    def __init__(self, host: str) -> None:
        self.log = logging.getLogger(self.__class__.__name__)
        self.control_stream = text_stream(host, CONTROL_PORT, newline="\r", timeout=2 * PING_PERIOD)
        start_thread(self.log, self._heartbeat_worker)

    def _heartbeat_worker(self):
        while True:
            sleep(PING_PERIOD)
            self.control_stream.write("AT\r")
            try:
                for response in self.control_stream:
                    self.log.debug(f"Control response: {response!r}")
                    if not response:
                        raise RuntimeError("Control socket disconnected")
                    clean_response = response.rstrip("\r\n")
                    if not clean_response:
                        continue
                    if clean_response == "OK":
                        break
                    raise RuntimeError(f"Unexpected AT command response: {response!r}")
            except timeout:
                raise RuntimeError("Control socket not responding")


PacketCallable = Callable[[bytes], None]


class Adam4571StxEtxPacketReader(Adam4571):
    def __init__(
        self,
        host: str,
        stx: bytes = b"\x02",
        etx: bytes = b"\x03",
    ) -> None:
        super().__init__(host)
        self.stx = stx
        self.etx = etx
        self.data_stream = binary_socket(host, 5300)
        self.buffer: bytes = b""
        self.packet_listeners: list[PacketCallable] = []
        start_thread(self.log, self._data_worker)

    def on_packet(self, listener: PacketCallable):
        self.packet_listeners.append(listener)

    def _data_worker(self):
        while True:
            while True:
                split = self.buffer.split(self.stx, 1)
                if len(split) == 2:
                    superfluous, self.buffer = split
                    break
                self.buffer += self.data_stream.recv(1024)
                continue
            while True:
                split = self.buffer.split(self.etx, 1)
                if len(split) == 2:
                    data, self.buffer = split
                    for listener in self.packet_listeners:
                        listener(data)
                    break
                self.buffer += self.data_stream.recv(1024)
                continue


LineCallable = Callable[[str], None]


class Adam4571LineReader(Adam4571):
    def __init__(self, host: str) -> None:
        super().__init__(host)
        self.data_stream = text_stream(host, 5300, mode="r")
        self.line_listeners: list[LineCallable] = []
        start_thread(self.log, self._data_worker)

    def on_line(self, listener: LineCallable):
        self.line_listeners.append(listener)

    def _data_worker(self):
        for line in self.data_stream:
            self.log.debug(f"Data response: {line!r}")
            if not line:
                raise RuntimeError("Socket disconnected")
            clean_line = line.rstrip("\n")
            for listener in self.line_listeners:
                listener(clean_line)


if __name__ == "__main__":

    def log_packet_timing_anomaly(packet: bytes):
        global last_ts
        now = monotonic()
        if last_ts is not None:
            elapsed = now - last_ts
            if elapsed > 0.15:
                print(f"Unexpected elapsed: {elapsed:.3f}s")
        last_ts = now

    last_ts = None
    reader = Adam4571StxEtxPacketReader("10.103.1.41")
    reader.on_packet(log_packet_timing_anomaly)
    while True:
        sleep(1)
