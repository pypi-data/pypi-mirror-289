from abc import ABC, abstractmethod

from .data_vehicle import DataVehicle
from .worker import Worker


class Consumer[D](Worker, ABC):
    @abstractmethod
    def process(self, dv: DataVehicle[D]) -> None: ...


class SimpleConsumer[D](Consumer[D], ABC):
    def process(self, dv) -> None:
        self._process_data(dv.data)

    @abstractmethod
    def _process_data(self, data: D, /) -> None: ...


class SinkConsumer(Consumer):
    def process(self, dv) -> None:
        pass
