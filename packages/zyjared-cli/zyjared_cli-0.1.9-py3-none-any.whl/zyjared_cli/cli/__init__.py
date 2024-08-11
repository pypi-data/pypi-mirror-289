from .app import app
from .clean import clean  # noqa: F401
from .config import config  # noqa: F401

from .version import app as app_version


__all__ = [
    'app',
]


app.add_typer(app_version, name='version')
