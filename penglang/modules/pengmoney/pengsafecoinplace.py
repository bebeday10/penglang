from decimal import Decimal

from ... import penglang as pl
from . import pengmoneyerror as pme

class PenguinSafeCoinPlace:
    def __init__(self, storage: dict | None = None) -> None:
        self.storage: dict[str, dict[str, Decimal]] = storage or {
            "coins": {}
        }

    def deposit(self, log: bool = False, spend: Decimal = None, name: str = None):
        if spend is None or name is None:
            pl.say("please run through the spend command") if log else None
            raise pme.PenguinDepositError("Run through spend.")
        self.storage["coins"][name] = self.storage.get("coins", {}).get(name, 0) + spend

    def withdraw(self, log: bool = False, amount: Decimal = None, name: str = None):
        if amount is None or name is None:
            pl.say("please run through the receive command") if log else None
            raise pme.PenguinWithdrawError("Run through receive.")

        if self.storage.get("coins", {}).get(name, 0) < amount:
            pl.say("not enough money in the bank.")
            raise pme.PenguinWithdrawError("Not enough money is in the bank.")

        self.storage["coins"][name] = self.storage.get("coins", {}).get(name, 0) - amount
            