from dataclasses import dataclass, field, replace
from typing import Sequence, Self

import numpy as np

from ..log.timestamp import timestamp_to_iso
from .rendering import Rendering


@dataclass(frozen=True)
class Strip:
    timestamp: float
    img: np.ndarray = field(compare=False)
    contiguous: bool
    rendering: Rendering
    frame_widths: Sequence[int] | None = None

    @property
    def w(self) -> int:
        return self.img.shape[1]

    @property
    def h(self) -> int:
        return self.img.shape[0]

    def replace_img(self, img: np.ndarray) -> Self:
        return replace(self, img=img)

    def disconnected(self) -> Self:
        return replace(self, contiguous=False)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {timestamp_to_iso(self.timestamp)}>"

    def __post_init__(self):
        self.img.setflags(write=False)
