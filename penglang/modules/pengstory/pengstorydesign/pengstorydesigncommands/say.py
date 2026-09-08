from .... import pengprint as pprint

def say(*args, separator: str = "", end: str = "\n", name: str | None = None):
    if name is None:
        return lambda: pprint.better_say(*args, seperator=separator, end=end)
    return lambda: pprint.better_say(f"{name}: ", *args, seperator=separator, end=end)