from dataclasses import dataclass
from ... import penglang as pl
from .. import pengbanana as pb
from .. import pengprint as pprint


@dataclass
class Penguin:
    """
    The awesome ***Penguin***.

    ## Has:
    - speed
    - weight
    - name
    - money
    - inventory
    - clothes
    - banana
        - banana as used in PengBanana.
    """
    speed: float
    weight: float
    name: str
    money: float
    inventory: dict | None = None
    clothes: dict | None = None
    banana: pb.PenguinBanana | None = None

    def __post_init__(self):
        self.inventory = self.inventory or {}
        self.clothes = self.clothes or {}
        self.banana = self.banana or pb.PenguinBanana("Banana", 1, 1, 1, 1, "Banana")

    def waddle(self, log: bool = False):
        """
        make your penguin do a fun waddle

        Args:
            log (bool, optional): SAY THE WADDLING. May scare penguins. Defaults to False.

        Returns:
            Literal['Penguin waddles.']: Penguin waddles.
        """
        pl.say("the penguin waddles...") if log else None
        return "Penguin waddles."

    def train(self, amount, log: bool = False):
        self.speed += amount
        pl.say(f"the penguin trains and earns {amount} speed") if log else None
        return "Penguin trains."

    def add_to_inventory(self, thing, amount):
        self.inventory[thing] = self.inventory.get(thing, 0) + amount

    def use(self, thing, amount):
        self.inventory[thing] = max(0, self.inventory.get(thing, 0) - amount)
        return [thing for _ in range(amount)]

    def add_to_clothes(self, cloth, amount):
        self.clothes[cloth] = self.clothes.get(cloth, 0) + amount

    def get_inventory(self) -> dict:
        return self.inventory

    def weight_to_speed_ratio(self) -> float:
        return self.weight / self.speed

    def dance(self, dance_type: str, shout: bool = False):
        pl.dance(dance_style=dance_type, shouting=shout)

    def say(self, *message, ending_signature: str="\n", breath_moments: str = ""):
        """
        make your penguin say something

        Args:
            ending_signature (str): what to say at the end. Defaults to "".
            breath_moments (str): what to breath after a message. Defaults to "\\n".
        """
        pprint.better_say(*message, end=ending_signature, seperator=breath_moments)

    def fall(self, floor_hardness, log: bool = False):
        speed -= floor_hardness
        pl.say(f"ouch. lost {floor_hardness} speed.") if log else None
        return "Pain"

    def quality_score(self) -> float:
        """
        check your penguin's quality. may be used for university or something. don't go fast.

        Returns:
            float: the quality
        """
        quality = 0
        quality += (self.money / 4)
        for i in self.inventory.values():
            quality += (i*1.5)

        quality += (self.speed*2)
        quality += (len(self.name) / 25)
        quality -= (self.weight * 0.6)
        clothes = 0
        for i in self.clothes.values():
            quality += (i*1.3)
            clothes += i
        if clothes >= 40: # messy alert
            quality -= 15
        if sum(self.inventory.values()) >= 111: # flex alert
            quality -= 15
        if sum(self.inventory.values()) >= 253: # too rich to hold anything alert
            quality -= 40
        if sum(self.inventory.values()) >= 506: # superflex alert
            quality -= (sum(self.inventory.values()) * 0.75)
        if sum(self.inventory.values()) >= 1002: # ultraflex alert
            quality -= (sum(self.inventory.values()) * 0.9)
        if self.speed >= 299_792_458: # light alert
            quality -= (self.speed*2.0002)

        if self.weight <= 3:
            quality += 0.999
        if self.money >= 1000: # rich factor
            quality += 5

        quality += self.banana.quality_ratio()
        


        return quality

    