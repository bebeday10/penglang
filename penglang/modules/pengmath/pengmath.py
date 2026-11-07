"""
# PengMath

PengMath: counting and more

- add
- subtract
- multiply
- divide
"""


# this is the math module for the penguin language, it has functions for addition, subtraction, multiplication, division, etc. that use penguin words instead of python keywords
from math import ceil, floor

from ... import penglang as peng

def penguin_add(a, b, *args, log: bool = False):
    """
    add something with addition

    Args:
        a (int): The first number to add.
        b (int): The second number to add.
        *args (int): Additional numbers to add.
        log (bool, optional): Whether to log the result. Defaults to False.

    Returns:
        int: The sum of the numbers.
    """
    total = a + b
    for num in args:
        total += num
    if log:
        peng.say(f"Sum: {total}")
    return total

def penguin_subtract(a, b, *args, log: bool = False):
    """
    subtract something with subtraction

    Args:
        a (int): The first number to subtract.
        b (int): The second number to subtract.
        *args (int): Additional numbers to subtract.
        log (bool, optional): Whether to log the result. Defaults to False.

    Returns:
        int: The difference of the numbers.
    """
    total = a - b
    for num in args:
        total -= num
    if log:
        peng.say(f"Difference: {total}")
    return total

def penguin_multiply(a, b, *args, log: bool = False):
    """
    multiply something with multiplication

    Args:
        a (int): The first number to multiply.
        b (int): The second number to multiply.
        *args (int): Additional numbers to multiply.
        log (bool, optional): Whether to log the result. Defaults to False.

    Returns:
        int: The product of the numbers.
    """
    total = a * b
    for num in args:
        total *= num
    if log:
        peng.say(f"Product: {total}")
    return total

def penguin_divide(a, b, *args, log: bool = False):
    """
    divide something with division

    Args:
        a (int): The first number to divide.
        b (int): The second number to divide.
        *args (int): Additional numbers to divide by.
        log (bool, optional): Whether to log the result. Defaults to False.

    Returns:
        float: The quotient of the numbers.
    """
    total = a / b
    for num in args:
        total /= num
    if log:
        peng.say(f"Quotient: {total}")
    return total

def penguin_floor_divide(a, b, *args, log: bool = False):
    """
    floor divide something with floor division

    Args:
        a (int): The first number to floor divide.
        b (int): The second number to floor divide.
        *args (int): Additional numbers to floor divide by.
        log (bool, optional): Whether to log the result. Defaults to False.

    Returns:
        int: The floor quotient of the numbers.
    """
    total = a // b
    for num in args:
        total //= num
    if log:
        peng.say(f"Floor quotient: {total}")
    return total

def penguin_modulo(a, b, *args, log: bool = False):
    """
    modulo something with modulo

    Args:
        a (int): The first number to modulo.
        b (int): The second number to modulo.
        *args (int): Additional numbers to modulo by.
        log (bool, optional): Whether to log the result. Defaults to False.

    Returns:
        float: The remainder of the numbers.
    """
    total = a % b
    for num in args:
        total %= num
    if log:
        peng.say(f"Remainder: {total}")
    return total

def penguin_exponentiation(a, b, *args, log: bool = False):
    """
    exponentiate something with exponentiation

    Args:
        a (int): The first number to exponentiate.
        b (int): The second number to exponentiate.
        *args (int): Additional numbers to exponentiate by.
        log (bool, optional): Whether to log the result. Defaults to False.

    Returns:
        float: The power of the numbers.
    """
    total = a ** b
    for num in args:
        total **= num
    if log:
        peng.say(f"Power: {total}")
    return total


def penguin_average(a, b, *args, log: bool = False):
    """
    average something with average

    Args:
        a (int): The first number to average.
        b (int): The second number to average.
        *args (int): Additional numbers to average by.
        log (bool, optional): Whether to log the result. Defaults to False.

    Returns:
        float: The average of the numbers.
    """
    total = a + b
    for num in args:
        total += num
    total /= (2 + len(args))
    if log:
        peng.say(f"Average: {total}")
    return total


def penguin_median(a, b, *args, log: bool = False):
    """
    median something with median

    Args:
        a (int): The first number to median.
        b (int): The second number to median.
        *args (int): Additional numbers to median by.
        log (bool, optional): Whether to log the result. Defaults to False.

    Returns:
        float: The median of the numbers.
    """
    to_medianize = [a, b, *args]
    median = len(to_medianize) / 2
    if len(to_medianize) % 2 == 0:
        total = (to_medianize[ceil(median)] + to_medianize[floor(median)]) / 2
    else:
        total = to_medianize[round(median)]


    if log:
        peng.say(f"Median: {total}")
    return total

def penguin_mode(a, b, *args, log: bool = False):
    """
    mode something with mode

    Args:
        a (int): The first number to mode.
        b (int): The second number to mode.
        *args (int): Additional numbers to mode by.
        log (bool, optional): Whether to log the result. Defaults to False.

    Returns:
        float: The mode of the numbers.
    """
    to_mode = [a, b, *args]
    count: dict[float | int, int] = {}
    for i in to_mode:
        count[i] = count.get(i, 0) + 1
    total = max(count.values())
    total = [key for key, val in count.items() if val == total]


    if log:
        peng.say(f"Mode: {", ".join(total)}")
    return total