from dataclasses import dataclass
from typing import Self
from . import pengmath as pm
from .. import pengerror as pe
@dataclass
class PenguinTolerance:
    middle: float | int
    tolerance: float | int

    PenguinToleranceSizzlingSizeError = pe.make_error("PenguinToleranceSizzlingSizeError")
    PenguinToleranceNotANumberError = pe.make_error("PenguinToleranceNotANumberError")
    @classmethod
    def from_range(cls, range_arg: range) -> Self:
        listed_range = list(range_arg)
        try:
            middle = pm.penguin_median(listed_range[0], listed_range[1], *listed_range[2:])
        except IndexError:
            raise cls.PenguinToleranceSizzlingSizeError("range needs at least 3 items")
        average_start_end = pm.penguin_average(middle - listed_range[0], listed_range[-1] - middle)
        tolerance = average_start_end
        return cls(middle, tolerance)
    
    @classmethod
    def from_list(cls, list_arg: list) -> Self:
        try:
            middle = pm.penguin_median(list_arg[0], list_arg[1], *list_arg[2:])
        except IndexError:
            raise cls.PenguinToleranceSizzlingSizeError("list needs at least 3 items")
        average_start_end = pm.penguin_average(middle - list_arg[0], list_arg[-1] - middle)
        tolerance = average_start_end
        return cls(middle, tolerance)

    def __contains__(self, item):
        try:
            return self.middle - self.tolerance <= item <= self.middle + self.tolerance
        except TypeError:
            raise self.PenguinToleranceNotANumberError(f"please give a real number instead of {type(item)}")