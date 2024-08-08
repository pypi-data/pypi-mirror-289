import traceback
from pathlib import Path

LOG_PATH = Path("/dev/termination-log")


def write_termination_message(message: str):
    if LOG_PATH.exists():
        with open(LOG_PATH, "a") as f:
            print(message, file=f)


have_written_termination_exc_info = False


def write_termination_exc_info(exc_info):
    global have_written_termination_exc_info
    if not have_written_termination_exc_info:
        if LOG_PATH.exists():
            with open(LOG_PATH, "a") as f:
                traceback.print_exception(*exc_info, file=f)
            have_written_termination_exc_info = True
