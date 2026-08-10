from dataclasses import dataclass
from typing import Any

@dataclass
class PenguinCursor:
    """
    A penguin made cursor. Useful for keeping track where you go.

    Args:
        position (dict | None): the positions. for example: {"x": 0, "y": 0}
        pins (dict | None): the pins. for placing a permanent spot.
    """
    position: dict[str, int] | None = None
    pins: dict[str, dict[str, int]] | None = None
    def __post_init__(self):
        self.position = self.position or {}
        self.pins = self.pins or {}

    def move(self, direction: Any, movement: int):
        self.position[direction] = self.position.get("direction", 0) + movement

    def pin(self, name: str):
        self.pins[name] = self.position

    def get_far_from_start(self):
        distance = 0
        for i in self.position.values():
            distance += i
        if distance < 0:
            distance *= -1

        return distance

    def get_pin_far_from_start(self, pin):
        distance = 0
        for i in self.pins.get(pin, {}).values():
            distance += i
        if distance < 0:
            distance *= -1

        return distance

    def get_far_from_pin(self, pin):
        pin_distance = self.get_pin_far_from_start(pin)
        current_distance = self.get_far_from_start()
        distance = pin_distance - current_distance
        if distance < 0:
            distance *= -1
        return distance

    def get_pin_far_from_pin(self, pin_1, pin_2):
        pin_1_distance = self.get_pin_far_from_start(pin_1)
        pin_2_distance = self.get_pin_far_from_start(pin_2)
        distance = pin_1_distance - pin_2_distance
        if distance < 0:
            distance *= -1
        return distance

    def get_position(self):
        return self.position

    def has_pin(self):
        for pin in self.pins.values():
            if pin == self.position:
                return True
        else:
            return False

    def get_pin(self):
        for name, pin in self.pins.items():
            if pin == self.position:
                    return name
        else:
            return None

    def remove_pin(self, pin):
        self.pins[pin] = None

    def go_to_pin(self, pin):
        self.position = self.pins.get(pin, self.position)
