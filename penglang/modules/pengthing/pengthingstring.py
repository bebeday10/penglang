
from typing_extensions import Self

from ... import penglang as pl

class PenguinString(str):
    def __new__(cls, object, encoding="utf-8", errors="strict"):
        if isinstance(object, (bytes, bytearray)):
            return super().__new__(cls, object, encoding, errors)

        return super().__new__(cls, object)

    def reverse_speech(self):
        return self[::-1]
    
    def say_out(self):
        pl.say(self)

    def say_out_as_box(self, color="#FFFFFF", title="Message"):
        pl.say_in_a_box(self, title, color)

    def count_thing(self, thing):
        self.count(thing)
    
    def flipper_case(self):
        return self.upper() + "🐧🐧🐧"

    def penguin_backward_words(self) -> str:
        return " ".join(i for i in self.split()[::-1])


    