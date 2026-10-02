import time as t
from ... import penglang as pl
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