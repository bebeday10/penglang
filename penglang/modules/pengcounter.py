"""
# PengCounter
Counters are cool.  
Penguins are cool.
A simplistic counter for daily needs.
"""
from dataclasses import dataclass

@dataclass
class PenguinCounter:
    """
    A little counter for all your needs.
    """
    count: int
    interval: int
    def count_up(self, interval: int | None = None):
        interval = interval or self.interval
        count += interval

    def count_down(self, interval: int | None = None):
        interval = interval or self.interval
        count -= interval
