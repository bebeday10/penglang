import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from rich.text import Text
from rich.live import Live
from .penglink.hubs import karaoke as plink
from .. import penglang as pl
import asyncio as asy
import pygame as pg



pg.mixer.init()

class PenguinKaraokeMachine:
    def __init__(self, songs: dict[str, dict[str, list[dict[str, float | str]]]], show_words: list[int], active_color: str ="white", inactive_color: str = "dim white", word_one_away_color: str = "#B4B4B4", name: str = "karaoke machine"):
        """
        the penguin karaoke machine to play songs

        # Args:
            songs (dict[str, list[dict[str, float  |  str]]]): the songs in the machine
            show_words (list[int]): lines to show. should be 2 items (0: behind, 1: infront).
            active_color (str, optional): _description_. Defaults to "#FFFFFF".
            inactive_color (str, optional): _description_. Defaults to "#5b5b5b".

        # Songs format:
            >>> {
                    "song":{ 
                        "song":[
                            {
                            "lyric": "hello",
                            "delay": 0.3,
                            "active color": "white",
                            "inactive color": "dim grey",
                            "word one away color": "#D3D3D3",
                            }
                        ],
                        "music": "path/to/file"
                    }
                }
        """
        self.songs: dict[str, dict[str, list[dict[str, float | str]]]] = songs
        self.show_words: list[int] = show_words
        self.active_color: str = active_color
        self.inactive_color: str = inactive_color
        self.word_one_away_color: str = word_one_away_color
        self.name: str = name


    @pl.multitask
    async def play_song(self, song_name: str, start_wait_time: int = 1, log: bool = False):
        if self.songs.get(song_name, {}).get("song") is None:
            pl.say("song doesn't exist!") if log else None
            return "Song doesn't exist."
        
        
        song: list[dict[str, float | str]] = self.songs[song_name]["song"]

        if not self.songs.get(song_name, {}).get("music") is None:
            pl.say("music found, song plays") if log else None
            pg.mixer.music.load(self.songs[song_name]["music"])
            pg.mixer.music.play()

        await asy.sleep(start_wait_time)

        try:

            with Live(refresh_per_second=30) as live:

                for i, lyric in enumerate(song):
                    t = Text()

                    
                    start = max(0, i - self.show_words[0])
                    end = min(len(song), i + self.show_words[1])

                    for j in range(start, end):
                        w = song[j].get("lyric", "oops")

                        if j - i == -1:
                            t.append(w, lyric.get("word one away color", self.word_one_away_color))

                        elif j < i:
                            t.append(w, lyric.get("inactive color", self.inactive_color))

                        elif j == i:
                            t.append(w, lyric.get("active color", self.active_color))

                        elif j - i == 1:
                            t.append(w, lyric.get("word one away color", self.word_one_away_color))

                        else:
                            t.append(w, lyric.get("inactive color", self.inactive_color))

                    live.update(t, refresh= True)
                    await asy.sleep(lyric.get("delay", 0.1))

            await asy.sleep(1)

        except Exception as e:
            pl.say(f"Karaoke explode {e}")

        pl.say("song has ended") if log else None

    def add_request(self, mode: str, request_name: str, song: str, amount: int, log: bool = False):
        if self.songs.get(song) is None:             
            pl.say("[bold blue]song doesn't exist[/bold blue]") if log else None
            return "Song doesn't exist"

        plink.add_request(request_name, self.name, mode, self.songs[song], song, amount, "PenguinKaraokeMachine")

    def accept_request(self, request_name, remove_request=True, log=False, overwrite: bool = False):
        result = plink.accept_request(request_name, self.name, log, remove_request)

        if result is None:
            pl.say("failed") if log else None
            return None
        
        if result[0] == "share recipe":
            if overwrite:
                self.songs.update(result[3])
            elif self.songs.get(result[2], None) is None:
                self.songs.update(result[3])
            else:
                self.songs[result[2]]["song"].extend(result[1].get("song"))

    def show_songs(self) -> dict[str, dict[str, list[dict[str, float | str]]]]:
        for song_name, song in self.songs.items():
            pl.say(f"{song_name}:")
            for lyric in song.get("song", []):
                pl.say(f"{lyric.get("lyric")}: {lyric.get("delay")}")

        return self.songs
        