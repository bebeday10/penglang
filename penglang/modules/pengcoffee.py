# coffee machine
import asyncio as asy
import random as r
from .. import penglang as pl
from . import pengvending as pv

def auto_async(func):
    def wrapper(*args, **kwargs):
        return asy.run(func(*args, **kwargs))
    
    return wrapper

class PenguinCoffeeMachine:
    def __init__(self, inventory: dict, supplies: dict ={}, name: str ="coffee machine", speed: int =60, vendinglink: pv.PenguinVendingMachine=None, autosend: bool =False):
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
                    },
                "another": {
                    "amount": int,
                    "supplies": {
                        "item": amount
                        "another": amount
                        }
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
        self.supplies = supplies
        self.vendinglink: pv.PenguinVendingMachine = vendinglink
        self.autosend = autosend

    def send_to_vending(self, log: bool =False):
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
                
            
    @auto_async
    async def make_coffee(self, typeofcoffee: str, log: bool =False):
        if self.inventory.get(typeofcoffee) == None:
            pl.say("that coffee doesn't exist!") if log else None
            return "Coffee doesn't exist."

        suppliesneeded: dict = self.inventory[typeofcoffee]["supplies"]

        for itemneeded, amountneeded in suppliesneeded.items():
            currentsupplies = self.supplies.get(itemneeded, 0)
            if currentsupplies < amountneeded:
                pl.say(f"don't have the supplies: {itemneeded}, need {amountneeded}.") if log else None
                return "Don't have the supplies."
        else:
            for item, amount in suppliesneeded.items():
                currentsupplies = self.supplies.get(item, 0)
                self.supplies[item] -= amount
            
        pl.say(f"wait {self.speed} seconds to get {typeofcoffee}.") if log else None
        await asy.sleep(self.speed) # wait the time of coffee making

        self.inventory[typeofcoffee]["amount"] = self.inventory[typeofcoffee].get("amount", 0) + 1

        self.send_to_vending() if self.autosend and self.vendinglink else None

        pl.say(f"{self.name} has made {typeofcoffee}. there are now {self.inventory.get(typeofcoffee, 0).get("amount", 0)} {typeofcoffee}s.") if log else None

        return self.inventory.get(typeofcoffee, 0)

    def drink_coffee(self, coffee: str, log: bool =False):
        if coffee not in self.inventory:
            pl.say(f"that coffee doesn't exist.") if log else None
            return "Doesn't exist."
        
        elif self.inventory[coffee]["amount"] == 0:
            pl.say("you don't have that coffee.") if log else None
            return "Don't have."
        
        self.inventory[coffee]["amount"] -= 1

        pl.say(f"drank {coffee}. {coffee} now has {self.inventory[coffee]["amount"]}.")

        return f"drank {coffee}. {coffee} now has {self.inventory[coffee]["amount"]}."
    
    def insert_supplies(self, supply: str, amount: int, log: bool =False):
        pl.say("penguin is suppling the machine...") if log else None

        self.supplies[supply] = self.supplies.get(supply, 0) + amount

        pl.say(f"supplied {amount} {supply}s") if log else None

        return f"Supplied {amount} {supply}s."
    
    def new_coffee(self, typeofcoffee, suppliesneeded: dict ={}, log: bool =False):
        if typeofcoffee in self.inventory:
            pl.say("coffee already exists") if log else None
            return f"{typeofcoffee} already exists."
        
        self.inventory[typeofcoffee] = {
            "supplies": suppliesneeded,
            "amount": 0
        }

        pl.say(f"{typeofcoffee} made.")

        return f"{typeofcoffee} has been made."
    
    def display_inventory(self, log: bool =True):
        inventory_list = []

        for item_name, details in self.inventory.items():
            inventory_list.append(f"{item_name}: {details["amount"]} ({" | ".join(f"{k}: {v}" for k, v in details["supplies"].items())})")

        pl.say("\n".join(inventory_list)) if log else None

        return "\n".join(inventory_list)

    
    def link_PenguinVendingMachine(self, vending_machine: pv.PenguinVendingMachine, log: bool =False):
        self.vendinglink = vending_machine
        self.send_to_vending() if self.autosend else None
        pl.say(f"vending machine {vending_machine} linked.") if log else None
        return f"Linked {vending_machine}."




