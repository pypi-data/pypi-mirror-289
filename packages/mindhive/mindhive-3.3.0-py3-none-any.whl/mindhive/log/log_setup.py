import logging
import os
from typing import Collection

import datadoglog
import sys
from .datadog_agent import has_datadog_agent
from .exception_handling import ensure_exception_handling_installed
from .gc_metrics import init_gc_metrics


def patch_better_exception_formatter(handler: logging.Handler):
    if not handler.formatter:
        return
    try:
        import better_exceptions  # pyright: ignore [reportMissingImports]
    except ModuleNotFoundError:
        return

    def _format_exception(ei):
        return "".join(better_exceptions.format_exception(*ei))

    handler.formatter.formatException = _format_exception


def init_logging(level=logging.INFO, debug: Collection[str] = ()):
    ensure_exception_handling_installed()
    if has_datadog_agent():
        datadoglog.init_logging()
        init_gc_metrics()
    else:
        logging.basicConfig(format=f"%(asctime)s:{logging.BASIC_FORMAT}", stream=sys.stdout)
        for handler in logging.getLogger().handlers:
            patch_better_exception_formatter(handler)
    root_log = logging.getLogger()
    if "DEBUG" in os.environ:
        level = logging.DEBUG
    root_log.setLevel(level)
    logging.getLogger("datadog.api").setLevel(logging.WARNING)
    for name in debug:
        logging.getLogger(name).setLevel(logging.DEBUG)
    if debug_loggers_env_var := os.getenv("DEBUG_LOGGERS"):
        for name in debug_loggers_env_var.split(","):
            logging.getLogger(name.strip()).setLevel(logging.DEBUG)
