from dataclasses import dataclass

from ...penglang import PenguinError

from .pengfood import PenguinFood
from .pengfoodrecipe import PenguinFoodRecipe
from .. import pengerror as pe
PenguinFoodNotFoundError = pe.make_error("PenguinFoodNotFoundError", PenguinError)
PenguinInsufficientIngredientsError = pe.make_error("PenguinInsufficientIngredientsError", PenguinError)
@dataclass
class PenguinFoodMachine:
    ingredients: dict[str, float | int] | None = None
    recipes: list[PenguinFoodRecipe] | None = None

    def __post_init__(self):
        self.ingredients = self.ingredients or {}
        self.recipes = self.recipes or []
    def add_ingredients(self, **ingredients):
        for ingredient, amount in ingredients.items():
            self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + amount

    def make_food(self, food_name):
        food_index = 0
        for i, recipe in enumerate(self.recipes):
            if food_name == recipe:
                food_index = i
                break
        else:
            raise PenguinFoodNotFoundError(f"{food_name} was not found.")

        for ingredient, amount in self.recipes[food_index].recipe.items():
            if self.ingredients.get(ingredient, 0) < amount:
                raise PenguinInsufficientIngredientsError(f"the ingredient {ingredient} had only {amount} of it, but the recipe required {amount}.")

        for ingredient, amount in self.recipes[food_index].recipe.items():
            self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) - amount

        return PenguinFood(food_name)

            
    def __contains__(self, item):
        return item in self.ingredients