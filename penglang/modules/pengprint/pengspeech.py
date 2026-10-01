import textwrap as tw
from ... import penglang as pl
from typing import Literal

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