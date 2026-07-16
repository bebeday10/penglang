from .. import pengcoffee as pc
from .. import pengvending as pv
from ... import penglang as pl
import random as r

class PenguinCoffeeMachine(pc.PenguinCoffeeMachine):
    def __init__(self, inventory, supplies = None, name = "coffee machine", speed = 60, vendinglink = None, autosend = False):
        super().__init__(inventory, supplies, name, speed, vendinglink, autosend)

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


    def link_PenguinVendingMachine(self, vending_machine: pv.PenguinVendingMachine, log: bool = False):
        self.vendinglink = vending_machine
        self.send_to_vending() if self.autosend else None
        pl.say(f"vending machine {vending_machine} linked.") if log else None
        return f"Linked {vending_machine}."