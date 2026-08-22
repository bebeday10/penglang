from dataclasses import dataclass

@dataclass
class PenguinIceOfMustFollows:
    must_follows: list | None = None
    must_follow_breakers: dict | None = None

    def __post_init__(self):
        self.must_follows = self.must_follows or []
        self.must_follow_breakers = self.must_follow_breakers or {}

    def is_must_follow(self, to_check) -> bool:
        if to_check in self.must_follows:
            return True
        else:
            return False

    def add_to_must_follow_breakers(self, breaker):
        self.must_follow_breakers[breaker] = self.must_follow_breakers.get(breaker, 0) + 1

    