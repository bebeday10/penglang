# __init__.py file for the penglang_language.modules package

__version__ = "0.5.0"

from . import (
    pengmath,
    pengimage,
    pengrandom,
    pengbanana,
    pengpenguin,
    pengcrowd,
    pengiterable,
    pengbulletin,
    pengcard,
    pengdecorator,
    pengvending,
    pengsymbol,
    pengcoffee,
    pengcursor,
    penglink,
    pengmoney,
    pengmustfollow,
    pengnote,
    pengpast,
    pengpath,
    pengprint,
    pengsong,
    pengstring,
    pengthing,
    pengthis,
    pengwindow,
    pengyesno
)
from .pengcounter import pengcounter


SHOWLOGS = False

if SHOWLOGS:
    print(f"Loaded penglang_language.modules with version {__version__}")