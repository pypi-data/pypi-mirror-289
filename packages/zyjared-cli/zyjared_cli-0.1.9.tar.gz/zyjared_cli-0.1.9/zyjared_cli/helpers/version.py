from pathlib import Path
from typing import Literal
import toml

_MODE = Literal['major', 'minor', 'patch', ]
_PREMODE = Literal['alpha', 'beta', 'rc', 'dev']
_INDEX = Literal[0, 1, 2, 4]

PYPROJECT_PATH = Path('pyproject.toml')
PRE_MODE = ['alpha', 'beta', 'rc', 'dev']
MODE = ['major', 'minor', 'patch']


def _read(p=PYPROJECT_PATH):
    return toml.loads(p.read_text())


def _write(config, p=PYPROJECT_PATH):
    p.write_text(toml.dumps(config))


def load_version(v: str | list):
    if isinstance(v, list):
        return v

    ls = v.split('.')
    if '-' in ls[2]:
        _ls = ls[2].split('-')
        ls[2] = _ls[0]
        ls.insert(3, _ls[1])

    return ls


def dump_version(v: str | list):
    if isinstance(v, str):
        return v

    if len(v) < 4:
        return '.'.join(v)

    return '.'.join(v[:3]) + '-' + '.'.join(v[3:])


def _update_version(v: str | list, *, index: _INDEX, down: bool = False):
    _version: list[str] = load_version(v)
    if down:
        if _version[index] == '0':
            raise ValueError(f'Can not down {index} in {v}.')
        _version[index] = str(int(_version[index]) - 1)
    else:
        _version[index] = str(int(_version[index]) + 1)
    return _version


def _up(v: str | list, index: _INDEX):
    return _update_version(v, index=index)


def _down(v: str | list, index: _INDEX):
    return _update_version(v, index=index, down=True)


def version(*, return_str: bool = False, config: dict = None):
    config = _read() if config is None else config
    v: str = config['tool']['poetry']['version']
    if return_str:
        return v
    return load_version(v)


def save_version(v: str | list, *, config: dict = None):
    config = _read() if config is None else config
    config['tool']['poetry']['version'] = dump_version(v)
    _write(config)


def mode_version(mode: _MODE, *, down: bool = False, save: bool = False):
    index = MODE.index(mode)
    config = _read()
    _old: list = version(config=config)
    v: list = [i for i in _old]
    if len(v) < 4:
        if down:
            v = _down(v, index=index)
        else:
            v = _up(v, index=index)
    else:
        v = v[:3]
    if save:
        save_version(v, config=config)

    return {
        "old": _old,
        "now": v,
    }


def pre_version(pre_mode: _PREMODE, *, down: bool = False, save: bool = False):
    config = _read()
    _old: list = version(config=config)
    v: list = [i for i in _old]
    if len(v) < 4:
        v.extend([pre_mode, '1'])
    elif v[3] != pre_mode:
        v[3] = pre_mode
        v[4] = '1'
    else:
        if down:
            v = _down(v, index=4)
            if v[4] == '0':
                v = v[:3]
        else:
            v = _up(v, index=4)
    if save:
        save_version(v, config=config)

    return {
        "old": _old,
        "now": v,
    }
