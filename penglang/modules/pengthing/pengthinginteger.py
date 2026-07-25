from typing import SupportsIndex
from typing_extensions import Self

from ... import penglang as pl

class PenguinInteger(int):
    def __new__(cls, x: str | bytes | bytearray, /, base: SupportsIndex) -> Self:
        return super().__new__(x, base)
    
    def count_fish(self):
        return f"after a hard work, found {self} fish"

    def is_penguin_number(self):
        return self % 2 == 0
    
