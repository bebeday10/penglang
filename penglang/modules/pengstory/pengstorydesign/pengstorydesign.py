from dataclasses import dataclass

@dataclass
class PenguinIceOfStoryDecisions:
    name: str
    story: dict | None = None
    inventory: dict | None = None
    state: dict | None = None

    def __post_init__(self):
        self.story = self.story or {}
        self.inventory = self.inventory or {}
        self.state = self.state or {}

    def add_to_story(self, part, to_add):
        destination = self.story
        for journey in part[:-1]:
            destination = destination[journey]
        destination[part[-1]] = to_add