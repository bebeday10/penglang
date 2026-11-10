from dataclasses import dataclass
from string import hexdigits
from . import pengprint as pprint
from .. import penglang as pl
from random import choice, uniform

@dataclass
class PenguinBluescreen:
    text: str = "Penguin has bluescreened."
    color: str = "blue"
    text_color: str = "white"
    error_code: str = "PENGUIN_KERNEL_FATAL"
    show_sad_face: bool = True
    recovery_message: str = "Penguin is recovering..."
    recovery_percentage: float | int = 99
    show_recovery: bool = True
    
    def bluescreen(self):
        sizes = pprint.get_ice_size()
        middle = sizes.lines // 2
        for i in range(sizes.lines):
            if i == 0 and self.show_sad_face:
                pl.say(f"[{self.text_color} on {self.color}]{":(":<{sizes.columns}}")
            elif i == middle:
                pl.say(f"[{self.text_color} on {self.color}]{self.text:^{sizes.columns}}")
            elif i == sizes.lines - 2 and self.show_recovery:
                pl.say(f"[{self.text_color} on {self.color}]{f"{self.recovery_message}: {self.recovery_percentage}%":^{sizes.columns}}")
            elif i == sizes.lines - 1:
                pl.say(f"[{self.text_color} on {self.color}]{self.error_code:^{sizes.columns}}")
            else:
                pl.say(f"[{self.text_color} on {self.color}]{" "*sizes.columns}")

    def randomize(self):
        self.text = choice(
            [
                "Penguin has bluescreened.",
                "Multi-language error.",
                "PengOS has encountered an error and requires to restart.",
                "Penguin overflow.",
                "Duck interface crashed.",
                "Pro burner chip failed."
            ]
        )
        
        self.color = f"#{choice(hexdigits)}{choice(hexdigits)}{choice(hexdigits)}{choice(hexdigits)}{choice(hexdigits)}{choice(hexdigits)}"
        self.text_color = f"#{choice(hexdigits)}{choice(hexdigits)}{choice(hexdigits)}{choice(hexdigits)}{choice(hexdigits)}{choice(hexdigits)}"
        self.error_code = choice(
            [
                "PENGUIN_KERNEL_FATAL",
                "PENGUIN_KERNEL_MINOR",
                "PENGUIN_INT_OVERFLOW",
                "PENGUIN_DUCK_SEQUENCE",
                "PENGUIN_OVERLY_CRYPTIC",
                "PENGUIN_BURNED_DOWN"
            ]
        )
        self.show_sad_face = choice([True, False])
        self.show_recovery = choice([True, False])
        self.recovery_message = choice(
            [
                "Penguin is recovering...",
                "Reverting penguin changes...",
                "What did the duck do...",
                "Reducing penguins..."
            ]
        )
        self.recovery_percentage = uniform(0, 100)