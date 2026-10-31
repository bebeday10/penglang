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

    def __getitem__(self, key):
        if not self.stuff:
            return []
        if isinstance(key, int):
            changed_key = (key) % len(self.stuff)
            return self.stuff[changed_key]
        if isinstance(key, slice):
            changed_slice = [(key.start) % len(self.stuff) if key.start is not None else None, ((key.stop) % len(self.stuff)) if key.stop is not None else None, key.step]
            
            if (changed_slice[0] is not None) and (changed_slice[1] is not None):
                if changed_slice[1] < changed_slice[0]:
                    if changed_slice[0] is not None:
                        changed_slice[0] = (key.stop) % len(self.stuff)
                    if changed_slice[1] is not None:
                        changed_slice[1] = (key.start) % len(self.stuff)
            return self.stuff[changed_slice[0]:changed_slice[1]:changed_slice[2]]

