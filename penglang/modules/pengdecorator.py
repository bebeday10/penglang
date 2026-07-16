import asyncio as asy

from .. import penglang as pl
from functools import wraps

def penguin_deprecation(when_start: str, when_removed: str, replacement: str, func_name: str = "this penguin function"):
    """
    for deprecated functions, use when a function is going to get removed

    Args:
        when_start (str): when it started to be deprecated
        when_removed (str): when it is going to get removed
        replacement (str): a replacement for it
        func_name (str, optional): the function name. Defaults to "this penguin function".
    """
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            pl.say(f"{func_name} has been deprecated since {when_start}. it will be removed on {when_removed}. {replacement}")
            return func(*args, **kwargs)

        return inner
    return decorator

def keep_doing_it(times: int, log: bool = False):
    """
    keep doing a function

    Args:
        times (int): the amount of times
        log (bool, optional): whether to log or not. Defaults to False.
    """
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = ()
            for i in range(times):
                pl.say(f"this is the {i + 1} time!") if log else None
                result.append(func(*args, **kwargs))

            return result

        return inner
    return decorator


