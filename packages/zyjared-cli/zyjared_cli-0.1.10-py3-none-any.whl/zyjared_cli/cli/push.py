from typing import Annotated
import typer
from .app import app
from ..helpers.version import dump_version, handle_version, compare_version, version
from enum import Enum
import subprocess
from ..helpers.log import log, log_title
from zyjared_color import bold
import sys


class _V(str, Enum):
    patch = 'patch'
    minor = 'minor'
    major = 'major'
    alpha = 'alpha'
    beta = 'beta'
    rc = 'rc'
    dev = 'dev'


def _log(cmd: str, output: str):
    sys.stdout.write(f'  {bold(">").green()} {cmd}\n')
    sys.stdout.write(f'  {bold(".").red()}{output}\n')
    sys.stdout.flush()


def _subsystem(cmd: str, *, log=False):
    try:
        result = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        if log:
            _log(cmd, result)
        return result
    except subprocess.CalledProcessError as e:
        raise Exception(f'command error: {cmd}\nError message: {e.output}')


def _system(log=False, *args):
    for arg in args:
        _subsystem(arg, log=log)
    return list(args)


def _version(tag: _V, *, down=False):
    return handle_version(mode=tag.value, down=down, save=True)


def _push(message: str, *, amend=False, tag=False, retag=False, _echo=False):
    result = {}

    v = version(return_str=True)

    if retag:
        _system(
            _echo,
            f'git tag -d v{v}',
            f'git push origin -d v{v}',
        )

    if tag:
        up = _version(tag)
        v = dump_version(up['now'])
        result["tag"] = compare_version(old=up['old'], now=up['now'])

    _system(
        _echo,
        'git add .',
        f'git commit{"" if not amend else " --amend"} -m "{message}"',
        f'git push origin main{"" if not amend else " --force"}',
    )

    if tag or retag:
        _system(
            _echo,
            f'git tag v{v}',
            f'git push origin v{v}',
        )

    result['version'] = v

    return result


@app.command()
def push(
    message: Annotated[
        str,
        typer.Option(
            "-m",
            "--message",
            show_default=False,
            help="Specify the commit message.",
        ),
    ],
    amend: Annotated[
        bool,
        typer.Option(
            "--amend",
            show_default=False,
            help="Amend the commit.",
        )
    ] = False,
    tag: Annotated[
        _V,
        typer.Option(
            "--tag",
            show_default=False,
            help="Push the latest tag.",
        )
    ] = None,
    retag: Annotated[
        bool,
        typer.Option(
            "--retag",
            show_default=False,
            help="Retag the latest tag.",
        )
    ] = False,
    silent: Annotated[
        bool,
        typer.Option(
            "--silent",
            show_default=False,
            help="Show the command.",
        )
    ] = False,
):
    """
    Push to the repo.
    """
    log_title(cli='push')
    try:
        result = _push(message, amend=amend, tag=tag,
                       retag=retag, _echo=False if silent else True)
        status = bold('SUCCESS').green()
    except Exception as e:
        result = {'error': str(e)}
        status = bold('FAIL').red()
    finally:
        log(
            log_dict={
                'Status': status,
                'Result': result
            },
            show_title=False
        )
