from dataclasses import dataclass

from .pengride import PenguinRide


@dataclass
class PenguinPublicRide(PenguinRide):
    max_people: int = 100