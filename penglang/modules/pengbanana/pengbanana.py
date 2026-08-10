
from dataclasses import dataclass
from ... import penglang as pl

@dataclass
class PenguinBanana:
    name: str
    size: float
    weight: float
    freshness: int
    potassium: float
    species: str
    peeled: bool = False
    eaten: bool = False
    def peel(self, log: bool = False):
        if self.eaten:
            pl.say("the banana is already eaten!") if log else None
            return "Can't peel an eaten banana."
        self.peeled = True

    def eat(self, log: bool = True):
        if not self.peeled:
            pl.say("it is not peeled!") if log else None
            return "unpeeled"

        self.eaten = True

    def throw(self, log: bool = True):
        if not self.eaten:
            pl.say("the banana is not eaten!")
            return "eat it"

    def get_potassium(self):
        return self.potassium

    def potassium_to_freshness_ratio(self):
        return self.potassium / self.freshness

    def bmi(self):
        return self.weight / (self.size**2)

    def get_weight_category(self):
        bmi = self.bmi()
        if bmi <= 1:
            return "tiny banana"
        elif bmi <= 3:
            return "normal banana"
        elif bmi <= 5:
            return "big banana"
        else:
            return "chonky banana"

    def quality_ratio(self):
        (self.potassium * self.freshness) / (self.bmi() * 50)

        

        