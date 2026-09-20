from dataclasses import dataclass
from typing import Any
from copy import deepcopy

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
        self.position[direction] = self.position.get(direction, 0) + movement

    def pin(self, name: str):
        self.pins[name] = deepcopy(self.position)

    def get_far_from_start(self):
        distance = 0
        for i in self.position.values():
            if i < 0:
                i *= -1
            distance += i
        if distance < 0:
            distance *= -1

        return distance

    def get_pin_far_from_start(self, pin):
        distance = 0
        for i in self.pins.get(pin, {}).values():
            if i < 0:
                i *= -1
            distance += i
        if distance < 0:
            distance *= -1

        return distance

    def get_far_from_pin(self, pin):
        longest_pin = self.pins.get(pin, {})
        shortest_pin = self.position
        distance = 0
        for k, v in longest_pin.items():
            temp_distance = v - shortest_pin.get(k, 0)
            if temp_distance < 0:
                temp_distance *= -1

            distance += temp_distance

        if distance < 0:
            distance *= -1
        return distance

    def get_pin_far_from_pin(self, pin_1, pin_2):
        longest_pin = self.pins.get(pin_1, {})
        shortest_pin = self.pins.get(pin_2, {})
        distance = 0
        for k, v in longest_pin.items():
            temp_distance = v - shortest_pin.get(k, 0)
            if temp_distance < 0:
                temp_distance *= -1

            distance += temp_distance


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
