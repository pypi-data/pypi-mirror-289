import faulthandler
import logging
import os
import signal
import sys
import threading
from threading import RLock
from types import TracebackType
from typing import Type, Never

from .termination_log import write_termination_message, write_termination_exc_info

_log = logging.getLogger("exception_handling")
_exception_handling_installed = False
_raise_sigint_check_lock = RLock()
_have_raised_sigint = False


def exception_to_exc_info(exception: BaseException):
    try:
        tb = exception.__traceback__
    except AttributeError:
        tb = None
    return type(exception), exception, tb


def _log_critical_exc_info(exc_info, log: logging.Logger | None = None):
    try:
        (exc_type, value, traceback) = exc_info
        (log or _log).critical(f"{exc_type.__name__}: {value}", exc_info=exc_info)
        write_termination_exc_info(exc_info)
    except:  # noqa
        print("Failed to log exc_info:", exc_info)


def _handle_critical_thread_exc_info(exc_info, log: logging.Logger | None = None):
    with _raise_sigint_check_lock:
        global _have_raised_sigint
        raise_sigint = not _have_raised_sigint
        _have_raised_sigint = True
    _log_critical_exc_info(exc_info, log)
    if raise_sigint:
        _log.info("Sending internal SIGINT")
        os.kill(os.getpid(), signal.SIGINT)


def _sys_excepthook(exc_type: Type[BaseException], value: BaseException, traceback: TracebackType | None):
    # Note: SystemExit does not trigger sys.excepthook
    exc_info = (exc_type, value, traceback)
    if isinstance(value, SystemExit):
        _log.info("SystemExit raised")  # Assuming someone has handled this already
    elif isinstance(value, KeyboardInterrupt):
        if _have_raised_sigint:
            _log.info("Caught internal SIGINT in main thread")
            sys.exit(1)  # Otherwise the exit code will be 130 from SIGINT we raised
        else:
            _log.warning("Received external SIGINT/KeyboardInterrupt, exiting", exc_info=exc_info)
            write_termination_message("Received SIGINT")
    else:
        _log_critical_exc_info(exc_info)


def _threading_excepthook(args):
    _log.critical(f"Unhandled exception in thread: {args.thread}")
    exc_info = args.exc_type, args.exc_value, args.exc_traceback
    _handle_critical_thread_exc_info(exc_info)


def ensure_exception_handling_installed():
    global _exception_handling_installed
    if not _exception_handling_installed:
        _log.debug("Installing excepthooks")
        sys.excepthook = _sys_excepthook
        threading.excepthook = _threading_excepthook
        faulthandler.enable()
        if os.getenv("THREAD_DUMP_ON_SIGINT"):
            faulthandler.register(signal.SIGINT, chain=True)
        _exception_handling_installed = True


def critical_thread_exception(exception: BaseException, log: logging.Logger | None = None) -> Never:
    _handle_critical_thread_exc_info(exception_to_exc_info(exception), log)
    sys.exit(1)
