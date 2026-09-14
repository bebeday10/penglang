"""
# PengString

*PengString*, the module for strings and everything.

# Features:
    - reverse speech
"""
# strings and everything

from typing import Iterable
from copy import deepcopy
from .. import penglang as pl


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

def put_speech_in_speech_everywhere(original_speech: str, speech_to_put: str, log: bool = False, cjk: bool = False) -> list:
    """
    for every word in the speech, put the speech in it. Great for that one person.

    Args:
        original_speech (str): the original speech to use to put the speech to put.
        speech_to_put (str): the speech to put in the original speech
        log (bool, optional): display every single putting. Defaults to False.
        cjk (bool, optional): for Chinese/Japanese/Korean. used because they don't really have spaces. you can also use this for putting in every letter. Defaults to False.

    Returns:
        list: the puts
    """
    if cjk:
        chopped_speech = list(original_speech)
    else:
        chopped_speech: list[str] = original_speech.split()
    speech_list: list[str] = []
    for i, speech in enumerate(chopped_speech):
        speech_copy = deepcopy(chopped_speech)
        speech_copy.insert(i, speech_to_put)
        if cjk:
            speech_with_speech = "".join(speech_copy)
        else:
            speech_with_speech = " ".join(speech_copy)
        if log:
            pl.say(speech_with_speech)
        speech_list.append(speech_with_speech)
    speech_copy = deepcopy(chopped_speech)
    speech_copy.append(speech_to_put)
    if cjk:
        speech_with_speech = "".join(speech_copy)
    else:
        speech_with_speech = " ".join(speech_copy)
    if log:
        pl.say(speech_with_speech)
    speech_list.append(speech_with_speech)
    return speech_list
