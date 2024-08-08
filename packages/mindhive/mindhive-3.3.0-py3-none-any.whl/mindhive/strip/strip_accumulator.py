from typing import Sequence

import numpy as np

from .strip import Strip
from .strip_masked import StripMasked


class StripAccumulator:
    def __init__(self, strip: Strip) -> None:
        self.w = strip.w
        self.rendering = strip.rendering
        self.start_timestamp = strip.timestamp
        self.strips = [strip.disconnected()]
        self._h: int | None = None

    def append(self, strip: Strip):
        self._h = None
        self.strips.append(strip)

    @property
    def h(self) -> int:
        if self._h is None:
            self._h = sum(strip.h for strip in self.strips)
        return self._h

    @property
    def height_per_width(self) -> float:
        return self.h / self.w

    @property
    def strip_count(self) -> int:
        return len(self.strips)

    @property
    def end_timestamp(self) -> float:
        return self.strips[-1].timestamp

    @property
    def img(self) -> np.ndarray:
        return np.vstack([strip.img for strip in self.strips])

    @property
    def frame_widths(self) -> Sequence[int] | None:
        return self.strips[0].frame_widths


class StripMaskedAccumulator(StripAccumulator):
    def __init__(self, strip_masked: StripMasked) -> None:
        super().__init__(strip_masked.strip)
        self.masks = [strip_masked.mask]

    def append(self, strip_masked: StripMasked):  # pyright: ignore [reportIncompatibleMethodOverride]
        super().append(strip_masked.strip)
        self.masks.append(strip_masked.mask)

    @property
    def mask(self) -> np.ndarray:
        return np.vstack(self.masks)
