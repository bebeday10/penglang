from copy import copy, deepcopy
from dataclasses import dataclass
from .pengtone import PenguinTone
from rich.live import Live
from rich.text import Text
import readchar as rc
from rich import print
import os
import math
import array
import json
from .. import pengerror as pe

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
pygame.mixer.init(
    frequency=48000,
    size=-16,
    channels=2
)
NOTES = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11
}
PenguinMusicNotFoundError = pe.make_error("PenguinMusicNotFoundError", FileNotFoundError)
@dataclass
class PenguinMusicWorkplace:
    tones: dict[int, dict[str, dict[int, PenguinTone]]] | None = None
    bpm: int = 120
    volume: int = 0.5
    current_position: int = 0
    cursor: list[int] | None = None
    letters: list[str] | None = None
    octave: int = 4
    render_distance: int = 6
    render_shift: int = 0
    sample_rate: int = 44100
    length: int = 0
    filename: str = "music.json"
    def __post_init__(self):
        
        self.cursor = self.cursor or [0, 0]
        self.letters = self.letters or ["B", "A", "G", "F", "E", "D", "C"][::-1]
        self.tones = self.tones or {}
    def edit(self):
        if self.octave not in self.tones:
            self.tones[self.octave] = {i: {} for i in self.letters}
        for i in self.letters:
            
            for j in range(self.render_distance + self.render_shift + 2):
                if j not in self.tones[self.octave][i]:
                    self.tones[self.octave][i][j] = None
        with Live(refresh_per_second=60) as l:
            while True:
                # --- Rendering ---
                t = Text()
                t.append("Penguin Music Workplace 🐧🎼\n\n", "bold")
                t.append(f"Octave {self.octave}\n\n")
                # --- Grid part ---
                t.append(f"  ")
                for column in range(self.render_shift, self.render_distance + self.render_shift):
                    t.append(f" {column} " ) 
                t.append("\n")
                for i in range(len(self.letters) - 1, -1, -1):
                    t.append(f"{self.letters[i]} ")
                    for column in range(self.render_shift, self.render_distance + self.render_shift):
                        if self.cursor[0] == column and self.cursor[1] == i:
                            if self.tones[self.octave][self.letters[i]][column] is None:

                                t.append(" ○ ", style="black on white blink")

                            else:
                                t.append(" ⏺ ", style="black on white blink")

                        else:
                            if self.tones[self.octave][self.letters[i]][column] is None:
                                t.append(" ○ ")

                            else:
                                t.append(" ⏺ ")
                    t.append("\n")
                t.append("\n")
                t.append("✥/WASD Move Cursor | Page Up/Down Octave +/- | ↳/E Declare Sound Existence | R Run | Ctrl+S Save | Ctrl+L Load | Ctrl+E Evict Everyone | Ctrl+G Generate Certificate | Esc Exit Editor Profusely")
                l.update(t, refresh=True)

                # --- Key reading ---
                key = rc.readkey()

                if key == rc.key.ESC or key == rc.key.ESC_2:
                    break
                elif key == rc.key.UP or key == "w":
                    if self.cursor[1] >= len(self.letters) - 1:
                        self.octave += 1
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for i in self.letters:
                            
                            for j in range(self.render_distance + self.render_shift + 2):
                                if j not in self.tones[self.octave][i]:
                                    self.tones[self.octave][i][j] = None
                        self.cursor[1] = 0
                    else:
                        self.cursor[1] += 1
                
                elif key == rc.key.DOWN or key == "s":
                    if self.cursor[1] <= 0:
                        self.octave -= 1
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for i in self.letters:
                            
                            for j in range(self.render_distance + self.render_shift + 2):
                                if j not in self.tones[self.octave][i]:
                                    self.tones[self.octave][i][j] = None
                        self.cursor[1] = len(self.letters) - 1
                        
                    else:
                        self.cursor[1] -= 1

                elif key == rc.key.RIGHT or key == "d":
                    if self.cursor[0] >= self.render_distance + self.render_shift - 1:
                        self.render_shift += 1
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for i in self.letters:
                            
                            for j in range(self.render_distance + self.render_shift + 2):
                                if j not in self.tones[self.octave][i]:
                                    self.tones[self.octave][i][j] = None
                    self.cursor[0] += 1

                elif key == rc.key.LEFT or key == "a":
                    if self.cursor[0] <= 0:
                        self.cursor[0] = 0
                        continue
                    if self.cursor[0] <= self.render_shift:
                        self.render_shift -= 1

                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for i in self.letters:
                            
                            for j in range(self.render_distance + self.render_shift + 2):
                                if j not in self.tones[self.octave][i]:
                                    self.tones[self.octave][i][j] = None

                    self.cursor[0] -= 1

                elif key == rc.key.ENTER or key == "e":
                    if self.tones[self.octave][self.letters[self.cursor[1]]][self.cursor[0]] is None:
                        if self.cursor[0] > self.length:
                            self.length = self.cursor[0]
                        self.tones[self.octave][self.letters[self.cursor[1]]][self.cursor[0]] = PenguinTone(self.get_frequency(self.letters[self.cursor[1]], self.octave), self.cursor)
                        sound = self.tones[self.octave][self.letters[self.cursor[1]]][self.cursor[0]].generate_tone(bpm=self.bpm)
                        sound.set_volume(self.volume)
                        sound.play()
                    else:
                        self.tones[self.octave][self.letters[self.cursor[1]]][self.cursor[0]] = None

                elif key == rc.key.PAGE_UP:
                    self.octave += 1
                    if self.octave not in self.tones:
                        self.tones[self.octave] = {i: {} for i in self.letters}
                    for i in self.letters:
                        
                        for j in range(self.render_distance + self.render_shift + 2):
                            if j not in self.tones[self.octave][i]:
                                self.tones[self.octave][i][j] = None
                    self.cursor[1] = len(self.letters) - 1
                elif key == rc.key.PAGE_DOWN:
                    self.octave -= 1
                    if self.octave not in self.tones:
                        self.tones[self.octave] = {i: {} for i in self.letters}
                    for i in self.letters:
                        
                        for j in range(self.render_distance + self.render_shift + 2):
                            if j not in self.tones[self.octave][i]:
                                self.tones[self.octave][i][j] = None
                    self.cursor[1] = len(self.letters) - 1

                elif key == "r":
                    
                    self.play()

                elif key == rc.key.CTRL_S:
                    self.save()

                elif key == rc.key.CTRL_L:
                    self.load()

                elif key == rc.key.CTRL_E:
                    self.tones = {}

                elif key == rc.key.CTRL_G:
                    print(f"{f"Certificate of {self.filename}":=<50}")
                    print(f"This file, {self.filename}, worked by Penguin Music Workplace, is a document featuring music.")
                    print(f"Author: Somewhere between you and PengLang"),
                    print(f"Cheering Penguins 🎉🐧🎼")
                    print(f"{"="*50}")
    def get_frequency(self, note: str, octave: int) -> float:
        midi = (octave + 1) * 12 + NOTES[note]

        return 440 * 2 ** ((midi - 69) / 12)

    def play(self):
        pygame.mixer.set_num_channels(128)
        for pos in range(self.length + 1):
            self.play_position(pos)
            pygame.time.wait(int(60000 / self.bpm))
        
            
    def get_tones_at(self, position: int) -> list[PenguinTone]:

        result = []

        for octave in self.tones.values():
            for note in octave.values():
                if position in note and note[position] is not None:
                    result.append(note[position])

        return result

    def play_position(self, position: int):
        
        for tone in self.get_tones_at(position):
            sound = tone.generate_tone(sample_rate=self.sample_rate, bpm=self.bpm)
            sound.set_volume(self.volume)
            sound.play()

    def save(self, filename: str | None = None):
        filename = filename or self.filename
        data = copy(self.__dict__)
        data["tones"] = {}
        for i, octave in self.tones.items():
            data["tones"][i] = {}
            for j, note in octave.items():
                data["tones"][i][j] = {}
                for k, pos in note.items():
                    if self.tones[i][j][k] is not None:
                        data["tones"][i][j][k] = self.tones[i][j][k].to_dictionary()
                    else:
                        data["tones"][i][j][k] = None

        with open(filename, "w") as f: json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)

    def load(self, filename: str | None = None):
        filename = filename or self.filename
        try:
            with open(filename, "r") as f:
                data: dict = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            raise PenguinMusicNotFoundError("penguin sought long but music was not found")
        for key, value in data.items():
            setattr(self, key, value)
        temp = deepcopy(self.tones)
        for i, octave in temp.items():

            self.tones[int(i)] = octave
            del self.tones[i]
        temp = deepcopy(self.tones)
        for i, octave in temp.items():
            for j, letter in octave.items():
                for k, note in letter.items():
                    self.tones[i][j][int(k)] = note
                    del self.tones[i][j][k]

        temp = deepcopy(self.tones)

        for i, octave in temp.items():
            for j, letter in octave.items():
                for k, note in letter.items():
                    if note is not None:
                        self.tones[i][j][k] = PenguinTone.from_dictionary(note)

        

            
        
        

