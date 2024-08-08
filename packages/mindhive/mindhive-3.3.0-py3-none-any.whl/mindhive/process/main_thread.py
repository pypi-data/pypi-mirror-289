from time import sleep

from ..log.exception_handling import ensure_exception_handling_installed
from .pipeline_component import PipelineComponent


def hold_main_thread(timeout: float | None = None):
    ensure_exception_handling_installed()
    PipelineComponent.sanity_check_all()
    if timeout is not None:
        sleep(timeout)
    else:
        while True:
            sleep(60)
