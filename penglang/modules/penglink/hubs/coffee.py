"""
# The Coffee Hub

The hub for *coffee machines*.
Connect to PengLink here!
"""


import random as r
from .. import central as ct
from .... import penglang as pl


def add_request(request_name: str, name: str, mode: str, item: dict, item_name: str, amount: int, internal_name: str, log: bool = False):
    """
    add a request to PengLink

    # Args:
        request_name (str): the name for the request
        name (str): the name for the machine
        mode (str): the mode of giving
        item (dict): the item to share
        item_name (str): the item's name
        amount (int): the amount of that item to give
        internal_name (str): the machine's **internal** name
        log (bool, optional): whether to log or not. Defaults to False.

    Returns:
        None | str: the success. returns None if nothing wrong.
    """
    if not ct.requests.get(request_name) is None:
        pl.say("request already exists") if log else None
        return "Request already exists."

    ct.requests[request_name] = {
        "from": name,
        "frominternal": internal_name,
        "mode": mode,
        "item": item,
        "name": item_name,
        "amount": amount
    }


def accept_request(request_name: str, name: str, log: bool = False, remove_request: bool = True):
    """
    accept a valid request from the requests

    Args:
        request_name (str): the name of that request
        name (str): the name of *you*
        log (bool, optional): whether to log or not. Defaults to False.
        remove_request (bool, optional): _description_. Defaults to True.

    Returns:
        None | tuple: the tuple of your item. Returns None if failed.
    """
    if ct.requests.get(request_name) is None:
        pl.say("request doesn't exist") if log else None
        return None

    request: dict = ct.requests[request_name]

    if name == "PenguinCoffeeMachine":
        if request.get("mode") == "share recipe":
            item: dict = request.get("item", {})

            if item == {}: pl.say("no item found."); return None

            supplies: dict = item.get("supplies", {})

            item_name: str = request.get("name", "coffee")

            price: float = item.get("price", round(r.uniform(6, 9) * 20) / 20)

            if remove_request: ct.requests.pop(request_name)

            pl.say(f"received {item_name}'s recipe from [italic]{request["from"]}[/italic].") if log else None

            return "share recipe", {
                item_name: {
                    "amount": 0,
                    "supplies": supplies,
                    "price": price,
                }
            }, supplies, item_name, item

        else:
            item = request.get("item", {})

            if item == {}: pl.say("no item found.") if log else None; return None

            supplies: dict = item.get("supplies", {})

            item_name: str = request.get("name", "coffee")

            price: float = item.get("price", round(r.uniform(6, 9) * 20) / 20)

            amount: int = request.get("amount", 1)

            if remove_request: ct.requests.pop(request_name)

            pl.say(f"received {amount} {item_name}s from [italic]{request["from"]}[/italic].") if log else None

            return "give", item_name, amount, {
                item_name: {
                    "amount": amount,
                    "supplies": supplies,
                    "price": price,
                }
            }, item
