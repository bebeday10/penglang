from typing_extensions import Self
from typing import SupportsFloat, SupportsIndex



class PenguinFloat(float):
    def __new__(cls, x: str | SupportsFloat | SupportsIndex = 0) -> Self:
        return super().__new__(cls, x)
    
    def penguin_round(self, digits=2):
        return round(self, digits)

    def penguin_temperature(self, unit="°C"):
        return f"{self}{unit} 🐧"