"""
# PengVending

The module for vending machines

## Features:
    a penguin vending machine
"""

# a vending machine for penglang
# it's literally just a vending machine class.
# this is unserious and not meant to be taken seriously.

from typing import Literal, LiteralString

from .penglink.hubs import vending as plink


class PenguinVendingMachine:
    """
    ## PenguinVendingMachine

    The first machine in PengLang.

    ### Features:
        purchasing
        restocking
        adding and accepting requests from PengLink
        make new items
        change prices
        show the inventory
        dsplaying the total sales

    Supports PengLink.
    """
    def __init__(self, inventory: dict, name="vending machine"):
        """
        vending machine

        Args:
            inventory (dict): make sure to format the inventory like this:
            {
                "item_name": {
                    "price": 1.00,
                    "quantity": 10
                },
                "another_item": {
                    "price": 2.50,
                    "quantity": 5
                }
            }
            thank you for your cooperation
        """
        self.inventory = inventory
        self.total_sales = 0
        self.name = name

    def purchase(self, item_name: str, money: float, give_back_change: str = None):
        """
        purchase an item from the vending machine's inventory.

        Args:
            item_name (str): the item's name
            money (float): the money you have
            give_back_change (str, optional): the place to give back the change. Defaults to None.

        Returns:
            str: the result
        """

        if not item_name in self.inventory:
            return "Item not found."

        item = self.inventory[item_name]
        price = item["price"]
        quantity = item["quantity"]

        if quantity <= 0:
            return "Item out of stock."

        if money < price:
            return f"Not enough money. {item_name} costs ${price:.2f}."

        # Process the purchase
        self.inventory[item_name]["quantity"] -= 1
        self.total_sales += price
        change = money - price
        change = round(change, 2)
        if give_back_change:
            globals()[give_back_change] = globals().get(give_back_change, 0) + change
        return f"Purchased {item_name}. Change: ${change:.2f}."

    def restock(self, item_name: str, quantity: int):
        """
        restock items in the vending machine.

        Args:
            item_name (str): the name of the item
            quantity (int): the quantity of the item

        Returns:
            str: the results.
        """
        if item_name not in self.inventory:
            return "Item not found."

        self.inventory[item_name]["quantity"] += quantity
        return f"Restocked {item_name}. New quantity: {self.inventory[item_name]['quantity']}."

    def add_request(self, mode: str, request_name: str, item_name: str, amount: int, log: bool = False) -> None | Literal['Item not found.'] | Literal['Unsufficit amount.']:
        """
        add a request to PengLink.

        Args:
            mode (str): the mode
            request_name (str): the request's name
            item_name (str): the name of the item
            amount (int): the amount of the item.
            log (bool): whether to log or not. Defaults to False.

        Returns:
            None | str: the result of sucess. returns None if went well.
        """
        if self.inventory.get(item_name) is None:
            return "Item not found."
        if self.inventory.get(item_name, {}).get("quantity", 0) < amount:
            return "Unsufficit amount."

        plink.add_request(request_name, self.name, mode, self.inventory.get(item_name, {}), amount=amount, internal_name="PenguinVendingMachine", log=log, item_name=item_name)

    def accept_request(self, request_name, remove_request: bool = True, log: bool = False, overwrite: bool = False) -> str | None:
        """
        accept a request from PengLink.

        Args:
            request_name (str): the request name
            remove_request (bool, optional): whether to remove the request. Defaults to True.
            log (bool, optional): whether to log or not. Defaults to False.
            overwrite (bool, optional): whether to overwrite or not, used to ensure metadata. Defaults to False.

        Returns:
            str | None: the result of success, returns None if went correctly.
        """
        result = plink.accept_request(request_name, self.name, log, remove_request)

        if result is None:
            return "Request not found."

        if result[0] == "give":
            if overwrite:
                self.inventory.update(result[4])
            elif self.inventory.get(result[2]) is None:
                self.inventory.update(result[1])
                return f"Got {result[2]}."

            else:
                self.inventory[result[2]]["quantity"] = self.inventory.get(result[2], {}).get("quantity", 0) + result[3]

        elif result[0] == "share recipe":
            if overwrite:
                self.inventory.update(result[4])
            elif self.inventory.get(result[3]) is None:
                self.inventory.update(result[1])
                return f"Got {result[3]}."
            else:
                self.inventory[result[3]]["supplies"] = result[2]

    def new_item(self, item_name: str, price: float, quantity: int):
        """
        make a new item for the vending machine.

        Args:
            item_name (str): the item's name
            price (float): the price
            quantity (int): the amount of the item.

        Returns:
            str: the result of success.
        """
        if item_name in self.inventory:
            return "Item already exists."

        self.inventory[item_name] = {
            "price": price,
            "quantity": quantity
        }
        return f"Added new item: {item_name} with price ${price:.2f} and quantity {quantity}."

    def change_price(self, item_name: str, new_price: float):
        """
        change the price of an item in the vending machine.

        Args:
            item_name (str): the item's name
            new_price (float): the new price.

        Returns:
            str: the result.
        """
        if item_name not in self.inventory:
            return "Item not found."

        self.inventory[item_name]["price"] = new_price
        return f"Changed price of {item_name} to ${new_price:.2f}."

    def display_inventory(self) -> LiteralString:
        """
        display the inventory.

        Returns:
            LiteralString: the inventory
        """
        inventory_list = []
        for item_name, details in self.inventory.items():
            inventory_list.append(f"{item_name}: ${details['price']:.2f} ({details['quantity']} in stock)")
        return "\n".join(inventory_list)

    # what else could a vending machine do? I can't think of anything else.
    # maybe it could have a method to remove an item from the inventory? but that seems a bit excessive for a vending machine.
    # total sales is a idea.

    def display_total_sales(self):
        """
        get the total sales. useful to calculate earnings, and get deadline requirements.

        Returns:
            int: the sales
        """
        return self.total_sales

    def __str__(self):
        """
        when it is printed.

        Returns:
            str: the thing to print.
        """
        return f"a vending machine named {self.name}, has {f", ".join(i for i in list(self.inventory)) if self.inventory else "no items"}"
