from dataclasses import dataclass
from . import pengrandom as pr
from .. import PenguinError, penglang as pl

@dataclass
class PenguinBoxOfStuff:
    stuff: list | None = None
    name: str = "Box"

    def __post_init__(self):
        self.stuff = self.stuff or []

    def get_something(self):
        try:
            thing = pr.random_decision(*self.stuff)
            self.stuff.remove(thing)
        except IndexError:
            raise PenguinError("there were too little items to pick from (try to have less than have)")
        return thing

    def get_multiple_things(self, amount):
        things = []
        try:
            for i in range(amount):
                things.append(self.get_something())
        except IndexError:
            raise PenguinError("there were too little items to pick from (try to have less than have)")
        return things

    def get(self):
        return self.stuff

    def has_item(self, item):
        return item in self.stuff

    def __str__(self):
        return f"a box of stuff named {self.name} with {", ".join(str(stuff) for stuff in self.stuff)}"

    def __len__(self):
        return len(self.stuff)

    def __call__(self):
        return self.get_something()

    def __bool__(self):
        return bool(self.stuff)