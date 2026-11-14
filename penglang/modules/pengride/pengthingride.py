from dataclasses import dataclass
from typing import Any

from .pengride import PenguinRide


@dataclass
class PenguinThingRide(PenguinRide):
    """
    Use things instead of penguins to go on a ride.
    """
    people: list[Any] | None = None