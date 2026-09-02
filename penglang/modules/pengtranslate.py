from copy import deepcopy
from dataclasses import dataclass
from typing import Generator, Iterable
from . import pengsymbol as ps
from . import pengiterable as pi

@dataclass
class PenguinTranslator:
    translate_to: list | None = None
    translate_from: list | None = None

    def __post_init__(self):
        self.translate_to = self.translate_to or list(map(str, ps.alphanums))
        if isinstance(self.translate_to, int):
            self.translate_to = str(self.translate_to)
        if isinstance(self.translate_to, str):
            self.translate_to = list(self.translate_to)
        self.translate_from = self.translate_from or list(map(str, ps.alphanums))
        if isinstance(self.translate_from, Iterable):
            self.translate_from = list(map(str, self.translate_from))
            self.translate_from = "".join(self.translate_from)
        self.translate_from = self.translate_from.lower()
        self.translate_from = list(self.translate_from)
        self.translate_to = list(map(str, self.translate_to))
        self.translate_key = pi.list_combine(self.translate_from, self.translate_to)

    def translate(self, text):
        text = list(text)
        for i, letter in enumerate(deepcopy(text)):
            try:
                text[i] = self.translate_key[letter.lower()]
            except KeyError:
                continue

        return "".join(text)   