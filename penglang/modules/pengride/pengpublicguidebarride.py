from dataclasses import dataclass

from .pengguidebarride import PenguinGuideBarRide
from .pengpublicride import PenguinPublicRide


@dataclass
class PenguinPublicGuideBarRide(PenguinPublicRide, PenguinGuideBarRide):
    pass