from dataclasses import dataclass
import enum
from typing import TYPE_CHECKING
from ... import penglang as pl
from . import pengraceerror as pre
from textwrap import dedent
from .. import pengrandom as pr
import asyncio as asy
from copy import deepcopy

if TYPE_CHECKING:
    from ..pengpenguin import pengracingpenguin as prp

@dataclass
class PenguinRace:
    name: str
    level: str
    race_length: int
    temperature: int | float
    course: str
    season: str
    track: str
    weather: str
    participants: None | list["prp.RacingPenguin"] = None
    winner: str | None = None
    ended: bool = False

    def __post_init__(self):
        self.participants: list["prp.RacingPenguin"] = self.participants or []

    def race_info(self):
        pl.say(dedent(
            f"""
                {self.level}
                {self.name}
                Temperature: {self.temperature}°
                Course: {self.course}
                Season: {self.season}
                Track: {self.track}
                Weather: {self.weather}
                Participating:
                {", ".join(participant.name for participant in self.participants)}
                """
        ))

    def add_participant(self, participant: "prp.RacingPenguin"):
        self.participants.append(participant)

    def remove_participant(self, participant: "prp.RacingPenguin"):
        try:
            self.participants.remove(participant)
        except ValueError:
            raise pre.PenguinParticipantError(f"Participant {participant} does not exist.")

    def get_participant_score_predictions(self, participant_number):
        try:
            self.participants[participant_number]
        except IndexError:
            raise pre.PenguinParticipantError(f"Participant number {participant_number} out of reach")

        participant: "prp.RacingPenguin" = self.participants[participant_number]

        speed = participant.speed * 1.4
        power = participant.power * 1.25
        stamina = participant.stamina * 1.3
        guts = participant.guts * 0.9
        wit = participant.wit * 1.1
        skills = len(participant.skills) * 6

        score = speed + power + stamina + guts + wit + skills

        return score

    def participant_score_predictions(self) -> list[str]:
        scores: dict[str, int | float] = {}
        for i, participant in enumerate(self.participants):
            score = self.get_participant_score_predictions(i)
            scores[participant.name] = score

        ranks = list(scores.values())
        ranks.sort(reverse=True)

        rankings: list[str] = []

        for rank in ranks:
            for participant, score in scores.items():
                if score == rank:
                    rankings.append(participant)


        return rankings

    def show_participant_score_predictions(self):
        rankings: list[str] = self.participant_score_predictions()
        for i, participant in enumerate(rankings, 1):
            pl.say(f"{i}: {participant}")


    @pl.multitask
    async def start_race(self):
        self.race_info()
        pl.say("Favorite:")
        self.show_participant_score_predictions()
        pl.say("The race is starting...")
        await asy.sleep(pr.random_decimal(2, 4))
        pl.say("OFF!")
        try:
            await asy.sleep(self.race_length / sorted([participant.speed for participant in self.participants], reverse=True)[0])  
            remaining = deepcopy(self.participants)
            self.winner: list = []
            for _ in enumerate(self.participants):
                self.winner.append(pr.random_decisions(**{participant.name: self.get_participant_score_predictions(i) for i, participant in enumerate(remaining)}))
                for participant in self.participants:
                    if self.winner[-1][0] == participant.name:
                        remaining.remove(participant)
                        break
                    
        except IndexError:
            raise pre.PenguinRaceError("The race broke down because there are approximately 0 participants")
        for i, place in enumerate(self.winner, start=1):
            pl.say(f"{i}: {place[0]}")
        for participant in self.participants:
            if self.winner[0][0] == participant.name:
                participant.racing_record.append(self.name)
                break