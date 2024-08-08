from typing import Callable, Self

type Callback = Callable[[], None]


class ThreadSweeper:
    capturing: Self | None = None

    def __init__(self, auto_shutdown=True) -> None:
        self.auto_shutdown = auto_shutdown
        self.stop_callbacks: list[Callback] = []
        self.wait_callbacks: list[Callback] = []

    @classmethod
    def register(cls, stop_callback: Callback | None, wait_callback: Callback | None = None):
        if cls.capturing:
            if stop_callback is None:
                raise RuntimeError("Must provide a stop callback when ThreadSweeper is capturing")
            cls.capturing.stop_callbacks.append(stop_callback)
            if wait_callback is not None:
                cls.capturing.wait_callbacks.append(wait_callback)

    def shutdown(self):
        for callback in self.stop_callbacks[::-1]:
            callback()
        for callback in self.wait_callbacks[::-1]:
            callback()
        self.stop_callbacks.clear()
        self.wait_callbacks.clear()

    def __enter__(self):
        if ThreadSweeper.capturing:
            raise RuntimeError("Already capturing, can't do that nested")
        ThreadSweeper.capturing = self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ThreadSweeper.capturing = None
        if self.auto_shutdown:
            self.shutdown()
