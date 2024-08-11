from pathlib import Path
import toml

__all__ = [
    'get_config',
    'resolve_config',
    'CONFIG_PATH',
]

CONFIG_PATH = Path.cwd() / 'zycli.toml'


def get_config(config_path=CONFIG_PATH, cli: str = None )-> None | dict:
    if not config_path.exists():
        return None

    toml_string = config_path.read_text()
    config = toml.loads(toml_string)

    return config[cli] if cli else config


def resolve_config(cli: str = None, config_path=CONFIG_PATH, **kwargs):
    """
    获取指定路径配置的 `cli` 项, 可传入默认值 `**kwargs`。
    """
    config = get_config(config_path, cli) or {}
    return {**kwargs, **config}
