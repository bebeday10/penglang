"""
# PengThing

*PengThing*, make things.
"""

from typing import Callable


def make_thing(name, bases=(), things_it_has: list =None, things_it_can_do=None) -> type:
    """
    make a thing.

    Args:
        name (str): the name of the thing.
        bases (tuple, optional): the bases. Defaults to ().
        things_it_has (list, optional): the things it has. Defaults to None.
        things_it_can_do (dict, optional): the things it can do. Defaults to None.

    Returns:
        type: the thing
    """
    attrs = things_it_has or []
    methods = things_it_can_do or {}

    namespace = {
        "__init__": start_maker(things=attrs),
        "show": show_maker(things=attrs),
        "__repr__": show_maker(things=attrs),
        "__add__": lambda self, other: self.__class__.__name__ + "-" + other.__class__.__name__
    }
    namespace.update(methods)
    

    
    return type(name, bases, namespace)

def start_maker(things) -> Callable[..., None]:
    """
    a start maker, used when a thing is made.

    Args:
        things (Any): the things that will be made.

    Returns:
        Callable[..., None]: the starter.
    """
    def __init__(self, *values):
        for name, value in zip(things, values):
            setattr(self, name, value)

    return __init__

def show_maker(things) -> Callable[..., str]:
    """
    a show maker, used when things are printed.

    Args:
        things (_type_): the things that will show.

    Returns:
        Callable[..., str]: the show.
    """
    def show(self):
        parts = []
        for t in things:
            parts.append(f"{t}={getattr(self, t)}")
        return f"<{self.__class__.__name__} " + ", ".join(parts) + ">"
    
    return show