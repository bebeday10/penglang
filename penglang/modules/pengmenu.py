from dataclasses import dataclass
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from . import pengrandom as pr

import readchar

@dataclass
class PenguinMenu:
    restaurant: str
    food: list | None = None
    subtitle: str | None = None
    color: str = "white"
    waiter: bool = False
    recommend: str | None = None
    michelin_penguin: int | None = None
    hungry_penguins: int = 0
    special: bool = False
    special_item: None | str = None
    confirmations: int = 0
    random_start: bool = False
    beep: bool = False

    def __post_init__(self):
        self.food = self.food or []

    def to_hungry_penguins(self):
        current_selection = 0
        if self.random_start:
            current_selection = pr.random_number(0, (len(self.food) - 1))
        with Live(refresh_per_second=10) as l:
            while True:
                t = Text()
                if self.subtitle is not None:
                    t.append(self.subtitle, "bold")
                    t.append("\n\n")
                if self.michelin_penguin:
                    t.append(f"This place has earned: {"🐧"*self.michelin_penguin} michelin penguins.")
                    t.append("\n\n")
                for dish in self.food:
                    if self.food[current_selection] == dish:
                        t.append(f"> {dish}")
                    else:
                        t.append(f"  {dish}")
                    t.append("\n")

                if self.special:
                    t.append("\n\n")
                    t.append(f"{"Today's Special":{"-"}^40}")
                    t.append("\n")
                    t.append(f"The special for today: {self.special_item}")
                    t.append("\n")
                    t.append("Get it before stocks go out!")

                if self.hungry_penguins:
                    t.append("\n\n")
                    t.append(f"Do Not Hold The Line. There Are {self.hungry_penguins} Hungry Penguins Behind You.")

                if self.recommend:
                    t.append("\n\n")
                    t.append(f"The Waiter Recommends: {self.recommend}, But They Are Not Liable For Any Damages.")

                if self.waiter:
                    t.append("\n\n")
                    t.append("↕ Travel  ↳ Consent to This Item  Esc Disagree Profusely")
                l.update(Panel(t, title=self.restaurant, border_style=self.color), refresh=True)
                key = readchar.readkey()

                if key == readchar.key.UP:
                    if current_selection <= 0:
                        current_selection = len(self.food) - 1
                    else:
                        current_selection -= 1
                    if self.beep:
                        print("\a", end="")

                elif key == readchar.key.DOWN:
                    if current_selection >= len(self.food) - 1:
                        current_selection = 0
                    else:
                        current_selection += 1
                    if self.beep:
                        print("\a", end="")
                elif key == readchar.key.ENTER or key == readchar.key.ENTER_2:

                    break

                elif key == readchar.key.ESC or key == readchar.key.ESC_2:
                    return "The penguin profusely disagreed to your menu."
                
                l.update(Panel(t, title=self.restaurant, border_style=self.color), refresh=True)

        for confirms in range(self.confirmations):
            with Live(refresh_per_second=5) as p:
                confirm_selection = 0
                confirm_list = ["I Am Willing To Confirm To This Item", "Profusely Not"]
                while True:

                    prompt = Text()
                    prompt.append("Are You Sure To Consent?")
                    prompt.append("\n\n")
                    for i in confirm_list:
                        if confirm_list[confirm_selection] == i:
                            prompt.append(f"> {i}")
                        else:
                            prompt.append(f"  {i}")
                        prompt.append("\n")
                    p.update(Panel(prompt, title="Confirmation", border_style="red"), refresh=True)
                    confirm_key = readchar.readkey()
                    if confirm_key == readchar.key.UP:
                        if confirm_selection <= 0:
                            confirm_selection = len(confirm_list) - 1
                        else:
                            confirm_selection -= 1
                    elif confirm_key == readchar.key.DOWN:
                        if confirm_selection >= len(confirm_list) - 1:
                            confirm_selection = 0
                        else:

                            confirm_selection += 1
                    elif confirm_key == readchar.key.ENTER or confirm_key == readchar.key.ENTER_2:
                        if confirm_selection == 0:
                            break
                        else: return "The penguin profusely disagreed to your menu."

                    elif confirm_key == readchar.key.ESC or confirm_key == readchar.key.ESC_2:
                        return "The penguin profusely disagreed to your menu."

                    p.update(Panel(prompt, title="Confirmation", border_style="red"), refresh=True)

        return self.food[current_selection]

