from abc import ABC

from .consumer_processor import ConsumerProcessor
from .producer import Producer


class TransformerProcessor[D, R](ConsumerProcessor[D], Producer[R], ABC):
    pass
