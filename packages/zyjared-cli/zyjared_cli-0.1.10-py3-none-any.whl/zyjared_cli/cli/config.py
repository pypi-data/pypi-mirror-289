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


IGNORES = [
    'config',
    'push'
]


DEFAULT = {
    'str': '',
    'list': [],
    'List': [],
    'dict': {},
    'Dict': {},
}


def _ignore(cli: str, *, group: str = None):
    if group:
        return group in IGNORES
    return cli in IGNORES


def _typer_group(group: str):
    for g in app.registered_groups:
        if g.name == group:
            return g.typer_instance
    return None


def _typer_instance_command(instance: typer.Typer, command_name: str):
    for c in instance.registered_commands:
        if c.callback.__name__ == command_name:
            return c
    # for c in instance.registered_groups:
    #     _info = _typer_instance_command(c.typer_instance, command_name)
    #     if _info:
    #         return _info
    return None


def _tyepr_command(cli: str, *, group: str = None):
    if group:
        ins = _typer_group(group)
        if ins:
            return _typer_instance_command(ins, cli)
    return _typer_instance_command(app, cli)


def _func_params(func):
    signature = inspect.signature(func)
    parameters = signature.parameters
    return [
        {
            'name': name,
            'type': parameter.annotation,
            'default': parameter.default
        } for name, parameter in parameters.items()
    ]


def _func_param_default(param: list[dict[str, Any]]):
    if param['default'] is not inspect.Parameter.empty and param['default'] is not None:
        return param['default']
    if param['type'] in DEFAULT:
        return DEFAULT[param['type']]
    elif param['type'].__name__ == 'Annotated':
        _cname = param['type'].__args__[0].__name__
        if _cname in DEFAULT:
            return DEFAULT[_cname]
        else:
            return None
    else:
        return None


def _func_params_values(func):
    dic = {}
    for p in _func_params(func):
        dic[p['name']] = _func_param_default(p)
    return dic


def _save(config, config_path=CONFIG_PATH):
    config_path.write_text(toml.dumps(config))


def _fcli(cli: str, *, color=True, group: str = None):
    text = f'{group}.{cli}' if group else cli
    if color:
        return f"{red('[')}{italic(text)}{red(']')}"
    else:
        return f'[{text}]'


def get_command_info(cli: str, *, group: str = None):
    if _ignore(cli, group=group):
        return None
    return _tyepr_command(cli, group=group)


def get_command_config(cli: str, *, group: str = None):
    command = get_command_info(cli, group=group)
    if not command:
        return None
    return _func_params_values(command.callback)


def get_typer_instance_config(instance: typer.Typer, *, cover_config: dict = None):
    dic = cover_config or {}
    for c in instance.registered_commands:
        if c.callback.__name__ in dic:
            continue
        dic[c.callback.__name__] = _func_params_values(c.callback)
    return dic


def _formate_config(config: dict[str, Any], *, group: str = None):
    _cli = {}
    for k, v in config.items():
        _cli[str(_fcli(k, group=group))] = v
    return _cli


def _config(cli: str | None, *, group: str = None):
    """
    获取配置项
    """
    c = get_config() or {}
    if not group and not cli:
        return _formate_config(c)
    elif group and not cli:
        if group in c:
            return _formate_config(c[group], group=group)
        else:
            return {'error': red(f"Config [group: {group}] is not found.")}
    elif group:
        if group in c and cli in c[group]:
            return c[group][cli]
        else:
            return {'error': red(f"Config[{group}.{cli}] is not found.")}
    else:
        if cli in c:
            return c[cli]
        else:
            return {'error': red(f"Config[{cli}] is not found.")}


def _init(cli: str | None, *, group: str = None):
    c = get_config() or {}

    if not group and not cli:
        c = get_typer_instance_config(app, cover_config=c)
    elif group and not cli:
        for g in app.registered_groups:
            if g.name == group:
                c[group] = get_typer_instance_config(
                    g.typer_instance, cover_config=c.get(group, {})
                )
    elif group:
        if group not in c and cli in c[group]:
            return {'error': red(f"Config[{group}.{cli}] already exists.")}

        _dic = get_command_config(cli, group=group)
        if _dic is None:
            return {'error': f'Command[{group}.{cli}] is not found.'}

        if group in c:
            c[group][cli] = _dic
        else:
            c[group] = {cli: _dic}

    elif cli:
        if cli in c:
            return {'error': red(f"Config[{cli}] already exists.")}

        _dic = get_command_config(cli)
        if _dic is None:
            return {'error': f'Command[{cli}] is not found.'}

        c[cli] = _dic

    _save(c)

    return _config(cli, group=group)  # 重新获得配置


def _split_cli(cli: str | None):
    if cli is None:
        return None, None
    # if cli.endswith('.'):
    #     return cli[:-1], None
    if '.' in cli:
        return tuple(cli.split('.', 1))
    return None, cli


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
    """
    Show config of specified cli. And it can also be used to initialize config file.

    Example:

        $ zycli config

        $ zycli config --init

        $ zycli config clean

        $ zycli config clean --init
    """
    [group, cli] = _split_cli(cli)
    if init:
        log_run(
            lambda: _init(cli, group=group),
            cli='config',
            result_title='Init' +
                (_fcli(f'{cli}', group=group, color=False)
                 if cli is not None else '')
        )
    else:
        log_run(
            lambda: _config(cli, group=group),
            cli='config',
            result_title='Config' if cli is None else _fcli(
                cli, group=group, color=False),
        )
