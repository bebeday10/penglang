from .. import penglang
import random as r

def random_number(a: int, b: int) -> int:
    return r.randint(a, b)

def random_decimal(a: float, b: float) -> float:
    return r.uniform(a, b)

def random_decision(*options):
    return r.choice([i for i in options])

def random_range(start: int, stop: int, step: int) -> int:
    return r.randrange(start, stop, step)

def random_decisions(*_, times=1, **options):
    items: list = list(options.keys())
    weights: list = list(options.values())

    return r.choices(items, weights, k=times)