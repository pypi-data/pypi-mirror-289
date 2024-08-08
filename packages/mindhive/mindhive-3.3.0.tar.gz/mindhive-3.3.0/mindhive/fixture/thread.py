import traceback

from threading import Thread

import sys


def print_thread_stack(thread: Thread):
    for thread_id, frame in sys._current_frames().items():
        if thread_id == thread.ident:
            traceback.print_stack(frame, file=sys.stdout)
