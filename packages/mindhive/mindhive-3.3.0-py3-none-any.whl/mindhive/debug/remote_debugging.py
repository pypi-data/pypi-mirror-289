import sys
import os
from pathlib import Path
import logging


def setup_remote_debugger(server: str, port: int, stdout_to_server: bool = True, stderr_to_server: bool = True) -> None:
    logging.info(f"Remote Debugger: {server}:{port}")

    try:
        import pydevd_pycharm

        logging.info("Remote debugging: PyDevD loaded")
    except Exception:
        egg = Path(__file__).parent / "pydevd-pycharm.egg"
        if egg.exists():
            sys.path.append(str(egg))
            import pydevd_pycharm

            logging.info("Remote debugging: PyDevD loaded from egg")
        else:
            logging.error("Remote debugging: pydevd-pycharm.egg not found!")
            pydevd_pycharm = None

    if pydevd_pycharm:
        pydevd_pycharm.settrace(
            server,
            port=port,
            stdoutToServer=stdout_to_server,
            stderrToServer=stderr_to_server,
        )
    else:
        logging.debug("Remote debugging not enabled")


def init_remote_debugger() -> None:
    remote_debug: bool = os.getenv("REMOTE_DEBUG_ENABLE", "false") == "true"
    if remote_debug:
        server = os.getenv("REMOTE_DEBUG_SERVER")
        port = os.getenv("REMOTE_DEBUG_PORT")
        if server is not None and port is not None:
            try:
                setup_remote_debugger(server, int(port))
            except Exception as ex:
                logging.error("Error setting up remote debugging", ex.args)
