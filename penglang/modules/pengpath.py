from pathlib import Path

ROOT = None

def set_root(path):
    global ROOT
    ROOT = path
    ROOT = Path(ROOT)

def page(*parts):
    return ROOT.joinpath(*parts)

