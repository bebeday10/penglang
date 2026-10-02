import textwrap as tw
from ... import penglang as pl
from typing import Literal
import unicodedata as ud
from .. import pengstring as ps
from rich.live import Live
import asyncio as asy
from rich.text import Text

def better_say(*message, end="\n", seperator="", flush: bool = False, inspection: bool = True):
    """
    say, but with more options.

    Args:
        *message (str): the message.
        end (str, optional): the ending of the say. useful for seperating. Defaults to "\\n".
        seperator (str, optional): the seperator between each message. useful for seperating. Defaults to "".
        flush (bool, optional): whether to force refresh the terminal. Defaults to False.
        inspection (bool, optional): inspect the message. Defaults to True.
    """
    if inspection:
        print(*message, end=end, sep=seperator, flush=flush)
    else:
        message = [str(piece) for piece in message]
        print(*message, end=end, sep=seperator, flush=flush)

def penguin_speech_bubble(speech: str, bubble_size: int = 28, speech_direction: Literal[">", "<", "^"] = "<", penguins: int = 1, penguin_looks: str = "🐧"):
    lines = tw.wrap(
        speech,
        bubble_size
    )
    pl.say(" " + "_" * (bubble_size + 2))
    for line in lines:
        pl.say(f"| {line:{speech_direction}{bubble_size}} |")

    pl.say(" " + "-" * (bubble_size + 2))
    pl.say("        \\")
    pl.say("         " + f"{penguin_looks}"*penguins)

def penguin_side_speech_bubble(speech: str, bubble_size: int = 28, speech_direction: Literal[">", "<", "^"] = "<", penguins: int = 1, penguin_looks: str = "🐧"):
    lines = tw.wrap(
        speech,
        bubble_size
    )
    penguin_len = len(penguin_looks)
    for letter in penguin_looks:
        if ud.east_asian_width(letter) == "W":
            penguin_len += 1
    
    pl.say(f"{penguin_looks}</" + "‾" * (bubble_size + 2) + "\\")
    penguins -= 1
    for line in lines:
        if penguins >= 1:
            pl.say(f"{penguin_looks} | {line:{speech_direction}{bubble_size}} |")
            penguins -= 1
        else:
            pl.say((" "*penguin_len) + f" | {line:{speech_direction}{bubble_size}} |")
    if penguins >= 1:
        pl.say(f"{penguin_looks} \\" + "_" * (bubble_size + 2) + "/")
    else:
        pl.say(f"{" " * penguin_len} \\" + "_" * (bubble_size + 2) + "/")
    if penguins >= 1:
        for penguin in range(penguins):
            pl.say(penguin_looks)

def penguin_speech_bubble_no_ice(speech: str, bubble_size: int = 28, speech_direction: Literal[">", "<", "^"] = "<", penguins: int = 1, penguin_looks: str = "🐧"):
    lines = tw.wrap(
        speech,
        bubble_size
    )
    to_return = ""
    to_return += ps.add_new_line(" " + "_" * (bubble_size + 2))
    for line in lines:
        to_return += ps.add_new_line(f"| {line:{speech_direction}{bubble_size}} |")

    to_return += ps.add_new_line(" " + "-" * (bubble_size + 2))
    to_return += ps.add_new_line("        \\")
    to_return += ps.add_new_line("         " + f"{penguin_looks}"*penguins)
    return to_return

def penguin_side_speech_bubble_no_ice(speech: str, bubble_size: int = 28, speech_direction: Literal[">", "<", "^"] = "<", penguins: int = 1, penguin_looks: str = "🐧"):
    lines = tw.wrap(
        speech,
        bubble_size
    )
    penguin_len = len(penguin_looks)
    for letter in penguin_looks:
        if ud.east_asian_width(letter) == "W":
            penguin_len += 1
    to_return = ""
    to_return += ps.add_new_line(f"{penguin_looks}</" + "‾" * (bubble_size + 2) + "\\")
    penguins -= 1
    for line in lines:
        if penguins >= 1:
            to_return += ps.add_new_line(f"{penguin_looks} | {line:{speech_direction}{bubble_size}} |")
            penguins -= 1
        else:
            to_return += ps.add_new_line((" "*penguin_len) + f" | {line:{speech_direction}{bubble_size}} |")
    if penguins >= 1:
        to_return += ps.add_new_line(f"{penguin_looks} \\" + "_" * (bubble_size + 2) + "/")
    else:
        to_return += ps.add_new_line(f"{" " * penguin_len} \\" + "_" * (bubble_size + 2) + "/")
    if penguins >= 1:
        for penguin in range(penguins):
            to_return += ps.add_new_line(penguin_looks)

    return to_return

@pl.multitask
async def penguin_speech_bubble_typewrite(speech: str, bubble_size: int = 28, speech_direction: Literal[">", "<", "^"] = "<", penguins: int = 1, penguin_looks: str = "🐧", delay=0.05):
    with Live(refresh_per_second=60) as l:
        for i, letter in enumerate(speech):
            l.update(penguin_speech_bubble_no_ice(speech[:i], bubble_size, speech_direction, penguins, penguin_looks), refresh=True)
            await asy.sleep(delay)

@pl.multitask
async def penguin_side_speech_bubble_typewrite(speech: str, bubble_size: int = 28, speech_direction: Literal[">", "<", "^"] = "<", penguins: int = 1, penguin_looks: str = "🐧", delay=0.05):
    with Live(refresh_per_second=30) as l:
        for i, letter in enumerate(speech):
            l.update(penguin_side_speech_bubble_no_ice(speech[:i], bubble_size, speech_direction, penguins, penguin_looks), refresh=True)
            await asy.sleep(delay)
