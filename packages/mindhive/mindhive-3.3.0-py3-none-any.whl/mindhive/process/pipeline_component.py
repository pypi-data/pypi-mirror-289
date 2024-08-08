import logging
from logging import Logger
from threading import RLock
from typing import Self


class PipelineComponent:
    __global_list_lock = RLock()
    __global_list: list[Self] = []

    def __init__(self):
        super().__init__()
        self._log = None
        with PipelineComponent.__global_list_lock:
            PipelineComponent.__global_list.append(self)

    @property
    def name(self) -> str:
        differentiator = self.differentiator
        if differentiator is None:
            return self.__class__.__name__
        if self._differentiator_is_entire_name():
            return differentiator
        return f"{self.__class__.__name__}.{differentiator}"

    @staticmethod
    def _differentiator_is_entire_name() -> bool:
        return False

    @property
    def differentiator(self) -> str | None:
        return None

    @property
    def log(self) -> Logger:
        if self._log is None:
            self._log = logging.getLogger(self.name)
        return self._log

    def sanity_check(self):
        pass

    @staticmethod
    def sanity_check_all():
        with PipelineComponent.__global_list_lock:
            for component in PipelineComponent.__global_list:
                component.sanity_check()
