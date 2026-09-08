from . import PenguinCounter
from dataclasses import dataclass

@dataclass
class PenguinTitleCounter(PenguinCounter):
    title: str

    def change_title(self, new_title: str):
        self.title = new_title

    def __str__(self):
        return f"{self.title}: {self.count}"