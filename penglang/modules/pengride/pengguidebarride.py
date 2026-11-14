from dataclasses import dataclass

from .pengride import PenguinRide
from ..pengerror import make_error
from ...penglang import PenguinError
from .. import pengnoend as pne
PenguinLocationNotLocatableError = make_error("PenguinLocationNotLocatableError", PenguinError)

@dataclass
class PenguinGuideBarRide(PenguinRide):
    """
    Ride that uses guide bars and has predetermined locations.
    """
    locations: pne.PenguinNoEnd[str] | None = None

    def __post_init__(self):
        self.locations = self.locations or []
        return super().__post_init__()

    def ride_to(self, location):
        if location not in self.locations:
            raise PenguinLocationNotLocatableError(f"{location} is not in the supplied locations.")
        return super().ride_to(location)

    def ride_to_next_location(self):
        self.locations.forward(1)
        self.location = self.locations.get()

    def __contains__(self, item):
        return item in self.locations
