from dataclasses import dataclass
from . import pengerror as pe
from .. import penglang as pl
@dataclass
class PenguinRectangleShape:
    """
    rectangle shape, aka aspect ratio
    shape: "x:y"
    """
    shape: str
    def __post_init__(self):
        PenguinShapeError = pe.make_error("PenguinShapeError")
        try:
            self.split_shape = list(map(int, self.shape.split(":")))
        except ValueError:
            try:
                self.split_shape = list(map(int, map(len, self.shape.split(":"))))
            except ValueError:
                raise PenguinShapeError("shape sizes cannot be your weird letters.")
        try:
            self.split_shape[0]
            self.split_shape[1]
        except IndexError:
            raise PenguinShapeError("the shape is not shaping. make sure it is using ':' and make sure it is not 1D")

    def simplify(self):
        result = 1

        for i in range(1, min(self.split_shape[0], self.split_shape[1]) + 1):
            if self.split_shape[0] % i == 0 and self.split_shape[1] % i == 0:
                result = i

        self.split_shape[0] //= result
        self.split_shape[1] //= result

    def compare(self, other: PenguinRectangleShape, *others: PenguinRectangleShape, log: bool = False):
        self.simplify()
        other.simplify()
        self_value = self.split_shape[0] * self.split_shape[1]
        other_value = other.split_shape[0] * other.split_shape[1]
        longest_first_split = len(max(self.shape, other.shape, *[i.shape for i in others], key=lambda k: len(k)))
        values = {}
        for i in others:
            i.simplify()
            values[i.shape] = i.split_shape[0] * i.split_shape[1]
        longest_number = len(max(self, other, *others, key=lambda k: len(str(k.split_shape[0] * k.split_shape[1]))))

        if log:
            pl.say(f"""Shape Comparison (min units):
------
{self.shape:<{longest_first_split}}'s: {self_value:>{longest_number}}
{other.shape:<{longest_first_split}}'s: {other_value:>{longest_number}}{"\n" if values else ""}{"\n".join(f"{k:<{longest_first_split}}'s: {v:>{longest_number}}" for k, v in values.items())}
Value {"increase" if self_value / other_value * 100 - 100 >= 0 else "decrease"}{f" (The first two)" if values else ""}: {self_value / other_value * 100 - 100 if self_value / other_value * 100 - 100 >= 0 else (self_value / other_value * 100 - 100) * -1}%
Winner{f" (of the first two)" if values else ""}: {self.shape if self_value > other_value else "tie" if self_value == other_value else other.shape}

Conclusion: {self.shape if self_value > other_value else "tie" if self_value == other_value else other.shape} might be a better value{f" (of the first two)" if values else ""}""")
        return self.shape if self_value > other_value else "tie" if self_value == other_value else other.shape

    def __len__(self):
        self.simplify()
        return self.split_shape[0] * self.split_shape[1]