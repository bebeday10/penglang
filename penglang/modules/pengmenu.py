from dataclasses import dataclass
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from . import pengrandom as pr
from . import pengprint as pprint
from .. import penglang as pl
import asyncio as asy
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
    selection_penguin: bool = False
    disagreement_penguin: bool = False
    selection_penguin_amount: int = 1
    disagreement_penguin_amount: int = 1
    forbidden_penguin_amount: int = 1
    travellers_delay: float = 0
    random_travellers_delay: bool = False
    travel_amount: int = 1
    remove_evidence: bool = False
    random_forbidden_list: list | None = None
    key_echo: bool = False

    def __post_init__(self):
        self.food = self.food or []
        self.random_forbidden_list = self.random_forbidden_list or [
            "we see you. we do not care.",
            "what is that forbidden key. we will report to the police office next saturday at 5PM. make sure you remember this awful crime of one.",
            "no",
            "are you serious?",
            "why did you do that. we hate you now",
            "know your rules, buddy",
            "did you know you can press the arrow keys, enter, esc to do stuff?",
            "what does it mean to be like you",
            "thank you for not following instructions.",
            "we hope we know what you pressed. unfortunately we do not"
        ]

    @pl.multitask
    async def to_hungry_penguins(self):
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
                        current_selection = len(self.food) - self.travel_amount
                    else:
                        current_selection -= self.travel_amount
                    if self.beep:
                        print("\a", end="")
                    if self.selection_penguin:
                        pprint.penguin_speech_bubble(
                            f"you have chosen {self.food[current_selection]}",
                            speech_direction="^",
                            penguins=self.selection_penguin_amount
                        )

                elif key == readchar.key.DOWN:
                    if current_selection >= len(self.food) - self.travel_amount:
                        current_selection = 0
                    else:
                        current_selection += self.travel_amount
                    if self.beep:
                        print("\a", end="")
                    if self.selection_penguin:
                        pprint.penguin_speech_bubble(
                            f"you have chosen {self.food[current_selection]}",
                            speech_direction="^",
                            penguins=self.selection_penguin_amount
                        )
                elif key == readchar.key.ENTER or key == readchar.key.ENTER_2:
                    if self.remove_evidence:
                        l.update("(Evidence has been removed.)", refresh=True)
                    break

                elif key == readchar.key.ESC or key == readchar.key.ESC_2:
                    if self.remove_evidence:
                        l.update("(Evidence has been removed.)", refresh=True)
                    if self.disagreement_penguin:
                        pprint.penguin_speech_bubble(
                            f"you profusely disagree to the menu. they will hear about this",
                            speech_direction="^",
                            penguins=self.disagreement_penguin_amount
                        )
                    return "The penguin profusely disagreed to your menu."
                else:
                    pprint.penguin_speech_bubble(
                        pr.random_decision(*self.random_forbidden_list),
                        speech_direction="^",
                        penguins=self.forbidden_penguin_amount
                    )
                if self.random_travellers_delay:
                    await asy.sleep(pr.random_decimal(0, self.travellers_delay))
                else:
                    await asy.sleep(self.travellers_delay)
                if self.key_echo:
                    pprint.penguin_speech_bubble(
                        f"you said {key}",
                        speech_direction="^",
                        penguins=self.selection_penguin_amount
                    )
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
                            confirm_selection -= self.travel_amount
                    elif confirm_key == readchar.key.DOWN:
                        if confirm_selection >= len(confirm_list) - 1:
                            confirm_selection = 0
                        else:

                            confirm_selection += self.travel_amount
                    elif confirm_key == readchar.key.ENTER or confirm_key == readchar.key.ENTER_2:
                        if confirm_selection == 0:
                            break
                        else: return "The penguin profusely disagreed to your menu."

                    elif confirm_key == readchar.key.ESC or confirm_key == readchar.key.ESC_2:
                        return "The penguin profusely disagreed to your menu."

                    p.update(Panel(prompt, title="Confirmation", border_style="red"), refresh=True)

        return self.food[current_selection]

