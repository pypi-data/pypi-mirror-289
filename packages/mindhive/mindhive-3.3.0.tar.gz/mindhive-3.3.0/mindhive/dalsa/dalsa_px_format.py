from typing import Mapping

import numpy as np

from ..gev.px_format import PxFormat, RgbToBgrFormat
from ..gev.px_layout import PxLayout


class DalsaBayerRBGGFormat(PxFormat):
    """
    Bayer format:
    RBRBRB...
    GGGGGG...
    """

    def __init__(self, code: int):
        super().__init__(code, binning=False)

    # noinspection PyShadowingBuiltins
    def rgb_views(self, img: np.ndarray, reversed: bool) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        green = img[:, :, 1]
        left = img[:, 0::2, 0]
        right = img[:, 1::2, 0]
        if reversed:
            return right, green, left
        else:
            return left, green, right


class DalsaBayerRBGGFormat12BitPacked(DalsaBayerRBGGFormat):
    @property
    def bits_per_px(self) -> int:
        return 12

    def copy_image_from_buffer(self, buf: np.ndarray) -> np.ndarray:
        # From https://stackoverflow.com/a/51967333/3424884
        fst_uint8, mid_uint8, lst_uint8 = np.reshape(buf, (buf.size // 3, 3)).astype(np.uint16).T
        fst_uint12 = (fst_uint8 << 4) + (mid_uint8 >> 4)
        snd_uint12 = (lst_uint8 << 4) + (np.bitwise_and(0xF, mid_uint8))
        result = np.reshape(np.concatenate((fst_uint12[:, None], snd_uint12[:, None]), axis=1), (*buf.shape[:2], 2))
        return result


DALSA_LAYOUT_MAP_FORMAT: Mapping[PxLayout, PxFormat] = {
    PxLayout.BGR_8: RgbToBgrFormat(0x02180014, binning=False),
    PxLayout.BGR_8_BINNING: RgbToBgrFormat(0x02180014, binning=True),
    PxLayout.BAYER_8: DalsaBayerRBGGFormat(0),  # REVISIT: Dunno what 8bit is
    PxLayout.BAYER_12: DalsaBayerRBGGFormat12BitPacked(0x021800AC),
}
