from dataclasses import dataclass, field
from decimal import Decimal
from functools import wraps
from typing import Callable
from ..penglink.hubs import coinbag as plink

@dataclass(order=True)
class PenguinCoinBag:
    balance: Decimal
    name: str
    owner: str
    config: dict = field(init=False)
    coin_history: list = field(init=False)
    

    def __post_init__(self):
        self.config = {"balance": self.balance}
        self.coin_history = []

    def deposit(self, amount: Decimal) -> None:
        self.balance += amount
        self.coin_history.append(f"deposited {amount}.")

    def withdraw(self, amount: Decimal) -> None:
        self.balance -= amount
        self.coin_history.append(f"withdrew {amount}.")

    def get_wallet_money(self) -> Decimal:
        self.coin_history.append(f"checked wallet.")
        return self.balance
    

    def change_owner(self, new_owner) -> None:
        self.coin_history.append(f"former owner {self.owner} has transferred ownership to {new_owner}.")
        self.owner = new_owner

    def get_wallet_owner(self) -> str:
        self.coin_history.append("checked owner")
        return self.owner

    def spend(self, amount: Decimal, allow_debt: bool = True) -> Callable[...]:
        def decorator(func: Callable):
            @wraps(func)
            def inner(*args, **kwargs):
                if amount > self.balance and not allow_debt:
                    self.coin_history.append(f"unsucessful payment at {func.__name__}")
                    return "you have no money"
                self.balance -= amount
                self.coin_history.append(f"spent {amount} at {func.__name__}.")
                return func(*args, spend=amount, name=self.name, **kwargs)
            return inner
        return decorator

    def receive(self, amount: Decimal) -> Callable[...]:
        def decorator(func: Callable):
            @wraps(func)
            def inner(*args, **kwargs):
                self.balance += amount
                self.coin_history.append(f"received {amount} at {func.__name__}.")
                return func(*args, amount=amount, name=self.name, **kwargs)
            return inner
        return decorator

    def add_request(self, request_name: str, mode: str, item_name: str, amount: Decimal, log: bool = False, allow_debt: bool = True):
        self.config["balance"] = self.balance
        if item_name == "balance" and self.balance < amount and not allow_debt:
            return "you have no money"
        self.balance -= amount
        self.coin_history.append(f"made a request at PengLink for {amount} {item_name}.")
        plink.add_request(
            request_name,
            self.name,
            mode,
            amount if item_name == "balance" else self.config[item_name],
            item_name,
            amount,
            "PenguinCoinBag",
            log
        )

    def accept_request(self, request_name: str, remove_request: bool = True, log: bool = False):
        result = plink.accept_request(
            request_name,
            self.name,
            log,
            remove_request
        )
        if result is None:
            return "it failed"

        if result[0] == "give":
            self.coin_history.append(f"accepted a request at PengLink; earned {result[1]} {result[2]}.")
            if result[2] == "balance":
                self.balance += result[1]
            else:
                self.config.update(result[4])
