from typing import Literal
from zyjared_color import Color, cyan, italic
import time

__all__ = [
    'log',
    'alog',
    'log_run'
]

UNITS = ['s', 'ms', 'us', 'ns']
predot = Color(' · ').bold().cyan()


def _endow_unit(t: int, init_unit: Literal['s', 'ms', 'us', 'ns'] = 's', *, precision=2):
    i = UNITS.index(init_unit)

    for j in range(i, len(UNITS)):
        if t >= 1:
            break
        else:
            t = t * (1000 ** j)
            i = j

    if t > 1:
        msg = f'{round(t, precision)} {cyan(UNITS[i]).italic()}'
    else:
        msg = f'{italic('<1')} {cyan(UNITS[i])}'

    return {
        "time": t,
        "unit": UNITS[i],
        "msg": msg
    }


def measure_time(
        func,
        precision=2
):
    start = time.time()

    try:
        result = func()
        sucess = True
    except Exception as e:
        result = str(e)
        sucess = False

    end = time.time()

    endowed = _endow_unit(end - start, precision=precision)

    return {
        "sucess": sucess,
        "time": endowed['msg'],
        "result": result,
    }


def _log_list(ls: list, preblank: int = 2, prefix: Color = predot):
    if len(ls) == 0:
        print(f'{prefix.yellow():>{preblank}}{italic("Empty").yellow()}')
    for item in ls:
        print(f'{prefix:>{preblank}}{item}')


def _log_dict(d: dict, preblank: int = 2, prefix=predot):
    length = max([len(k) for k in d.keys()])
    for k, v in d.items():
        print(f'{" " * preblank}{Color(k).cyan():<{length}}: ', end='')
        if isinstance(v, list):
            print()
            _log_list(v, preblank + 4, prefix)
        elif isinstance(v, dict):
            print()
            _log(v, preblank + 2, prefix)
        else:
            print(v)


def _log(text: str | list | dict | Color, preblank: int = 2, prefix=predot):
    if isinstance(text, list):
        _log_list(text, preblank, prefix)
    elif isinstance(text, dict):
        _log_dict(text, preblank, prefix)
    else:
        print(text)


def _log_title(cli: str, status: Literal['success', 'fail', 'warning'] | str):
    pkgname = Color(' ZYCLI ').white().bold().bg_blue()
    cliname = Color(f' {cli} ').blue().bold().bg_white()
    _status = Color(f' {status.upper()} ').bold()
    if status == 'success':
        _status.green()
    elif status == 'fail':
        cliname.bg_red()
        _status.red()
    else:
        _status.yellow()

    print(f'\n{pkgname}{cliname}{_status} ')


def alog(
    cli: str,
    status: Literal['success', 'fail', 'warning'] | str,
    *args,
    **kwargs
):
    _log_title(cli, status)

    if args:
        _log_list(args, preblank=2, prefix=predot)
    if kwargs:
        _log(kwargs, preblank=2, prefix=predot)


def log(
    status: Literal['success', 'fail', 'warning'] | str,
    cli: str = "tool",
    log_list: list = [],
    log_dict: dict = {},
):
    _log_title(cli, status)

    if log_list:
        _log_list(log_list, preblank=4, prefix=predot)
    if log_dict:
        _log(log_dict, preblank=2, prefix=predot)


def log_run(func, *, precision=2, cli="tool", result_title="Result"):
    result = measure_time(func, precision)
    status = 'success'
    if not result['sucess'] or (isinstance(result['result'], dict) and 'error' in result['result']):
        status = 'fail'

    log(
        status=status,
        cli=cli,
        log_dict={
            'Time': result['time'],
            result_title: result['result'],
        }
    )
