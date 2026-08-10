from dataclasses import dataclass

@dataclass
class PenguinCrowd:
    penguins: int = 0
    def throw_penguins(self, amount: int):
        self.penguins = max(self.penguins - amount, 0)
    def receive_penguins(self, amount: int):
        self.penguins += amount
    def get_penguins(self) -> int:
        return self.penguins