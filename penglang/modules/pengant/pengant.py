from dataclasses import dataclass
from .. import pengrandom as pr
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pengantmachine import PenguinAntMachine
    from .pengantplace import PenguinAntPlace

@dataclass
class PenguinAnt:
    colony: "PenguinAntMachine"
    name: str = "Ant"
    location: "PenguinAntPlace | None" = None
    offense: int = 1
    defense: int = 1

    def __post_init__(self):
        self.doings = {
            "head to location": 30,
            "mitosis": 10,
            "nothing": 50,
            "confusion": 20

        }
        self.location = self.colony.locations[0]
    def turn(self):
        do = self.choose_what_to_do()
        
        if do == "head to location":
            self.location = pr.random_decision(*self.colony.locations)

            return f"Ant {self.name} is now at {self.location.name}"
        elif do == "mitosis":
            self.colony.ants.append(PenguinAnt(self.colony, f"#{self.colony.current_ant}"))
            temp_current = self.colony.current_ant
            self.colony.current_ant += 1

            return f"Ant {self.name} has mitosis'd Ant #{temp_current}"

        elif do == "confusion":
            return f"Ant {self.name} is confused"
        
        return ""

    def choose_what_to_do(self):
        return "".join(pr.random_decisions(**self.doings))