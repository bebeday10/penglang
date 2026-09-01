from dataclasses import dataclass
@dataclass
class PenguinQuestion:
    question: str = ""

    def ask(self):
        return input(self.question)