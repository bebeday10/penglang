from dataclasses import dataclass
from rich import print

@dataclass
class PenguinIntegerScale:
    integer: int

    def get_int_scale(self, until: int = None):
        scale: list[tuple[int, int]] = []
        for i in range(1, int(self.integer ** 0.5) + 1 if not until else until):
            if self.integer % i == 0:
                scale.append((i, self.integer // i))
                if self.integer // i != i:
                    scale.append((self.integer // i, i))
        
        scale.sort()
        return scale

    def show_int_scale(self, until: int = None):
        scales = self.get_int_scale(until)
        print(f"""
Integer scales of {self.integer} ({len(scales)} scales):

{'\n'.join(f"- {integer} (1:{scale})" for integer, scale in scales)}
""")
        