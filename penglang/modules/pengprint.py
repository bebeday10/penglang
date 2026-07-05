from .. import penglang as pl
import time as t
from rich import print

def emergency_box(message, title="🚨 EMERGENCY 🚨",):
    pl.say_in_a_box(f"[bold bright_red]{message}[/bold bright_red]", title, "bold bright_red")

def info_box(message, title="Info ℹ️",):
    pl.say_in_a_box(f"[bold cyan]{message}[/bold cyan]", title, "bold cyan")

def warning_box(message, title="⚠️  Warning ⚠️",):
    pl.say_in_a_box(f"[bold yellow]{message}[/bold yellow]", title, "bold yellow")

def typewrite(*message, delay: float = 0.05, pause: bool = True, spacing: bool = True):
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
    for piece in message:
        for char in piece:
            print(char, end='', flush=True)
            await pl.asy.sleep(delay=delay)

    if spacing:
        print()

def better_say(*message, end="\n", seperator="", flush: bool = False):
    print(*message, end=end, sep=seperator)