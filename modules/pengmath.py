# this is the math module for the penguin language, it has functions for addition, subtraction, multiplication, division, etc. that use penguin words instead of python keywords
import penglang_language.penglang as peng

def penguin_add(a, b, *args, log: bool = False):
    total = a + b
    for num in args:
        total += num
    if log:
        peng.say(f"Sum: {total}")
    return total

def penguin_subtract(a, b, *args, log: bool = False):
    total = a - b
    for num in args:
        total -= num
    if log:
        peng.say(f"Difference: {total}")
    return total

def penguin_multiply(a, b, *args, log: bool = False):
    total = a * b
    for num in args:
        total *= num
    if log:
        peng.say(f"Product: {total}")
    return total

def penguin_divide(a, b, *args, log: bool = False):
    total = a / b
    for num in args:
        total /= num
    if log:
        peng.say(f"Quotient: {total}")
    return total

