from ctypes import cast, POINTER, sizeof
from dataclasses import dataclass

import numpy as np
from time import time_ns

from ..gev.px_format import PxFormat
from .hik_c_data import FrameOut


@dataclass(frozen=True)
class HikFrameSnapshot:
    id: int
    image: np.ndarray
    frame_time: float


class HikFrame:
    def __init__(self, px_format: PxFormat) -> None:
        self.px_format = px_format
        self.frame = FrameOut()

    @property
    def has_contents(self) -> bool:
        return bool(self.frame.pBufAddr)

    def snapshot(self) -> HikFrameSnapshot:
        info = self.frame.stFrameInfo
        frame_id = info.nFrameNum
        if not self.frame.pBufAddr:
            raise RuntimeError(f"Buffer image is empty, frame: {frame_id}")
        frame_depth_float = info.nFrameLen / (info.nHeight * info.nWidth * sizeof(self.px_format.ctype))
        if frame_depth_float % 1 != 0:
            raise RuntimeError(
                f"Excepted nFrameLen: {info.nFrameLen} to be divisible by h*w: {info.nHeight}*{info.nWidth} in {self.px_format.ctype}"
            )
        buf = cast(self.frame.pBufAddr, POINTER(self.px_format.ctype))
        channels = int(frame_depth_float)
        shape = (info.nHeight, info.nWidth, channels) if channels > 1 else (info.nHeight, info.nWidth)
        np_buf = np.ctypeslib.as_array(buf, shape)
        data_to_make_frame_unique_beyond_ms = (time_ns() % 1_000_000) / 1_000_000_000
        frame_time = (info.nHostTimeStamp / 1_000) + data_to_make_frame_unique_beyond_ms
        return HikFrameSnapshot(frame_id, self.px_format.copy_image_from_buffer(np_buf), frame_time)

    @property
    def lost_packet_count(self) -> int:
        return self.frame.stFrameInfo.nLostPacket
