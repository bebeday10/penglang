__version__ = "0.8.0"

from .penglang import *
from .modules import pengwindow, pengmath

SHOW_LOGS = False

if SHOW_LOGS:
    print(f"PengLang initialized, version {__version__}")
