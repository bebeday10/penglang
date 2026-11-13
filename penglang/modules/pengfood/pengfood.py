from dataclasses import dataclass


@dataclass
class PenguinFood:
    name: str
    consumed: bool = False