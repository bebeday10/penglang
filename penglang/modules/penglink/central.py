"""
# PengLink

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

# Modes:
    ## share recipe: share a recipe
        ### Support:
            PenguinCoffeeMachine
            PenguinVendingMachine
            PenguinKaraokeMachine
            PenguinSong
    ## give: give something to something
        ### Support:
            PenguinCoffeeMachine
            PenguinVendingMachine
"""

from ... import penglang as pl
import random as r
from rich import print_json

requests: dict = {}


def show_requests(mode="normal"):
    """
    show the requests dictionary

    Args:
        mode (str): the mode to show

    Examples:
        >>> show_requests("dev")
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
        >>> show_requests()
        request_name is:
            frominternal is class name as str
            from is name of specific object
            mode is see modes
            item is:
            name is name of item
            amount is amount of item
            supplies is:
            supply is amount of item
            ------
            price is price of item
            ------
            amount is amount of item
            ------
            ------

    """
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
