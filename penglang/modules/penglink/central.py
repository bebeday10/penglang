"""
PengLink, the bridge for items

The dictionary style:
{
    "request_name": {
        "frominternal": "class name as str"
        "from": "name of specific object"
        "mode": "see modes"
        "item": {
            "name": "name of item"
            "amount": int
            "supplies": {
                "supply": int
                }
            "price": int
            }
        "amount": int
        }
    }
}

Modes:
    share recipe: share a recipe with PenguinCoffeeMachine
    give: give something to something
"""

from ... import penglang as pl
import random as r
from rich import print_json

requests: dict = {}


def show_requests(mode="normal"):
    if mode == "dev":
        print_json(data=requests)

    else:
        def autoforloop(dictionary):
            for key, value in dictionary.items():
                if isinstance(value, dict):
                    pl.say(f"{key} is:")
                    autoforloop(value)

                else:
                    pl.say(f"{key} is {value}")
            else:
                pl.say("------")

        autoforloop(requests)
                
            




            

