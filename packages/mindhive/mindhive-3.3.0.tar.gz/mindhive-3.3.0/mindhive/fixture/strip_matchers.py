import numpy as np
from dataclasses import dataclass

from ..strip.strip import Strip
from ..strip.strip_masked import StripMasked


@dataclass(frozen=True)
class MatchStrip(Strip):
    def __eq__(self, o: object) -> bool:
        if not super().__eq__(o) or not isinstance(o, Strip):
            return False
        if self.img.dtype.kind == "f":
            return np.allclose(self.img, o.img)
        return np.array_equal(self.img, o.img)


@dataclass(frozen=True)
class MatchStripMasked(StripMasked):
    def disconnected(self):
        return MatchStripMasked(self.strip.disconnected(), self.mask)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, StripMasked) and o.strip == self.strip and np.array_equal(self.mask, o.mask)
