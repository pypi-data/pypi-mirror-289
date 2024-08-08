from io import TextIOWrapper
from socket import AF_INET, IPPROTO_TCP, SO_KEEPALIVE, SOCK_STREAM, socket, SOL_SOCKET, TCP_NODELAY
from typing import Literal


def binary_socket(host: str, port: int, timeout: int | None = None, connect_timeout=5) -> socket:
    result = socket(AF_INET, SOCK_STREAM)
    result.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
    result.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)
    result.settimeout(connect_timeout)
    result.connect((host, port))
    result.settimeout(timeout)
    return result


def text_stream(
    host: str,
    port: int,
    timeout: int | None = None,
    mode: Literal["r", "w", "rw", "wr"] = "rw",
    encoding="ascii",
    newline=None,
    line_buffering=True,
) -> TextIOWrapper:
    binary = binary_socket(host, port, timeout)
    # noinspection PyTypeChecker
    stream: TextIOWrapper = binary.makefile(mode, encoding=encoding, newline=newline)
    if line_buffering:
        try:
            stream.reconfigure(line_buffering=line_buffering)
        except:  # noqa
            stream.close()
            raise
    return stream
