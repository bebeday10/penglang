from dataclasses import dataclass
from typing import TYPE_CHECKING
from .. import pengrandom as pr

if TYPE_CHECKING:
    from .pengantmachine import PenguinAntMachine
    from .pengantplace import PenguinAntPlace
    from .pengant import PenguinAnt

@dataclass
class PenguinAntEnemy:
    colony: "PenguinAntMachine"
    name: str = "Enemy"
    offense: int = 1
    defense: int = 1
    location: "PenguinAntPlace | None" = None
    hp: int = 10

    def __post_init__(self):
        self.doings = {
            "confusion": 20,
            "nothing": 50,
            "head to location": 30,
            "fight": 60,
            "mitosis": 13
        }
        self.base_hp = self.hp

    def turn(self):
        do = self.choose_what_to_do()

        if do == "confusion":
            return f"Enemy {self.name} is confused"
        elif do == "head to location":
            self.location = pr.random_decision(*self.colony.locations)

            return f"Enemy {self.name} is now at {self.location.name}"

        elif do == "fight":
            ants = self.find_ants_here()

            if ants:
                to_fight: "PenguinAnt" = pr.random_decision(*ants)
                hp_burn = self.offense - to_fight.defense + pr.random_decimal(-2, 2)
                to_fight.hp -= hp_burn
                if to_fight.hp <= 0:
                    self.colony.ants.remove(to_fight)
                    return f"Enemy {self.name} fought Ant {to_fight.name} dealing {hp_burn} HP and Ant {to_fight.name} now has {to_fight.hp} HP which means they're dead"
                
                return f"Enemy {self.name} fought Ant {to_fight.name} dealing {hp_burn} HP and Ant {to_fight.name} now has {to_fight.hp} HP"

            else:
                return f"Enemy {self.name} tried to fight but no ant was at {self.location.name}"
            
        elif do == "mitosis":
            self.colony.enemies.append(PenguinAntEnemy(self.colony, f"{self.name}", offense=self.offense + pr.random_decimal(-0.5, 0.5), defense=self.defense + pr.random_decimal(-0.5, 0.5), hp=self.base_hp + pr.random_decimal(-5, 5), location=self.location))


            return f"Enemy {self.name} has mitosis'd Enemy {self.name} which has {self.colony.enemies[-1].defense} defense {self.colony.enemies[-1].offense} offense and {self.colony.enemies[-1].hp} HP"

                

        return ""

    def choose_what_to_do(self):
        return "".join(pr.random_decisions(**self.doings))

    def find_ants_here(self):
        return [ant for ant in self.colony.ants if ant.location.name == self.location.name]