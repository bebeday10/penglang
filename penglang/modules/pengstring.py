"""
# PengString

*PengString*, the module for strings and everything.

# Features:
    - reverse speech
"""
# strings and everything

from typing import Iterable


def reverse_speech(speech: str) -> str:
    """
    reverse speech.

    Args:
        speech (str): the speech

    Returns:
        str: the reversed version
    """
    return speech[::-1]

def cut_speech(speech: str, cut: Iterable[int]) -> str:
    """
    cut a speech

    Args:
        speech (str): the speech to cut
        cut (Iterable[int]): the cut way. (start, stop, step)

    Returns:
        str: the cut speech
    """
    return speech[cut[0]:cut[1]:cut[2]]

def replace_part(text: str, old: str, new: str) -> str:
    """
    replace part in text

    Args:
        text (str): the text to modify
        old (str): the part to replace
        new (str): the replacement

    Returns:
        str: the replaced text
    """
    return text.replace(old, new)