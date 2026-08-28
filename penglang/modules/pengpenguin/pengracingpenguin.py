from .pengpenguin import Penguin
from ... import penglang as pl
from .. import pengrandom as pr

class RacingPenguin(Penguin):
    power: int
    wit: int
    stamina: int
    guts: int

    def speed_training(self):
        self.speed += pr.random_number(5, 15)
        self.power += pr.random_number(1, 3)

    def power_training(self):
        self.power += pr.random_number(5, 15)
        self.stamina += pr.random_number(1, 3)

    def stamina_training(self):
        self.stamina += pr.random_number(5, 15)
        self.guts += pr.random_number(1, 3)

    def guts_training(self):
        self.guts += pr.random_number(5, 15)
        self.stamina += pr.random_number(2, 5)

    def wit_training(self):
        self.wit += pr.random_number(5, 15)
        self.power += pr.random_number(3, 5)
        self.speed += pr.random_number(2, 4)