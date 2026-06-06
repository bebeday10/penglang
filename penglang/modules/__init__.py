# __init__.py file for the penglang_language.modules package

__version__ = "0.1.0"

from .pengmath import *
from .pengwindow import *

SHOWLOGS = False

if SHOWLOGS:
    print(f"Loaded penglang_language.modules with version {__version__}")