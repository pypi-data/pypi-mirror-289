from abc import abstractmethod
from typing import Any, Callable, Never

from .consumer import Consumer
from .data_vehicle import DataVehicle
from .worker import Worker

type DataPush[D] = Callable[[DataVehicle[D]], None]


class Transformer[D, R](Worker):
    @abstractmethod
    def process(self, dv: DataVehicle[D], push: DataPush[R]) -> None: ...


class SimpleTransformer[D, R](Transformer[D, R]):
    def process(self, dv, push) -> None:
        result = self._process_data(dv.data)
        push(DataVehicle(result, dv))

    @abstractmethod
    def _process_data(self, data: D, /) -> R: ...


class IdentityTransformerAdapter[D](Transformer[D, D]):
    def __init__(self, consumer: Consumer[D]) -> None:
        super().__init__(consumer.name)
        self.consumer = consumer

    @property
    def trace_name(self) -> str:
        return self.consumer.name

    def process(self, dv, push) -> None:
        self.consumer.process(dv)
        push(dv)


class SinkTransformer(Transformer[Any, Never]):
    def process(self, dv, push) -> None:
        pass
