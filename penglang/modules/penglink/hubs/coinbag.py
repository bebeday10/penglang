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

    if request.get("mode") == "give":
        item: dict = request.get("item")
        amount: float | int = request.get('amount')
        item_name: str = request.get("name", "unknown")
        if remove_request: ct.requests.pop(request_name)

        return "give", item, item_name, amount, {item_name: item}