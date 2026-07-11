from .... import penglang as pl
from .. import central as ct


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

    if request.get("mode") == "share recipe":
        item: dict = request.get("item")
        if item is None: pl.say("item doesn't exist") if log else None; return None
        item_name: str = request.get("name", "unknown")

        if remove_request: ct.requests.pop(request_name)

        return "share recipe", item, item_name, {
            item_name: item
        }