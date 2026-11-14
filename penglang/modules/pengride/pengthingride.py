from dataclasses import dataclass
from typing import Any

from .pengride import PenguinRide


@dataclass
class PenguinThingRide(PenguinRide):
    people: list[Any] | None = None