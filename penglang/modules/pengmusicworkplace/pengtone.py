from dataclasses import dataclass
import math
import array
import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
    import pygame



@dataclass
class PenguinTone:
    frequency: int
    position: list[int]
    duration: int = 1
    def generate_tone(self, sample_rate = 48000, bpm=120):

        samples = array.array("h")
        duration = self.duration * (60/bpm)
        for i in range(int(sample_rate * duration)):
            t = i / sample_rate
            value = int(math.sin(2 * math.pi * self.frequency * t) * 32767)

            samples.append(value)  # Left
            samples.append(value)  # Right

        return pygame.mixer.Sound(buffer=samples)

    def to_dictionary(self):
        return self.__dict__

    @classmethod
    def from_dictionary(cls, data):
        temp = cls(0, 0)
        for key, value in data.items():
            setattr(temp, key, value)
        return temp