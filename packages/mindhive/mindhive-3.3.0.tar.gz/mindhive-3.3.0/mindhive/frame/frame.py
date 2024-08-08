from dataclasses import dataclass, field, replace
from typing import Self, Any

import numpy as np

from ..strip.rendering import Rendering


@dataclass(frozen=True)
class Frame:
    cam_idx: int
    id: int
    timestamp: float
    img: np.ndarray | None = field(compare=False)
    rendering: Rendering

    def __repr__(self) -> str:
        parts: list[str] = [
            self.__class__.__name__,
            f"cam_idx: {self.cam_idx}",
            f"id: {self.id}>",
            f"rendering: {self.rendering.name}>",
        ]
        if self.img is None:
            parts.append("INVALIDATED")
        return f"<{" ".join(parts)}>"

    @property
    def is_filled(self) -> bool:
        return self.img is not None

    def replace_img(
        self,
        img: np.ndarray,
        rendering: Rendering | None = None,
    ) -> Self:
        replace_fields: dict[str, Any] = {"img": img}
        if rendering is not None:
            replace_fields["rendering"] = rendering
        return replace(self, **replace_fields)

    def invalidate(self) -> Self:
        return replace(self, img=None)
