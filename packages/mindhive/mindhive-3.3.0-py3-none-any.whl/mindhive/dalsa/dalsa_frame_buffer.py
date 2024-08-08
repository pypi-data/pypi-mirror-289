from ctypes import POINTER
from dataclasses import dataclass

import numpy as np

from .dalsa_c_data import BufferStats, BufferObject
from ..gev.px_format import PxFormat


@dataclass(frozen=True)
class DalsaFrameSnapshot:
    id: int
    image: np.ndarray
    device_micros: int


class DalsaFrameBuffer:
    def __init__(self, px_format: PxFormat) -> None:
        self.px_format = px_format
        self.buffer = POINTER(BufferObject)()
        self.stats = BufferStats()

    @property
    def has_contents(self) -> bool:
        return bool(self.buffer)

    def snapshot(self) -> DalsaFrameSnapshot:
        contents: BufferObject = self.buffer.contents
        if not contents.address:
            raise RuntimeError(f"Buffer image is empty, frame: {contents.id}")
        np_buf = np.ctypeslib.as_array(contents.address, (contents.h, contents.w, contents.d))
        return DalsaFrameSnapshot(contents.id, self.px_format.copy_image_from_buffer(np_buf), contents.timestamp)

    @property
    def trashed_count(self) -> int:
        return self.stats.trashed

    @property
    def used_count(self) -> int:
        return self.stats.total - self.stats.free
