from dataclasses import dataclass
import asyncio as asy
from .. import penglang as pl

@dataclass
class PenguinTimer:
    seconds: float
    ringtone: str = "RIIIING"
    name: str = "Timer"

    @pl.multitask
    async def start_timer(self):
        await asy.sleep(self.seconds)
        pl.say_in_a_box(message=self.ringtone, title=self.name, box_color="yellow")