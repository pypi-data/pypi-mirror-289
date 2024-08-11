from typing import Annotated
from zyjared_color import red
import typer
from ..helpers.version import PRE_MODE, MODE, pre_version, mode_version, dump_version
from ..helpers.log import log_run
from zyjared_color import Color

__all__ = [
    'app'
]

app = typer.Typer()


def _result(dic: dict):
    old = dic['old']
    now = dic['now']

    _len_old = len(old)
    _len_now = len(now)
    _min = min(_len_old, _len_now)

    def _log(t): return str(Color(t).red())

    for i in range(_min):
        if old[i] != now[i]:
            old[i] = _log(old[i])
            now[i] = _log(now[i])

    if _len_old > _len_now:
        for i in range(_len_now, _len_old):
            old[i] = _log(old[i])
    elif _len_old < _len_now:
        for i in range(_len_old, _len_now):
            now[i] = _log(now[i])
    else:
        pass

    return {
        'old': dump_version(old),
        'now': dump_version(now),
    }


def _mode_wrapper(mode: str):
    def _wrapper(
        down: Annotated[
            bool,
            typer.Option(
            '-d',
            '--down',
            help=f"Downgrade the version in {red(mode)} mode.",)
        ] = False
    ):
        log_run(
            lambda: _result(mode_version(mode, down=down, save=True)),
            cli='version',
        )
    return _wrapper


def _pre_wrapper(mode: str):
    def _wrapper(
        down: Annotated[
            bool,
            typer.Option(
            '-d',
            '--down',
            help=f"Downgrade the version in {red(mode)} mode.",)
        ] = False
    ):
        log_run(
            lambda: _result(pre_version(mode, down=down, save=True)),
            cli='version',
        )
    return _wrapper


for _mode in MODE:
    app.command(_mode)(_mode_wrapper(_mode))

for _mode in PRE_MODE:
    app.command(_mode)(_pre_wrapper(_mode))
