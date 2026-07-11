from ... import penglang as pl
from typing import Any
from ..penglink.hubs import song as plink

class PenguinSong:
    def __init__(self, body: dict[str, list[dict[str, str | float]]], name: str = "song") -> None:
        self.song: dict[str, list[dict[str, str | float]]] = body
        self.name: str = name

    def add_lyric(self, *lyrics) -> None:
        try:
            for piece in lyrics:
                if isinstance(piece, list):
                    self.song["song"].extend(piece)
                
                if isinstance(piece, dict):
                    self.song["song"].append(piece)
        except KeyError as e:
            pl.say("[red] the penguin can't find [/red]")
            return None

    def configure_lyric(self, lyric: int, config_what: str, config_to: Any) -> None:
        try:
            to_config: dict[str, str | float] = self.song["song"][lyric]
        except KeyError as e:
            pl.say("[red] the penguin can't find [/red]")
            return None
        
        to_config[config_what] = config_to

    def remove_lyric(self, *lyrics: int):
        try:
            for lyric in lyrics:
                self.song["song"].pop(lyric)
        except KeyError as e:
            pl.say("[red] the penguin can't find [/red]")
            return None
        
    def add_request(self, mode: str, request_name: str, log: bool = False):
        plink.add_request(request_name=request_name, name=self.name, mode=mode, item=self.song, item_name=self.name, internal_name="PenguinSong", log=log, amount=0)

    def accept_request(self, request_name: str, log: bool = False, remove_request: bool = True):
        result = plink.accept_request(
            request_name=request_name,
            name=self.name,
            log=log,
            remove_request=remove_request
        )
        if result is None:
            pl.say("failed") if log else None
            return None

        if result[0] == "share recipe":
            self.song, self.name = result[1], result[2]


        


    def __getitem__(self, key):
        return self.song["song"][key]
    
    def __str__(self) -> str:
        return f"penguin song named {self.name} containing" + ", ".join(i.get("lyric", "nothing") for i in self.song.get('song', {}))



