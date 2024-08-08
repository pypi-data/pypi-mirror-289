from ctypes import c_uint16
from typing import Mapping

import numpy as np

from ..gev.px_format import PxFormat
from ..gev.px_layout import PxLayout


class HikRGToRBGGFormat(PxFormat):
    def __init__(self, code: int) -> None:
        super().__init__(code, binning=False)

    # noinspection PyShadowingBuiltins
    def rgb_views(self, img: np.ndarray, reversed: bool) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        green = img[:, :, 1]
        red = img[:, 0::2, 0]
        blue = img[:, 1::2, 0]
        return red, green, blue

    def copy_image_from_buffer(self, buf: np.ndarray) -> np.ndarray:
        buf_h, buf_w = buf.shape
        result = np.empty((buf_h // 2, buf_w, 2), self.ctype)
        r, g, b = self.rgb_views(result, False)
        r[:] = buf[0::2, 0::2]
        b[:] = buf[1::2, 1::2]
        g[:, 0::2] = buf[0::2, 1::2]
        g[:, 1::2] = buf[1::2, 0::2]
        return result


class HikRGToRBGGFormat12Bit(HikRGToRBGGFormat):
    @property
    def bits_per_px(self) -> int:
        return 12

    @property
    def ctype(self):
        return c_uint16


HIK_LAYOUT_MAP_FORMAT: Mapping[PxLayout, PxFormat] = {
    PxLayout.BGR_8: PxFormat(0x02180015, binning=False),
    PxLayout.BGR_8_BINNING: PxFormat(0x02180015, binning=True),
    PxLayout.MONO_8: PxFormat(0x01080001, mono=True),
    PxLayout.BAYER_8: HikRGToRBGGFormat(0x01080009),
    PxLayout.BAYER_12: HikRGToRBGGFormat12Bit(0x01100011),
}
