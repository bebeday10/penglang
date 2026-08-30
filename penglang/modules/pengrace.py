from dataclasses import dataclass
from typing import TYPE_CHECKING
from .. import penglang as pl
from textwrap import dedent

if TYPE_CHECKING:
    from .pengpenguin import pengracingpenguin as prp

@dataclass
class PenguinRace:
    name: str
    level: str
    participants: None | list["prp.RacingPenguin"] = None
    winner: str | None = None
    ended: bool = False

    def __post_init__(self):
        self.participants = self.participants or []

    def race_info(self):
        pl.say(dedent(
            f"""
                {self.level}
                {self.name}
                Participating:
                {", ".join(self.participants)}
                """
        ))