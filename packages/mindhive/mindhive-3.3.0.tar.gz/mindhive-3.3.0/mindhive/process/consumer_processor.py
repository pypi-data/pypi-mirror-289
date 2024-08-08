from abc import abstractmethod

from .producer import Producer


class ConsumerProcessor[D]:
    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def receive_from(self, producer: Producer[D]): ...
