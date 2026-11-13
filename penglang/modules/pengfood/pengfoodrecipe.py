from dataclasses import dataclass


@dataclass
class PenguinFoodRecipe:
    name: str
    recipe: dict[str, int | float]