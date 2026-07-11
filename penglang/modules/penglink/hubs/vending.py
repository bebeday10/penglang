from .. import central as ct
from .... import penglang as pl
import random as r


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
        "amount": amount,

    }


def accept_request(request_name: str, name: str, log: bool = False, remove_request: bool = True):
    if ct.requests.get(request_name) is None:
        pl.say("request doesn't exist") if log else None
        return None

    request: dict = ct.requests[request_name]

    if request.get("mode") == "give":  # request check
        item: dict = request.get("item")
        if item is None: pl.say("item doesn't exist") if log else None; return None

        item_name: str = request.get("name", "unknown")

        price: float = item.get("price", round(r.uniform(6, 9) * 20) / 20)

        amount: float = request.get("amount", 0)

        supplies: dict = item.get("supplies", {})

        if remove_request: ct.requests.pop(request_name)

        pl.say(f"received {amount} {item_name} from [italic]{request["from"]}[/italic].") if log else None

        return "give", {
            item_name: {
                "price": price,
                "quantity": amount,
                "supplies": supplies
            }
        }, item_name, amount



    elif request.get("mode") == "share recipe":
        item = request.get("item")
        if item is None: pl.say("item doesn't exist") if log else None; return None

        item_name: str = request.get("name", "unknown")
        price: float = item.get("price", round(r.uniform(6, 9) * 20) / 20)
        supplies: dict = item.get("supplies", {})

        if remove_request: ct.requests.pop(request_name)

        pl.say(f"received {item_name}'s recipe from [italic]{request["from"]}[/italic].") if log else None

        return "share recipe", {
            item_name: {
                "price": price,
                "quantity": 0,
                "supplies": supplies,
            }
        }, supplies, item_name
    
    pl.say("[red]cannot process this request. reason: unsupported mode[/red]") if log else None
