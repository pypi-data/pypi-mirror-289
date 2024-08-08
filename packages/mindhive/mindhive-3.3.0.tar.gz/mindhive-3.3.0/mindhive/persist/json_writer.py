import json
import logging
from typing import Mapping

from ..debug.external_output import block_external_output
from .dirs import STORE_DIR


class PersistForPushJsonWriter:
    _used_noun_sources = set()

    def __init__(self, noun: str, source: str) -> None:
        self.source = source
        self.log = logging.getLogger(f"{self.__class__.__name__}.{noun}.{source}")
        self.dir = STORE_DIR / noun
        self.dir.mkdir(parents=True, exist_ok=True)
        key = (noun, source)
        if key in PersistForPushJsonWriter._used_noun_sources:
            raise RuntimeError(f"Duplicated noun/source: {key}")
        PersistForPushJsonWriter._used_noun_sources.add(key)

    def write(self, local_id: str, data: Mapping):
        json_path = self.dir / f"{local_id}-{self.source}.json"
        if block_external_output():
            self.log.info(f"Blocking writing {json_path}")
            return
        if self.log.isEnabledFor(logging.DEBUG):
            self.log.debug(f"Writing {json_path}:\n{data!r}")
        else:
            self.log.info(f"Writing {json_path}")
        json_path.write_text(json.dumps(data))
