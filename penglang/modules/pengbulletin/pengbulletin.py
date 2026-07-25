




from typing import Callable

from ...penglang import multitask
from ... import penglang as pl
import asyncio as asy
from .. import pengrandom as pd
from . import pengbulletinmessage as pbm


class PenguinBulletinBoard:
    
    def __init__(
            self,
            speed: list[float] = [1, 5]
            
    ) -> None:
        self.config = {
            "bulletin": {
                
                "objects": pbm.objects,
                "actions": pbm.actions,
                "aftermath": pbm.aftermath,
                "places": pbm.places,
                "news": pbm.news,
                "speed": speed
            }
        }
        self.run = False

    @multitask
    async def start(self):
        self.run = True
        bulletin = self.config.get("bulletin", {})
        objects = bulletin.get("objects", [])
        places = bulletin.get("places", [])
        news = bulletin.get("news", [])
        actions = bulletin.get("actions", [])
        aftermath = bulletin.get("aftermath", [])
        speed = bulletin.get("speed", [1, 5])
        try:
            while self.run:
            
                pl.say(f"[{"".join(i for i in pd.random_decisions(**news))}] {pd.random_decision(*objects)} are currently {pd.random_decision(*actions)} {pd.random_decision(*places)}, and others are {pd.random_decision(*aftermath)}.")
                await asy.sleep(pd.random_decimal(speed[0], speed[1]))
        except (KeyboardInterrupt, asy.CancelledError):
            pl.say("stopped.")
            
            

    def stop(self):
        self.run = False

    def get_news(self):
        bulletin = self.config.get("bulletin", {})
        objects = bulletin.get("objects", [])
        places = bulletin.get("places", [])
        news = bulletin.get("news", [])
        actions = bulletin.get("actions", [])
        aftermath = bulletin.get("aftermath", [])

        return f"[{"".join(i for i in pd.random_decisions(**news))}] {pd.random_decision(*objects)} are currently {pd.random_decision(*actions)} {pd.random_decision(*places)}, and others are {pd.random_decision(*aftermath)}."
    
    def watch_function(self, func: Callable):
        def inner(*args, **kwargs):
            pl.say(f"[News] {func.__name__} is currently running, and others are waiting for it to run.")
            func(*args, **kwargs)
            pl.say(f"[News] {func.__name__} is currently finished running, and others are breathing.")
            if func.__name__ not in self.config.get("bulletin", {}).get("objects"):
                self.config["bulletin"]["objects"].append(func.__name__)

        return inner


    