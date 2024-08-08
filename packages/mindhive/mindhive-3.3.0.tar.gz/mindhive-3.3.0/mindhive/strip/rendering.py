from enum import Enum


class Rendering(Enum):
    color = "color"
    mono = "mono"
    profile = "profile"
    distance = "distance"

    def __init__(self, *_) -> None:
        self.tag = f"rendering:{self.value}"
