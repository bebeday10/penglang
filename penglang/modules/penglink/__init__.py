# __init__.py for penglink

__version__ = "0.4.0"

from .central import show_requests

SHOWLOGS = False

if SHOWLOGS:
    print(f"Loaded penglang_language.modules with version {__version__}")