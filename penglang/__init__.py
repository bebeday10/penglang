__version__ = "1.2.0"

from .penglang import *
from . import modules

SHOW_LOGS = False

if SHOW_LOGS:
    print(f"PengLang initialized, version {__version__}")
