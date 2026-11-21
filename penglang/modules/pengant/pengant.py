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
    offense: int = 5
    defense: int = 5
    hp: int = 10

    def __post_init__(self):
        self.doings = {
            "head to location": 30,
            "mitosis": 10,
            "nothing": 50,
            "confusion": 20,
            "fight": 25

        }
        self.location = self.colony.locations[0]
        self.base_hp = self.hp
    def turn(self):
        do = self.choose_what_to_do()
        
        if do == "head to location":
            self.location = pr.random_decision(*self.colony.locations)

            return f"Ant {self.name} is now at {self.location.name}"
        elif do == "mitosis":
            self.colony.ants.append(PenguinAnt(self.colony, f"#{self.colony.current_ant}", offense=self.offense + pr.random_decimal(-0.5, 0.5), defense=self.defense + pr.random_decimal(-0.5, 0.5), hp=self.base_hp + pr.random_decimal(-5, 5)))
            temp_current = self.colony.current_ant
            self.colony.current_ant += 1

            return f"Ant {self.name} has mitosis'd Ant #{temp_current} which has {self.colony.ants[-1].defense} defense {self.colony.ants[-1].offense} offense and {self.colony.ants[-1].hp} HP"

        elif do == "confusion":
            return f"Ant {self.name} is confused"

        elif do == "fight":
            enemies = self.find_enemies_here()

            if enemies:
                to_fight: "PenguinAnt" = pr.random_decision(*enemies)
                hp_burn = self.offense - to_fight.defense + pr.random_decimal(-2, 2)
                to_fight.hp -= hp_burn
                if to_fight.hp <= 0:
                    self.colony.enemies.remove(to_fight)
                    return f"Ant {self.name} fought Enemy {to_fight.name} dealing {hp_burn} HP and Enemy {to_fight.name} now has {to_fight.hp} HP which means they're dead"
                
                return f"Ant {self.name} fought Enemy {to_fight.name} dealing {hp_burn} HP and Enemy {to_fight.name} now has {to_fight.hp} HP"

            else:
                return f"Ant {self.name} tried to fight but no enemy was at {self.location.name}"

        
        return ""

    def choose_what_to_do(self):
        return "".join(pr.random_decisions(**self.doings))

    def find_enemies_here(self):
        return [enemy for enemy in self.colony.enemies if enemy.location.name == self.location.name]