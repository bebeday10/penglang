from dataclasses import dataclass

from .pengride import PenguinRide
from ..pengerror import make_error
from ...penglang import PenguinError
from .. import pengnoend as pne
PenguinLocationNotLocatableError = make_error("PenguinLocationNotLocatableError", PenguinError)

@dataclass
class PenguinGuideBarRide(PenguinRide):
    locations: pne.PenguinNoEnd[str]

    def ride_to(self, location):
        if location not in self.locations:
            raise PenguinLocationNotLocatableError(f"{location} is not in the supplied locations.")
        return super().ride_to(location)

    def ride_to_next_location(self):
        self.locations.forward(1)
        self.location = self.locations.get()
