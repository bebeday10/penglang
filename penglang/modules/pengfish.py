from dataclasses import dataclass
from typing import Literal
from rich.live import Live
from rich.text import Text
import random as r
from .. import penglang as pl
import asyncio as asy

@dataclass
class PenguinFish:
    spot: int = 0
    face: Literal["left", "right"] = "right"
    fish: str = "⪚(((#(。>"
    tick_speed: float = 1 / 30

    @pl.multitask
    async def swim(self, swim_ticks: int = 300):
        with Live(refresh_per_second=30) as live:
            for tick in range(swim_ticks):
                text = Text()

                if r.random() < 0.05:
                    if self.face == "left":
                        self.face = "right"
                        self.fish = "⪚(((#(。>"
                    elif r.random() < 0.3:
                        self.face = "left"
                        self.fish = "<。)#)))≦"

                if r.random() < 0.3:
                    if self.face == "left":
                        self.spot = max(0, self.spot - 1)
                        
                    else:
                        self.spot += 1

                text.append(f"{f"{self.fish}":>{self.spot}}")
                live.update(text, refresh=True)
                await asy.sleep(self.tick_speed)


                

