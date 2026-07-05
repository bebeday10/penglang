from .. import penglang as pl
from typing import Callable

def penguin_is_it(*cases: tuple[bool, Callable], otherwise: Callable | None = None):
    """
    the way for penguins to check if something is then do something

    Args:
        *cases (tuple[bool, Callable]): the cases for the command to check
        otherwise (Callable | None, optional): if none of the cases are correct, run this. Defaults to None.

    Returns:
        bool: get the answer

    Examples:
        >>> penguin = 5
        >>> banana = 2
        >>> pyn.penguin_is_it(
                (pyn.penguin_check(
                    penguin,
                    banana,
                    "more"
                ),
                lambda: pl.say("hello"), lambda: pl.say("thanks")),(
                    pyn.penguin_check(
                        banana,
                        penguin,
                        "less"
                    ),
                    lambda: pl.say("banana eat"),
                    lambda: pl.say("dance")
                ), otherwise= pl.say("no")
                )
        hello
        thanks
    """
    for case, *actions in cases:
        for action in actions:
            if case:
                if action is None:
                    pass
                else:
                    action()
                    
        else:
            if case:
                return True
            
    else:
        if otherwise is None:
            return False
        else:
            otherwise()
            return False
        
def penguin_check(a, b, mode: str):
    """
    check if it happens and get the answers

    Args:
        a (Any): the base
        b (Any): the condition
        mode (str): the way to check

    Modes:
        "same": check if it is the same.
        "not same": check if it is not the same.
        "more": check if it is more.
        "more or same": check if it more or the same.
        "less": check if it is less.
        "less or same": check if it is less or the same.
        "in": check if it is inside.
        "is": check if it is.

    Returns:
        bool: the answer
    """
    if mode == "same": return a == b
    if mode == "not same": return a != b
    if mode == "more": return a > b
    if mode == "more or same": return a >= b
    if mode == "less": return a < b
    if mode == "less or same": return a <= b
    if mode == "in": return a in b
    if mode == "is": return a is b
