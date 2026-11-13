from dataclasses import dataclass

from .pengfood import PenguinFood
from .. import pengerror as pe
from ... import penglang as pl
PenguinNotFoodError = pe.make_error("PenguinNotFoodError", TypeError)
PenguinDirtyDishError = pe.make_error("PenguinDirtyDishError", pl.PenguinError)
PenguinFoodConsumedError = pe.make_error("PenguinFoodConsumedError", pl.PenguinError)
@dataclass
class PenguinDish:
    food: PenguinFood | None = None
    dirty: bool = False
    def place_food(self, food: PenguinFood):
        self.dirty_check()
        if not isinstance(food, PenguinFood):
            raise PenguinNotFoodError(f"{food} ({type(food)}) is not PenguinFood.")
        if food.consumed:
            raise PenguinFoodConsumedError("the food has been consumed before.")

        self.food = food

    def eat_food(self):
        self.dirty_check()
        self.food_check()
        if self.food.consumed:
            raise PenguinFoodConsumedError("the food has been consumed before.")

        self.food.consumed = True
        self.food = None
        
    def dirty_check(self):
        if self.dirty:
            raise PenguinDirtyDishError("the dish is dirty, use dishwasher to wash it")
    def food_check(self):
        if not isinstance(self.food, PenguinFood):
            raise PenguinNotFoodError(f"{self.food} ({type(self.food)}) is not PenguinFood.")

    def __contains__(self, item):
        return self.food == item