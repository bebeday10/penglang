from copy import copy, deepcopy
from dataclasses import dataclass

from penglang import PenguinError
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
import wave
from datetime import timedelta

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
    import pygame


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
    sample_rate: int = 48000
    length: int = 0
    filename: str = "music.json"
    show_all: bool = False
    def __post_init__(self):
        pygame.mixer.init(
            frequency=self.sample_rate,
            size=-16,
            channels=2
        )
        self.cursor = self.cursor or [0, 0, self.octave]
        self.letters = self.letters or ["B", "A", "G", "F", "E", "D", "C"][::-1]
        self.tones = self.tones or {}
    def edit(self):
        if self.octave not in self.tones:
            self.tones[self.octave] = {i: {} for i in self.letters}
        for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
            for i in self.letters:
                
                for j in range(self.render_distance + self.render_shift + 2):
                    if j not in self.tones[octave][i]:
                        self.tones[octave][i][j] = None
        with Live(auto_refresh=False) as l:
            try:
                while True:
                    # --- Rendering ---
                    t = Text()
                    t.append("Penguin Music Workplace 🐧🎼\n\n", "bold")
                    t.append(f"Currently on: {self.letters[self.cursor[1]]}{self.octave} ({self.get_frequency(self.letters[self.cursor[1]], self.octave)}Hz) | Octave {self.octave} | BPM: {self.bpm} | Volume: {self.volume*100}% | Length: {self.length} bars | Duration: {timedelta(seconds=self.length*(60/self.bpm))} | Sample rate: {self.sample_rate}Hz | Filename: {self.filename} | Render Distance: {self.render_distance}\n\n")
                    # --- Grid part ---
                    t.append(f"  ")
                    for column in range(self.render_shift, self.render_distance + self.render_shift):
                        t.append(f" {column} " ) 
                    t.append("\n")
                    if self.show_all:
                        for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                            for i in range(len(self.letters) - 1, -1, -1):
                                t.append(f"{self.letters[i]} ")
                                for column in range(self.render_shift, self.render_distance + self.render_shift):
                                    if self.cursor[0] == column and self.cursor[1] == i and self.cursor[2] == octave:
                                        if self.tones[octave][self.letters[i]][column] is None:

                                            t.append(" ○ ", style="black on white blink")

                                        else:
                                            t.append(" ⏺ ", style="black on white blink")

                                    else:
                                        if self.tones[octave][self.letters[i]][column] is None:
                                            t.append(" ○ ")

                                        else:
                                            t.append(" ⏺ ")
                                t.append("\n")
                    else:
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
                    t.append("✥/WASD Move Cursor | Page Up/Down Octave +/- | ↳/E Declare Sound Existence | +/- BPM Increase/Decrease | [/] Change Volume by a Hundreth | (/) Change Sample Rate by One | {/} Change Render Distance | Ctrl+A Toggle Show All Octaves | Home Go to Position 1 | End Go to End | Ctrl+J Jump to Position | R Run | Ctrl+S Save | Ctrl+L Load | Ctrl+W Export WAV | Ctrl+E Evict Everyone | Ctrl+G Generate Certificate | Esc Exit Editor Profusely")
                    l.update(t, refresh=True)

                    # --- Key reading ---
                    key = rc.readkey()

                    if key == rc.key.ESC or key == rc.key.ESC_2:
                        break
                    elif key == rc.key.UP or key == "w":
                        if self.cursor[1] >= len(self.letters) - 1:
                            
                            self.octave += 1
                            self.cursor[2] += 1
                            if self.octave not in self.tones:
                                self.tones[self.octave] = {i: {} for i in self.letters}
                            for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                                for i in self.letters:
                                    
                                    for j in range(self.render_distance + self.render_shift + 2):
                                        if j not in self.tones[octave][i]:
                                            self.tones[octave][i][j] = None
                            self.cursor[1] = 0
                        else:
                            self.cursor[1] += 1
                    
                    elif key == rc.key.DOWN or key == "s":
                        if self.cursor[1] <= 0:
                            self.octave -= 1
                            self.cursor[2] -= 1
                            self.cursor[1] = len(self.letters) - 1
                            if self.octave not in self.tones:
                                self.tones[self.octave] = {i: {} for i in self.letters}
                            for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                                for i in self.letters:
                                    
                                    for j in range(self.render_distance + self.render_shift + 2):
                                        if j not in self.tones[octave][i]:
                                            self.tones[octave][i][j] = None
                            
                        else:
                            self.cursor[1] -= 1

                    elif key == rc.key.RIGHT or key == "d":
                        if self.cursor[0] >= self.render_distance + self.render_shift - 1:
                            self.render_shift += 1
                            if self.octave not in self.tones:
                                self.tones[self.octave] = {i: {} for i in self.letters}
                            for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                                for i in self.letters:
                                    
                                    for j in range(self.render_distance + self.render_shift + 2):
                                        if j not in self.tones[octave][i]:
                                            self.tones[octave][i][j] = None
                        self.cursor[0] += 1

                    elif key == rc.key.LEFT or key == "a":
                        if self.cursor[0] <= 0:
                            self.cursor[0] = 0
                            continue
                        if self.cursor[0] <= self.render_shift:
                            self.render_shift -= 1

                            if self.octave not in self.tones:
                                self.tones[self.octave] = {i: {} for i in self.letters}
                            for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                                for i in self.letters:
                                    
                                    for j in range(self.render_distance + self.render_shift + 2):
                                        if j not in self.tones[octave][i]:
                                            self.tones[octave][i][j] = None

                        self.cursor[0] -= 1

                    elif key == rc.key.ENTER or key == "e":
                        if self.tones[self.octave][self.letters[self.cursor[1]]][self.cursor[0]] is None:
                            if self.cursor[0] > self.length:
                                self.length = self.cursor[0]
                            self.tones[self.octave][self.letters[self.cursor[1]]][self.cursor[0]] = PenguinTone(self.get_frequency(self.letters[self.cursor[1]], self.octave), self.cursor)
                            sound = self.tones[self.octave][self.letters[self.cursor[1]]][self.cursor[0]].generate_tone(self.sample_rate, bpm=self.bpm)
                            sound.set_volume(self.volume)
                            sound.play()
                        else:
                            self.tones[self.octave][self.letters[self.cursor[1]]][self.cursor[0]] = None

                    elif key == rc.key.PAGE_UP:
                        self.octave += 1
                        self.cursor[2] += 1
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                            for i in self.letters:
                                
                                for j in range(self.render_distance + self.render_shift + 2):
                                    if j not in self.tones[octave][i]:
                                        self.tones[octave][i][j] = None
                        self.cursor[1] = len(self.letters) - 1
                    elif key == rc.key.PAGE_DOWN:
                        self.octave -= 1
                        self.cursor[2] -= 1
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                            for i in self.letters:
                                
                                for j in range(self.render_distance + self.render_shift + 2):
                                    if j not in self.tones[octave][i]:
                                        self.tones[octave][i][j] = None
                        self.cursor[1] = len(self.letters) - 1

                    elif key == "r":
                        
                        self.play()

                    elif key == rc.key.CTRL_S:
                        self.save()

                    elif key == rc.key.CTRL_L:
                        self.load()

                    elif key == rc.key.CTRL_E:
                        self.tones = {}
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                            for i in self.letters:
                                
                                for j in range(self.render_distance + self.render_shift + 2):
                                    if j not in self.tones[octave][i]:
                                        self.tones[octave][i][j] = None

                    elif key == rc.key.CTRL_G:
                        print(f"{f"Certificate of {self.filename}":=<50}")
                        print(f"This file, {self.filename}, worked by Penguin Music Workplace, is a document featuring music.")
                        print(f"Author: Somewhere between you and PengLang"),
                        print(f"Cheering Penguins 🎉🐧🎼")
                        print(f"{"="*50}")

                    elif key == "+":
                        self.bpm += 1
                    elif key == "-":
                        self.bpm -= 1

                    elif key == rc.key.CTRL_W:
                        self.export()

                    elif key == "[":
                        self.volume -= 0.0001

                    elif key == "]":
                        self.volume += 0.0001

                    elif key == "{":
                        self.render_distance -= 1
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                            for i in self.letters:
                                
                                for j in range(self.render_distance + self.render_shift + 2):
                                    if j not in self.tones[octave][i]:
                                        self.tones[octave][i][j] = None

                    elif key == "}":
                        self.render_distance += 1
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                            for i in self.letters:
                                
                                for j in range(self.render_distance + self.render_shift + 2):
                                    if j not in self.tones[octave][i]:
                                        self.tones[octave][i][j] = None

                    elif key == "(":
                        self.sample_rate -= 1
                        pygame.mixer.init(
                            frequency=self.sample_rate,
                            size=-16,
                            channels=2
                        )

                    elif key == ")":
                        self.sample_rate += 1
                        pygame.mixer.init(
                            frequency=self.sample_rate,
                            size=-16,
                            channels=2
                        )

                    elif key == rc.key.CTRL_A:
                        self.show_all = not self.show_all

                    elif key == rc.key.HOME:
                        self.cursor[0] = 0
                        self.render_shift = 0
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                            for i in self.letters:
                                
                                for j in range(self.render_distance + self.render_shift + 2):
                                    if j not in self.tones[octave][i]:
                                        self.tones[octave][i][j] = None
                    elif key == rc.key.END:
                        self.cursor[0] = self.length
                        self.render_shift = self.length - self.render_distance + 1
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        
                        for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                            for i in self.letters:
                                
                                for j in range(self.render_distance + self.render_shift + 2):
                                    if j not in self.tones[octave][i]:
                                        self.tones[octave][i][j] = None

                    elif key == rc.key.CTRL_J:
                        try:
                            answer = int(input("Position: "))
                        except ValueError:
                            print("Please give a numerical chance")
                            continue
                        if answer < 0:
                            answer = 0
                        self.cursor[0] = answer
                        self.render_shift = max(0, answer - self.render_distance + 1)
                        if self.octave not in self.tones:
                            self.tones[self.octave] = {i: {} for i in self.letters}
                        for octave in range(max(self.tones.keys()), min(self.tones.keys()) - 1, -1):
                            for i in self.letters:
                                
                                for j in range(self.render_distance + self.render_shift + 2):
                                    if j not in self.tones[octave][i]:
                                        self.tones[octave][i][j] = None
            except Exception as e:
                print(f"We have saved you from losing data. {e}")
                self.save()
                raise PenguinError("read above ^^")

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
    def mix_position(self, position: int) -> array.array:
        combined = []

        for tone in self.get_tones_at(position):
            sound = tone.generate_tone(
                sample_rate=self.sample_rate,
                bpm=self.bpm
            )

            samples = array.array("h", sound.get_raw())

            if len(samples) > len(combined):
                combined.extend([0] * (len(samples) - len(combined)))

            for i, sample in enumerate(samples):
                combined[i] += sample

        if not combined:
            return array.array("h")

        peak = max(abs(sample) for sample in combined)

        if peak > 32767:
            scale = 32767 / peak
            combined = [int(sample * scale) for sample in combined]

        return array.array("h", combined)
    def play_position(self, position: int):
        combined = self.mix_position(position)

        if combined:
            sound = pygame.mixer.Sound(buffer=combined.tobytes())
            sound.set_volume(self.volume)
            sound.play()

    def save(self, filename: str | None = None):
        filename = filename or self.filename + ".json"
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
        filename = filename or self.filename + ".json"
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

    def export(self, filename: str | None = None):
        filename = filename or self.filename + ".wav"

        with wave.open(filename, "wb") as f:
                f.setnchannels(2)
                f.setsampwidth(2)
                f.setframerate(self.sample_rate)
                audio_data = bytearray()
                for pos in range(self.length + 1):
                    combined = [0] * (int(self.sample_rate * 60 / self.bpm) * 2)

                    for tone in self.get_tones_at(pos):
                        sound = tone.generate_tone(
                            sample_rate=self.sample_rate,
                            bpm=self.bpm
                        )

                        samples = array.array("h", sound.get_raw())

                        for i in range(len(samples)):
                            combined[i] += samples[i]

                    peak = max(abs(sample) for sample in combined)

                    if peak > 32767:
                        scale = 32767 / peak
                        combined = [int(sample * scale) for sample in combined]

                    combined = array.array("h", combined)

                    audio_data.extend(combined.tobytes())
                f.writeframes(audio_data)
                                
        
        

