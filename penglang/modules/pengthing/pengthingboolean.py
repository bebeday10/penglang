from typing_extensions import Self


class PenguinBoolean:
    def __init__(self, value) -> None:
        self.value = bool(value)

    def penguin_truth(self):
        return self.value