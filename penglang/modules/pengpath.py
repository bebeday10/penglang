"""
# PengPath

PengPath: pathway to anywhere

Features:
    set root
    filp pages
"""

from pathlib import Path

ROOT = None

def set_root(path):
    """
    the hardcover.

    Args:
        path (str): the hardcover area.
    """
    global ROOT
    ROOT = path
    ROOT = Path(ROOT)

def page(*parts, start: Path = ROOT) -> Path:
    """
    flip some pages.

    Args:
        start (Path, optional): the starting line. Defaults to ROOT.

    Returns:
        Path: the page you land on
    """
    return start.joinpath(*parts)

