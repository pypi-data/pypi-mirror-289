from typing import Annotated, Any
from zyjared_color import red, italic
import toml
import typer
import inspect
from .app import app
from ..helpers.log import log_run
from ..helpers.config import get_config, CONFIG_PATH

__all__ = [
    'config',
]


DEFAULT = {
    'str': '',
    'list': [],
    'List': [],
    'dict': {},
    'Dict': {},
}

IGNORES = [
    'config'
]


def _ignore(cli: str):
    return cli in IGNORES


def _params(func):
    signature = inspect.signature(func)
    parameters = signature.parameters
    return [
        {
            'name': name,
            'type': parameter.annotation,
            'default': parameter.default
        } for name, parameter in parameters.items()
    ]


def _param_default(param: list[dict[str, Any]]):
    if param['default'] is not inspect.Parameter.empty and param['default'] is not None:
        return param['default']
    if param['type'] in DEFAULT:
        return DEFAULT[param['type']]
    elif param['type'].__name__ == 'Annotated':
        return DEFAULT[param['type'].__args__[0].__name__]
    else:
        return None


def _command_callback(cli: str):
    for c in app.registered_commands:
        if c.callback.__name__ == cli and not _ignore(c.callback.__name__):
            return c.callback
    return None


def _save(config, config_path=CONFIG_PATH):
    config_path.write_text(toml.dumps(config))


def _fcli(cli: str, color: bool = True):
    if color:
        return f"{red('[')}{italic(cli)}{red(']')}"
    else:
        return f'[{cli}]'


def _fconfig(config: dict[str, Any]):
    for k, v in config.items():
        config[k] = f'{v!r}'


def _config(cli: str | None):
    c = get_config() or {}
    if not cli:
        _cli = {}
        for k, v in c.items():
            _fconfig(v)
            _cli[str(_fcli(k))] = v
        return _cli
    if cli not in c:
        return {'error': red(f"Config({cli}) is not found.")}
    _fconfig(c[cli])
    return c[cli]


def _init(cli: str | None):
    c = get_config() or {}

    if not cli:
        for command in app.registered_commands:
            funcname = command.callback.__name__
            if funcname in c or _ignore(funcname):
                continue
            c[funcname] = {}
            for p in _params(command.callback):
                c[funcname][p['name']] = _param_default(p)
    else:
        if cli in c:
            return {'error': red(f"Config({cli}) already exists.")}

        if _ignore(cli):
            return {'error': red(f"Config({cli}) is not supported.")}

        _cli = {}
        callback = _command_callback(cli)
        if callback is None:
            return {'error': red(f"Command({cli}) is not found.")}

        for p in _params(callback):
            _cli[p['name']] = _param_default(p)

        c[cli] = _cli

    _save(c)
    return _config(cli)


@app.command()
def config(
    cli: Annotated[
        str,
        typer.Argument(
            show_default=False,
            help="Show config of specified cli.",
        ),
    ] = None,
    init: Annotated[
        bool,
        typer.Option(
            '-i',
            '--init',
            show_default=False,
            help="Initialize config file.",
        ),
    ] = False,
):
    if init:
        log_run(
            lambda: _init(cli),
            cli='config',
            result_title='Init' +
                (_fcli(f'{cli}', False) if cli is not None else '')
        )
    else:
        log_run(
            lambda: _config(cli),
            cli='config',
            result_title='Config' if cli is None else _fcli(cli, False),
        )
