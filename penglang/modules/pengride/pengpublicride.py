from dataclasses import dataclass

from .pengride import PenguinRide


@dataclass
class PenguinPublicRide(PenguinRide):
    """
    A public ride that supports more people.
    """
    max_people: int = 100