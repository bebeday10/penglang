"""
# PengPrint

*PengPrint*: Print nicely, stylish, and presentation.

# Features:
    ## Boxes:
        emergency box
        info box
        warning box
    ## Typewriters:
        typewrite
        multitask typewrite
    ## Say:
        better say
"""

from .. import penglang as pl
import time as t
from rich import print

def emergency_box(message, title="🚨 EMERGENCY 🚨",):
    """
    make an emergency. Useful when you need to emergent the user.

    Args:
        message (str): the emergency message
        title (str, optional): the title of the emergency. Defaults to "🚨 EMERGENCY 🚨".
    """
    pl.say_in_a_box(f"[bold bright_red]{message}[/bold bright_red]", title, "bold bright_red")

def info_box(message, title="Info ℹ️",):
    """
    make an info box. useful when you need to tell the user some info.

    Args:
        message (str): the info message
        title (str, optional): the title of the info box. Defaults to "Info ℹ️".
    """
    pl.say_in_a_box(f"[bold cyan]{message}[/bold cyan]", title, "bold cyan")

def warning_box(message, title="⚠️  Warning ⚠️",):
    """
    make a warning box. useful when you want to warn the user.

    Args:
        message (str): the warning message
        title (str, optional): the title of the warning. Defaults to "⚠️  Warning ⚠️".
    """
    pl.say_in_a_box(f"[bold yellow]{message}[/bold yellow]", title, "bold yellow")

def typewrite(*message, delay: float = 0.05, pause: bool = True, spacing: bool = True):
    """
    typewrite something.

    Args:
        *message (str): the message.
        delay (float, optional): the delay between letters. Defaults to 0.05.
        pause (bool, optional): whether to pause or not. Defaults to True.
        spacing (bool, optional): whether to space out or not. useful for seperating. Defaults to True.
    """
    for piece in message:
        for char in piece:
            print(char, end='', flush=True)
            t.sleep(delay)

    if spacing:
        print()

    if pause:
        t.sleep(1)

@pl.multitask
async def multitask_typewrite(*message, delay: float = 0.05, spacing: bool = True):
    """
    typewrite something without using everything up.

    Args:
        *message (str): the message.
        delay (float, optional): the delay between letters. Defaults to 0.05.
        spacing (bool, optional): whether to space out or not. useful for seperating. Defaults to True.
    """
    for piece in message:
        for char in piece:
            print(char, end='', flush=True)
            await pl.asy.sleep(delay=delay)

    if spacing:
        print()

def better_say(*message, end="\n", seperator="", flush: bool = False):
    """
    say, but with more options.

    Args:
        *message (str): the message.
        end (str, optional): the ending of the say. useful for seperating. Defaults to "\\n".
        seperator (str, optional): the seperator between each message. useful for seperating. Defaults to "".
        flush (bool, optional): whether to force refresh the terminal. Defaults to False.
    """
    print(*message, end=end, sep=seperator, flush=flush)