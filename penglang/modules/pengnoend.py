from dataclasses import dataclass

@dataclass
class PenguinNoEnd:
    stuff: list
    current_selection: int = 0

    def forward(self, amount_forward: int = 1):
        if len(self.stuff) == 0:
            return None
        self.current_selection = (self.current_selection + amount_forward) % len(self.stuff)

    def backward(self, amount_backward: int = 1):
        if len(self.stuff) == 0:
            return None
        self.current_selection = (self.current_selection - amount_backward) % len(self.stuff)

    def get(self):
        if len(self.stuff) == 0:
            return None
        return self.stuff[self.current_selection]

    def reset(self):
        self.current_selection = 0

    def __call__(self):
        return self.get()

    def __str__(self):
        return str(self.get())

    def __len__(self):
        return len(self.stuff)