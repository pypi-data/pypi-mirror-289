from typing import Annotated
from zyjared_color import red
import typer
from ..helpers.version import PRE_MODE, MODE, pre_version, mode_version, _result
from ..helpers.log import log_run

__all__ = [
    'app'
]

app = typer.Typer()


@app.callback()
def callback():
    """
    This command can be used to update the version of `pyproject.toml`.

    Example:

        $ zyjared-cli version patch

        $ zyjared-cli version patch --down

        $ zyjared-cli version alpha

        $ zyjared-cli version alpha --down

        $ ...
    """


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

    _wrapper.__name__ = mode
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

    _wrapper.__name__ = mode
    return _wrapper


def _mock(index: int, n: int):
    return [str(n) if i == index else '0' for i in range(3)]


def _help(ls0, ls1):
    res = _result({'old': ls0, 'now': ls1})
    return f"{res['old']} -> {res['now']}"


for _mode in MODE:
    i = MODE.index(_mode)

    app.command(
        _mode,
        short_help=_help(_mock(i, 0), _mock(i, 1)),
    )(_mode_wrapper(_mode))

for _mode in PRE_MODE:
    app.command(
        _mode,
        short_help=_help(['0', '0', '0'], ['0', '0', '0', _mode, '1']),
    )(_pre_wrapper(_mode))
