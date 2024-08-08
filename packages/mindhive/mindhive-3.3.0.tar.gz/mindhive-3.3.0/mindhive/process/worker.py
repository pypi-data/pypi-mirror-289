import logging


class Worker:
    def __init__(self, differentiator: str | None = None) -> None:
        self.name = self.__class__.__name__
        if differentiator:
            self.name = f"{self.name}.{differentiator}"
        self.log = logging.getLogger(self.name)

    @property
    def trace_name(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<{self.name}>"
