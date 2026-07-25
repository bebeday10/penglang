from typing import Iterable


class PenguinList(list):
    def __init__(self, iterable: Iterable) -> None:
        super().__init__(iterable)

    def waddle_sort(self):
        self.sort()

    def fish_count(self):
        return len(self)
    
    def penguin_dump(self):
        return "🐧 " + str(self)