"""
# PengRandom

PengRandom: the possibilities are too many penguins

# Features:
    - random numbers
    - random decimals
    - random decision
    - random range
    - random decisions
"""

from ... import penglang
import random as r

def random_number(start: int, end: int) -> int:
    """
    make a random number.

    Args:
        start (int): starting number
        end (int): ending number

    Returns:
        int: the random number
    """
    return r.randint(start, end)

def random_decimal(start: float, end: float) -> float:
    """
    make a random number with a decimal.

    Args:
        a (float): the starting number
        b (float): the ending number

    Returns:
        float: the random number with a decimal
    """
    return r.uniform(start, end)

def random_decision(*options):
    """
    make a random decision. choose a random decision from a list of decisions.
    Args:
        *options (Any): the options.
    Returns:
        Any: the decision
    """
    return r.choice([i for i in options])

def random_range(start: int = 0, stop: int = 1, step: int = 1) -> int:
    """
    generate a random number based on a range between a start and stop. ends at the number below stop, and inclusive of start.  
    functionally the same as `random_decision(range(start, stop, step))`.
    Args:
        start (int): the start number, inclusive. Defaults to 0.
        stop (int): the end number, exclusive. Defaults to 1.
        step (int): the step. Defaults to 1.

    Returns:
        int: the 
    """
    return r.randrange(start, stop, step)

def random_decisions(*_, times=1, **options) -> list:
    """
    make random decisions.  
    an advanced `random_decision`.  

    Args:
        **options (Any): the options. key is option, value is probability
        times (int, optional): the amount of times it will decide. Defaults to 1.

    Returns:
        list: the decisions made.
    """
    items: list = list(options.keys())
    weights: list = list(options.values())

    return r.choices(items, weights, k=times)