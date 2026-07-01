import random as r
from .. import central as ct
from .... import penglang as pl


def add_request(request_name: str, name: str, mode: str, item: dict, item_name: str, amount: int, internal_name: str, log: bool = False):
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
            }, supplies, item_name

        else:
            item = request.get("item", {})

            if item == {}: pl.say("no item found.") if log else None; return None

            supplies: dict = item.get("supplies", {})

            item_name: str = item.get("name", "coffee")

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
            }
