import penglang as pl
import penglang.modules.pengmenu as pm

choices = pm.PenguinMenu(
    restaurant="Shopping list 🏪🛒",
    food=[
        "add something",
        "remove something",
        "exit",
        "view",
        "clear"
    ],
    waiter=True,
    recommend="adding banana",
    michelin_penguin=2,
    color="green"
)
shopping_list = []

while True:
    choice = choices.to_hungry_penguins()
    if choice == "add something":
        to_add = pl.penguin_ask("add: ")
        shopping_list.append(to_add)
    elif choice == "remove something":
        to_remove = pl.penguin_ask("remove: ")
        try:
            shopping_list.remove(to_remove)
        except ValueError:
            pl.say("it is not there")

    elif choice == "exit" or choice == "The penguin profusely disagreed to your menu.":
        pl.say("finished shop")
        break
    elif choice == "view":
        for i, item in enumerate(shopping_list, 1):
            pl.say(f"{i}: {item}")

    elif choice == "clear":
        pl.say("it gone.")
        shopping_list = []