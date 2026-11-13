from dataclasses import dataclass

from .pengdish import PenguinDish
from ... import penglang as pl
from .. import pengerror as pe
PenguinDishAlreadyCleanError = pe.make_error("PenguinDishAlreadyCleanError", pl.PenguinError)

@dataclass
class PenguinDishwasher:
    pass
    def clean_dish(self, dish: PenguinDish):
        if not dish.dirty:
            raise PenguinDishAlreadyCleanError("the dish is already clean what are you cleaning it for")

        dish.dirty = False