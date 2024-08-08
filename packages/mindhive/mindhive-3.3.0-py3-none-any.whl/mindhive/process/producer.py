from abc import ABC, abstractmethod
from typing import Callable

from .data_vehicle import DataVehicle
from .pipeline_component import PipelineComponent

type CompletedCallback = Callable[[], None]
type DataListener[D] = Callable[[DataVehicle[D], CompletedCallback | None], None]


class Producer[R](ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def send_to(self, listener: DataListener[R]): ...


class ProducerImpl[R](PipelineComponent, Producer[R]):
    def __init__(self) -> None:
        super().__init__()
        self.__listeners: list[DataListener[R]] = []
        self._have_downstream = False

    def send_to(self, listener: DataListener[R]):
        self._have_downstream = True
        self.__listeners.append(listener)

    def _push(self, dv: DataVehicle[R]):
        for listener in self.__listeners:
            listener(dv, None)

    def sanity_check(self):
        super().sanity_check()
        if not self._have_downstream:
            raise RuntimeError(f"Not linked downstream: {self.name}")
