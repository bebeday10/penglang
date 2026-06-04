# this is the math module for the penguin language, it has functions for addition, subtraction, multiplication, division, etc. that use penguin words instead of python keywords
from .. import penglang as peng

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

