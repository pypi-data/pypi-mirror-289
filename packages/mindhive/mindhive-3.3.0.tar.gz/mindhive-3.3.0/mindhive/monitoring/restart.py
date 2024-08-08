import logging
from datetime import timedelta
from typing import Callable

import sys
from time import sleep

from ..log.termination_log import write_termination_message
from ..log.trace import tracer
from .downtime import is_downtime
from ..process.main_thread import hold_main_thread
from ..process.unit import Unit

log = logging.getLogger("restart")

MINIMUM_RUNTIME = timedelta(hours=8)
CHECK_DOWNTIME_PERIOD = timedelta(minutes=15)
PAUSE_BEFORE_EXIT_TIME = timedelta(seconds=60)


def hold_main_thread_with_restart(
    unit: Unit,
    on_restart: Callable[[], None] | None = None,
    restart_predicate: Callable[[], bool] | None = None,
):
    hold_main_thread(MINIMUM_RUNTIME.total_seconds())
    while True:
        with tracer.trace("hold_main_thread_with_restart.check"):
            want_restart = (restart_predicate is None or restart_predicate()) and is_downtime(unit)
            if want_restart:
                log.info("Initiating restart during downtime")
                write_termination_message("Restarting during downtime")
                if on_restart is not None:
                    on_restart()
                pause_seconds = PAUSE_BEFORE_EXIT_TIME.total_seconds()
                log.info(f"Pausing for {pause_seconds:.0f}s")
                sleep(pause_seconds)
                log.info("Exiting...")
        if want_restart:
            # Perform exit in here so trace does not capture SystemExit as an exception
            sys.exit(0)
        hold_main_thread(CHECK_DOWNTIME_PERIOD.total_seconds())
