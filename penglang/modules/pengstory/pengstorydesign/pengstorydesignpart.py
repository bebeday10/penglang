from dataclasses import dataclass
from typing import Callable, TypeAlias
from . import pengstorydesignerror as psde

Choices: TypeAlias = dict[str, "Choices" | Callable]
@dataclass
class PenguinIceOfStoryDecisionsPart:
    name: str
    choices: Choices | None = None

    def __post_init__(self):
        self.choices = self.choices or {}

    def rename(self, new: str):
        self.name = new

    def add_choice(self, choice_name: str, choice_action: Choices | Callable):
        if choice_name == "name":
            raise psde.PenguinChoiceReservedError("Choice name is the same as \"name\", which is reserved by the decision's name. Please do not try to go into the source code and edit the name of what the decision name uses, please.")

        self.choices[choice_name] = choice_action