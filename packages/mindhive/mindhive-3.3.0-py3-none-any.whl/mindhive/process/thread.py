from concurrent.futures import as_completed, Future
from logging import Logger

import logging
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread
from typing import Callable, Iterable

from ..log.exception_handling import ensure_exception_handling_installed, critical_thread_exception
from .cleanup import ThreadSweeper


def start_thread(log: logging.Logger, target: Callable, stop: Callable | None = None):
    def wrapped_target():
        try:
            return target()
        except BaseException as err:
            critical_thread_exception(err, log)

    ensure_exception_handling_installed()
    thread = Thread(name=log.name, target=wrapped_target, daemon=True)
    thread.start()
    log.debug(f"Started thread id: 0x{thread.ident:x}, PID: {thread.native_id}")
    ThreadSweeper.register(stop, thread.join)


def long_lived_thread_executor(max_workers: int, log: Logger) -> ThreadPoolExecutor:
    def stop():
        executor.shutdown(wait=False, cancel_futures=True)

    def wait():
        executor.shutdown(wait=True)

    executor = ThreadPoolExecutor(max_workers, thread_name_prefix=log.name)
    ThreadSweeper.register(stop, wait)
    return executor


def exec_all(futures: Iterable[Future]):
    futures = set(futures)  # Hold on to it
    for f in as_completed(futures):
        err = f.exception(timeout=0)
        if err is not None:
            logging.error(f"Cancelling futures due to exception", exc_info=err)
            for future in futures:
                future.cancel()
            logging.info(f"Will have to wait for already running tasks to complete")
            raise err
