from ctypes import c_uint8
from typing import Any

import cv2 as cv
import numpy as np


class PxFormat:
    def __init__(self, code: int, *, binning=False, mono=False) -> None:
        self.code = code
        self.binning = binning
        self.mono = mono

    @property
    def bits_per_px(self) -> int:
        return 8

    @property
    def max_value(self) -> int:
        return 2**self.bits_per_px - 1

    @property
    def ctype(self) -> Any:
        return c_uint8

    def copy_image_from_buffer(self, buf: np.ndarray) -> np.ndarray:
        return buf.copy()

    # noinspection PyShadowingBuiltins
    def rgb_views(self, img: np.ndarray, reversed: bool) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        raise NotImplementedError(f"{self=} does is not RGB")


class RgbToBgrFormat(PxFormat):
    def copy_image_from_buffer(self, buf: np.ndarray) -> np.ndarray:
        return cv.cvtColor(buf, cv.COLOR_RGB2BGR)

    # noinspection PyShadowingBuiltins
    def rgb_views(self, img: np.ndarray, reversed: bool) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        return img[:, :, 2], img[:, :, 1], img[:, :, 0]
