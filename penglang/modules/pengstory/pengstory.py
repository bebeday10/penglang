from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import pengstorydesign as psd

@dataclass
class PenguinIceOfStoryDecisionsMachine:
    machine: "psd.PenguinIceOfStoryDecisions"