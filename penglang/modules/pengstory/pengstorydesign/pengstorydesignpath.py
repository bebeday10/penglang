from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pengstorydesign import PenguinIceOfStoryDecisions as PIOSD
@dataclass
class PenguinIceOfStoryDecisionsPath:
    root: "PIOSD"
    path: list | None = None

    def __post_init__(self):
        self.path = self.path or []

    def get(self):
        destination: dict = self.root.story
        for i in self.path:
            destination = destination[i]

        return destination

    def to_decider(self) -> list:
        return self.path