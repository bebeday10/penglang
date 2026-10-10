
import pytest

from penglang.modules.pengmath import (
    penguin_add,
    penguin_subtract,
    penguin_multiply,
    penguin_divide,
)


def test_add():
    assert penguin_add(2, 3) == 5


def test_add_multiple_numbers():
    assert penguin_add(1, 2, 3, 4) == 10


def test_subtract():
    assert penguin_subtract(10, 3) == 7


def test_subtract_multiple_numbers():
    assert penguin_subtract(20, 3, 2) == 15


def test_multiply():
    assert penguin_multiply(4, 5) == 20


def test_multiply_multiple_numbers():
    assert penguin_multiply(2, 3, 4) == 24


def test_divide():
    assert penguin_divide(20, 4) == 5


def test_divide_multiple_numbers():
    assert penguin_divide(120, 3, 4) == 10


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        penguin_divide(10, 0)
