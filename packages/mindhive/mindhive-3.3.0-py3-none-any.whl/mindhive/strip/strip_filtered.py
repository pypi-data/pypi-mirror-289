from enum import auto, Enum
from .strip_masked import StripMasked


class AccumulateEvent(Enum):
    DONE = auto()
    RESET = auto()


StripFiltered = AccumulateEvent | StripMasked
