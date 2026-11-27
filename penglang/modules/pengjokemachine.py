from dataclasses import dataclass
from ..penglang import multitask
from asyncio import sleep
from rich import print
from random import choice

@dataclass
class PenguinJokeMachine:
    punchline_wait_seconds: int = 1

    def __post_init__(self):
        self.objects = [
            "chicken",
            "penguin",
            "spider",
            "dog",
            "cat",
            "horse",
            "alligator",
            "monkey",
            "cheetah",
            "atoms",
            "human",
            "grizzly bear",
            "employee",
            "octopus",
            "hat",
            "top hat",
            "head",
            "mozzarella cheese",
            "chihuahua",
            "investigator",
            "baker",
            "buffalo",
            "bison",
            "plant",
            "aloe vera",
            "cow",
            *list("1234567890"),
            "belt",
            "director",
            "producer",
            "knock-knock joke",
            "bell",
            "guy",
            "son"
        ]
        self.places = [
            "the road",
            "home",
            "the mall",
            "the city",
            "the Atlantic",
            "the other side",
            "the calendar factory",
            "the cafe",
            "college",
            "date night",
            "the cinema",
            "the moo-vies",
            "the studio",
            "game night",
            
        ]
    @multitask
    async def joke(self):
        print(self.get_start())
        await sleep(self.punchline_wait_seconds)
        print(self.get_end())

    def get_start(self):
        obj = choice(self.objects)
        second_obj = choice(self.objects)
        place = choice(self.places)
        starts = [
            f"Why did the {obj} cross {place}?",
            f"Knock knock.",
            f"Why did the {obj} invest?",
            f"Why don't scientists believe {obj}?",
            f"Why did the {obj} get fired from {place}?",
            f"How many tickles does it take to make a {obj} laugh?",
            f"What did one {obj} say to the other?",
            f"What did the {obj} say when their {second_obj} left for {place}?",
            f"What do {obj} do on {place}?",
            f"What did {obj} say to {second_obj}?",
            f"Did you hear about the {obj} who invented the {second_obj}?"
        ]
        return choice(starts)

    def get_end(self):
        obj = choice(self.objects)
        place = choice(self.places)
        ends = [
            f"Because it wanted to get to {place}.",
            f"{obj}'s here.",
            f"Because it was a {obj} at {place}.",
            "Because they make up everything.",
            "They took a day off.",
            "Ten-tickles.",
            f"You wait here. I'll go on a {obj}.",
            f"{obj}.",
            f"The {obj} told it to.",
            f"Go to {obj}.",
            f"Nice {obj}.",
            f"They won the no-{obj} prize."
        ]
        return choice(ends)
