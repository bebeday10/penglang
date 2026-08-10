from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import pengbanana as pb

@dataclass
class PenguinBananaBag:
    bananas: list["pb.PenguinBanana"] | None = None
    def __post_init__(self):
        if self.bananas == None:
            self.bananas = []

    def add_banana(self, banana: "pb.PenguinBanana"):
        self.bananas.append(banana)

    def remove_banana(self, banana: int):
        self.bananas.pop(banana)

    def count(self):
        return len(self.bananas)

    def has_banana(self, banana: "pb.PenguinBanana"):
        return banana in self.bananas

    def get_bananas(self):
        return self.bananas

    def reverse_bananas(self):
        self.bananas = self.bananas[::-1]

    def get_banana(self, banana: int = 0):
        try:
            return self.bananas[banana]
        except IndexError:
            return None