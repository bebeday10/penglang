"""
# PengCoffee

PengCoffee: drink and brew coffee

Supported with *PengLink*
"""

# coffee machine
import asyncio as asy
import random as r
from .. import penglang as pl
from . import pengvending as pv
from .penglink.hubs import coffee as plink
from . import pengdecorator as pd


def auto_async(func):
    def wrapper(*args, **kwargs):
        return asy.run(func(*args, **kwargs))

    return wrapper


class PenguinCoffeeMachine:
    """
    the coffee machine
    """
    def __init__(self, inventory: dict, supplies: dict = None, name: str = "coffee machine", speed: int = 60, vendinglink: pv.PenguinVendingMachine = None, autosend: bool = False):
        """
        a coffee machine

        Args:
            inventory (dict): the preset coffee in your coffee machine. follow:
            {
                "coffee": {
                    "amount": int,
                    "supplies": {
                        "item": amount
                        "another": amount
                        }
                    "price": float (optional)
                    },
                "another": {
                    "amount": int,
                    "supplies": {
                        "item": amount
                        "another": amount
                        }
                    "price": float (optional)
                    }
            }
            supplies (dict): the preset supplies in your coffee machine. follow:
            {
                "item": amount
                "another": amount
            }
            speed (int, optional): speed in seconds of coffee making time. Defaults to 60.
            vendinglink (PenguinVendingMachine): link the coffee machine to a vending machine.
            autosend (bool): automatically send coffee to the vending machine.
        """
        self.inventory = inventory
        self.name = name
        self.speed = speed
        self.supplies = supplies or {}
        self.vendinglink: pv.PenguinVendingMachine = vendinglink
        self.autosend = autosend

    @pd.penguin_deprecation("v0.6.0", "v0.8.0", "Use add_request.", "send_to_vending")
    def send_to_vending(self, log: bool = False):
        # formally known as sendto_Vending 🥹☕
        if not self.vendinglink:
            pl.say("you have no vending machine linked.") if log else None
            return "No vending machines are linked."

        for item, _ in self.inventory.items():
            item_in_vending = self.vendinglink.inventory.get(item)
            if item_in_vending == None:
                item_in_vending = {}
                item_in_vending["price"] = round(r.uniform(6, 9) * 20) / 20
                item_in_vending["quantity"] = 0

            item_in_vending["quantity"] += self.inventory[item]["amount"]
            self.inventory[item]["amount"] = 0
            self.vendinglink.inventory[item] = item_in_vending

        return f"Finished sending coffees to {pv.PenguinVendingMachine}."

    def add_request(self, mode: str, request_name: str, coffee: str, amount: int, log: bool = False):
        """
        add a request

        Args:
            mode (str): the mode
            request_name (str): the name of the request
            coffee (str): the coffee to select
            amount (int): the amount of the coffee
            log (bool, optional): whether to log or not. Defaults to False.

        Returns:
            _type_: _description_
        """
        if self.inventory.get(coffee) is None:
            pl.say("[bold blue]coffee doesn't exist[/bold blue]") if log else None
            return "Coffee doesn't exist"

        if self.inventory.get(coffee, {}).get("amount", 0) < amount:
            pl.say("you don't have that much coffees") if log else None
            return "Not enough coffees"

        plink.add_request(request_name, self.name, mode, self.inventory.get(coffee), coffee, amount, "PenguinCoffeeMachine", log)

    def accept_request(self, request_name, remove_request=True, log=False, overwrite: bool = False) -> None | str:
        """
        accept a request from PengLink

        Args:
            request_name (str): the name of the request
            remove_request (bool, optional): whether to remove the request. Defaults to True.
            log (bool, optional): whether to log or not. Defaults to False.
            overwrite (bool, optional): whether to overwrite the item. this can preserve metadata more. Defaults to False.

        Returns:
            None | str: what you got
        """
        result = plink.accept_request(request_name, "PenguinCoffeeMachine", log, remove_request)

        if result is None:
            pl.say("failed") if log else None
            return None

        if result[0] == "give":
            if overwrite:
                self.inventory.update(result[4])
            elif self.inventory.get(result[1], None) is None:
                self.inventory.update(result[3])
                pl.say(f"got {result[1]}.") if log else None
                return f"Got {result[1]}."
            else:
                self.inventory[result[1]]["amount"] = self.inventory.get(result[1], {}).get("amount", 0) + result[2]

        elif result[0] == "share recipe":
            if overwrite:
                self.inventory.update(result[4])
            else:
                if self.inventory.get(result[3], None) is None:
                    self.inventory.update(result[1])

                else:
                    self.inventory[result[3]]["supplies"] = result[1]

    @auto_async
    async def make_coffee(self, typeofcoffee: str, log: bool = False):
        """
        make some coffee to drink

        Args:
            typeofcoffee (str): the type of coffee you want to make
            log (bool, optional): whether to log or not. Defaults to False.

        Returns:
            str | int: if the thing failed, or the amount of that coffee you have.
        """
        if self.inventory.get(typeofcoffee) == None:
            pl.say("[bold cyan]that coffee doesn't exist![/bold cyan]") if log else None
            return "Coffee doesn't exist."

        suppliesneeded: dict = self.inventory[typeofcoffee]["supplies"]

        for itemneeded, amountneeded in suppliesneeded.items():
            currentsupplies = self.supplies.get(itemneeded, 0)
            if currentsupplies < amountneeded:
                pl.say(f"[bold bright_red]don't have the supplies: [italic]{itemneeded}[/italic], need [/bold bright_red]{amountneeded}[bold bright_red].[/bold bright_red]") if log else None
                return "Don't have the supplies."
        else:
            for item, amount in suppliesneeded.items():
                currentsupplies = self.supplies.get(item, 0)
                self.supplies[item] -= amount

        pl.say(f"wait {self.speed} seconds to get {typeofcoffee}.") if log else None
        await asy.sleep(self.speed)  # wait the time of coffee making

        self.inventory[typeofcoffee]["amount"] = self.inventory[typeofcoffee].get("amount", 0) + 1

        self.send_to_vending() if self.autosend and self.vendinglink else None

        pl.say(f"{self.name} has made {typeofcoffee}. there are now {self.inventory.get(typeofcoffee, 0).get("amount", 0)} {typeofcoffee}s.") if log else None

        return self.inventory.get(typeofcoffee, 0)

    def drink_coffee(self, coffee: str, log: bool = False) -> str:
        """
        dirk some coffee in your inventory.

        Args:
            coffee (str): the coffee you want to drink
            log (bool, optional): whether you want to log it or not. Defaults to False.

        Returns:
            str: the results.
        """
        if coffee not in self.inventory:
            pl.say(f"that coffee doesn't exist.") if log else None
            return "Doesn't exist."

        elif self.inventory[coffee]["amount"] == 0:
            pl.say("you don't have that coffee.") if log else None
            return "Don't have."

        self.inventory[coffee]["amount"] -= 1

        pl.say(f"drank {coffee}. {coffee} now has {self.inventory[coffee]["amount"]}.")

        return f"drank {coffee}. {coffee} now has {self.inventory[coffee]["amount"]}."

    def insert_supplies(self, supply: str, amount: int, log: bool = False) -> str:
        """
        restock supplies to make more coffee.

        Args:
            supply (str): the supply to stock
            amount (int): the amount to stock
            log (bool, optional): whether to log it or not. Defaults to False.

        Returns:
            str: the result.
        """
        pl.say("penguin is suppling the machine...") if log else None

        self.supplies[supply] = self.supplies.get(supply, 0) + amount

        pl.say(f"supplied {amount} {supply}s") if log else None

        return f"Supplied {amount} {supply}s."

    def new_coffee(self, typeofcoffee, price: float = round(r.uniform(6, 9) * 20) / 20, suppliesneeded: dict = {}, log: bool = False) -> str:
        """
        make a new coffee.

        Args:
            typeofcoffee (str): the coffee you want to make
            price (float, optional): the price of the coffee. Defaults to round(r.uniform(6, 9) * 20)/20.
            suppliesneeded (dict, optional): the supplies needed. Defaults to {}.
            log (bool, optional): whether to log or not. Defaults to False.

        Returns:
            str: the result.
        """
        if typeofcoffee in self.inventory:
            pl.say("coffee already exists") if log else None
            return f"{typeofcoffee} already exists."

        self.inventory[typeofcoffee] = {
            "supplies": suppliesneeded,
            "amount": 0,
            "price": price
        }

        pl.say(f"{typeofcoffee} made.")

        return f"{typeofcoffee} has been made."

    def display_inventory(self, log: bool = True, mode: str = "normal"):
        """
        display the inventory. this may be useful to get metadata from the inventory, or to show the player the inventory.

        Args:
            log (bool, optional): whether to log it or not. Defaults to True.
            mode (str, optional): the mode. can be either "normal" or "dev". Defaults to "normal".

        Returns:
            LiteralString | dict | None: the inventory
        """
        inventory_list = []

        if mode == "normal":

            for item_name, details in self.inventory.items():
                inventory_list.append(f"{item_name}: {details["amount"]} ({" | ".join(f"{k}: {v}" for k, v in details["supplies"].items())})")

            pl.say("\n".join(inventory_list)) if log else None

            return "\n".join(inventory_list)

        elif mode == "dev":
            pl.say(self.inventory) if log else None
            return self.inventory

    def display_supplies(self, log: bool = True, mode: str = "normal"):
        """
        display the supplies. may be useful to show the player the supplies.

        Args:
            log (bool, optional): whether to log or not. Defaults to True.
            mode (str, optional): the mode. can be either "normal" or "dev". Defaults to "normal".

        Returns:
            LiteralString | dict | None: the supplies
        """
        supplies_list: list = []
        if mode == "normal":

            for supply, amount in self.supplies.items():
                supplies_list.append(f"{supply}: {amount}")

            pl.say("\n".join(supplies_list)) if log else None

            return "\n".join(supplies_list)

        elif mode == "dev":
            pl.say(self.supplies) if log else None

            return self.supplies
        
    def change_recipe(self, coffee: str, recipe: dict[str, int], log: bool = False):
        """
        change the recipe

        Args:
            coffee (str): the coffee to change
            recipe (dict[str, int]): the recipe to change
            log (bool, optional): whether to log or not. Defaults to False.

        Returns:
            dict | str: the coffee.
        """
        if coffee not in self.inventory:
            pl.say(f"that coffee doesn't exist.") if log else None
            return "Doesn't exist."
        
        self.inventory[coffee]["supplies"] = recipe
        pl.say(f"coffee machine has now changed {coffee}'s recipe.") if log else None
        return self.inventory[coffee]
        

    @pd.penguin_deprecation("v0.6.0", "v0.8.0", "Use add_request.", "link_PenguinVendingMachine")
    def link_PenguinVendingMachine(self, vending_machine: pv.PenguinVendingMachine, log: bool = False):
        self.vendinglink = vending_machine
        self.send_to_vending() if self.autosend else None
        pl.say(f"vending machine {vending_machine} linked.") if log else None
        return f"Linked {vending_machine}."

    def __str__(self):
        return f"a coffee machine named {self.name}, makes a coffee per {self.speed}, currently {f"linked by '{self.vendinglink}'" if self.vendinglink else "not linked"}, has {", ".join(i for i in list(self.inventory))}"
