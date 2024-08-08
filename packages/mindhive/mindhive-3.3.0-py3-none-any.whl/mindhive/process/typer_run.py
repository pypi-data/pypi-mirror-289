from os import path as osp

import inspect
import logging
import sys
from time import monotonic

from click.exceptions import Exit, ClickException
from typer import Typer
from typer.main import get_command
from typing import Callable

from ..log.exception_handling import ensure_exception_handling_installed

log = logging.getLogger("typer_run")


def _typer_run(func: Callable, app_name: str | None = None, args: list[str] | None = None):
    if args is None:
        args = []
    app = Typer(add_completion=False)
    app.command()(func)
    command = get_command(app)
    try:
        with command.make_context(app_name, args) as ctx:
            return command.invoke(ctx)
    except Exit as err:
        sys.exit(err.exit_code)
    except ClickException as err:
        err.show()
        sys.exit(err.exit_code)


def typer_run(main: Callable):
    ensure_exception_handling_installed()
    app_name = inspect.stack()[1].filename
    if app_name.endswith("/__main__.py"):
        app_name = osp.dirname(app_name)
    args = sys.argv[1:]
    log.info(f"Starting: {app_name} {' '.join(args)}")
    start_time = monotonic()
    try:
        _typer_run(main, app_name, args)
    finally:
        elapsed_time = monotonic() - start_time
        log.info(f"Runtime: {elapsed_time:,.0f}s")


def typer_env_var_parse(func: Callable):
    return _typer_run(func)
