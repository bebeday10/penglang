from typing import Iterable


class PenguinDictionary(dict):

    def __init__(self: dict[bytes, bytes], iterable: Iterable[list[bytes]]) -> None:
        super().__init__(iterable)

    def fish_keys(self):
        return list(self.keys())
    
    def penguin_merge(self, other):
        self.update(other)

    def ice_report(self):
        return f"🐧 {len(self)} entries"