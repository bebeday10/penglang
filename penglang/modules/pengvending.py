# a vending machine for penglang
# it's literally just a vending machine class.
# this is unserious and not meant to be taken seriously.

class PenguinVendingMachine:
    def __init__(self, inventory: dict):
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

    def purchase(self, item_name: str, money: float, give_back_change: str=None):

        
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
        change = money - price
        change = round(change, 2)
        if give_back_change:
            globals()[give_back_change] = globals().get(give_back_change, 0) + change
        return f"Purchased {item_name}. Change: ${change:.2f}."
    

    def restock(self, item_name: str, quantity: int):
        if item_name not in self.inventory:
            return "Item not found."
        
        self.inventory[item_name]["quantity"] += quantity
        return f"Restocked {item_name}. New quantity: {self.inventory[item_name]['quantity']}."
    
    def new_item(self, item_name: str, price: float, quantity: int):
        if item_name in self.inventory:
            return "Item already exists."
        
        self.inventory[item_name] = {
            "price": price,
            "quantity": quantity
        }
        return f"Added new item: {item_name} with price ${price:.2f} and quantity {quantity}."
    

    def change_price(self, item_name: str, new_price: float):
        if item_name not in self.inventory:
            return "Item not found."
        
        self.inventory[item_name]["price"] = new_price
        return f"Changed price of {item_name} to ${new_price:.2f}."
    
    def display_inventory(self):
        inventory_list = []
        for item_name, details in self.inventory.items():
            inventory_list.append(f"{item_name}: ${details['price']:.2f} ({details['quantity']} in stock)")
        return "\n".join(inventory_list)
    
    # what else could a vending machine do? I can't think of anything else.
    # maybe it could have a method to remove an item from the inventory? but that seems a bit excessive for a vending machine.
    # total sales is a idea.

    def display_total_sales(self):
        return self.total_sales