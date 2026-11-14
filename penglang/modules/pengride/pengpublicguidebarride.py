from dataclasses import dataclass

from .pengguidebarride import PenguinGuideBarRide
from .pengpublicride import PenguinPublicRide


@dataclass
class PenguinPublicGuideBarRide(PenguinPublicRide, PenguinGuideBarRide):
    """
    Ride that combines the people of the public and guide bars.
    """
    pass