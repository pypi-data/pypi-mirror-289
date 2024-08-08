from dataclasses import dataclass

import numpy as np
from ..log.timestamp import timestamp_to_iso

from .strip import Strip


@dataclass(frozen=True)
class StripMasked:
    strip: Strip
    mask: np.ndarray

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {timestamp_to_iso(self.strip.timestamp)}>"
