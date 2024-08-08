from importlib.metadata import PackageNotFoundError, version

from .setup import setup, setup_oauth
from .ytmusic import YTMusic

__version__ = "0.2.6rc11.dev6"

__copyright__ = "Copyright 2024 jcbirdwell"
__license__ = "MIT"
__title__ = "moretunes.youtube"
__all__ = ["YTMusic", "setup_oauth", "setup"]
