from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .. import pengstorydesign as psd
def add_to_inventory(story: "psd.PenguinIceOfStoryDecisions", thing, amount):
    def inner():
        story.inventory[thing] = story.inventory.get(thing, 0) + amount

    return inner

def get_inventory(story: "psd.PenguinIceOfStoryDecisions", thing, default=None):
    def inner():
        return story.inventory.get(thing, default)

    return inner


def remove_and_get_inventory(story: "psd.PenguinIceOfStoryDecisions", thing, amount: int | float, default=None):
    def inner():
        story.inventory[thing] = story.inventory.get(thing, 0) - amount
        return story.inventory[thing]

    return inner