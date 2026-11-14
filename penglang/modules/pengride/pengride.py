from dataclasses import dataclass

from ..pengpenguin import Penguin


@dataclass
class PenguinRide:
    """
    Base ride class.
    """
    location: str
    people: list[Penguin] | None = None
    max_people: int = 6


    def __post_init__(self):
        self.people = self.people or []

    def ride_to(self, location: str):
        self.location = location
