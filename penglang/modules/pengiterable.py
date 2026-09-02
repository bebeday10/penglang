"""
# PengIterable

PengIterable: the module for iterables

- get answers
- add stuff
- remove stuff
- reverse stuff
- inverse stuff
"""


from .. import penglang as pl
from collections import defaultdict
from copy import deepcopy
from typing import Any, Callable, Iterable

def get_answer(key: Any, dictionary: dict, if_no_exist: Any = None) -> Any:
    """
    get the answers from a dictionary

    Args:
        key (Any): the key
        dictionary (dict): the dictionary
        if_no_exist (Any, optional): if it doesn't exist, get what answer. Defaults to None.

    Returns:
        Any: the answer from the dictionary
    """
    return dictionary.get(key, if_no_exist)

def add_to_list(the_list: list, *items: Any) -> list:
    """
    add items to a list

    Args:
        the_list (list): the list to add items to
        *items (Any): the items to add to the list

    Returns:
        list: the list with the added items
    """
    for i in items:
        the_list.append(i)
    return the_list

def add_to_dict(the_dict: dict, **items) -> dict:
    """
    add items to a dictionary

    Args:
        the_dict (dict): the dictionary to add it to
        **items (Any): the items to add to the dictionary

    Returns:
        dict: the dictionary with the added items
    """
    the_dict.update(items)
    return the_dict

def remove_from_list(the_list: list, *items):
    """
    remove items from a list

    Args:
        the_list (list): the list to remove items
        *items (Any): the items to remove from the list

    Returns:
        list: the list with the removed items
    """
    for i in items:
        if i in the_list:
            the_list.remove(i)
    
    return the_list

def remove_from_dict(the_dict: dict, *items):
    """
    remove items from the dictionary

    Args:
        the_dict (dict): the dictionary to remove items
        *items (Any): the key of the items to remove from the dictionary

    Returns:
        dict: the dictionary with the removed items
    """
    for i in items:
        if i in the_dict.keys():
            the_dict.pop(i)

    return the_dict

def reverse_the_list(the_list: list):
    """
    reverse a list

    Args:
        the_list (list): the list to get removed

    Returns:
        list: the reversed list
    """
    the_list.reverse()

    return the_list

def reverse_the_dict(the_dict: dict):
    """
    reverse a dictionary.

    Args:
        the_dict (dict): the dictionary to reverse

    Returns:
        dict: the reversed dictionary
    """
    return dict(reversed(the_dict.items()))

def invert_the_dict(the_dict: dict):
    """
    invert a dictionary

    Args:
        the_dict (dict): the dictionary to invert

    Returns:
        dict: the inverted dictionary

    Examples:
        >>> invert_the_dict({"penguin": "banana"})
        {"banana": "penguin"}
    """
    inverted_dict = defaultdict(list)

    for key, value in the_dict.items():
        inverted_dict[value].append(key)

    return inverted_dict


def iterate_a_function(the_iterable: Iterable, func: Callable, **funckwargs):
    if isinstance(the_iterable, dict):
        for i, j in the_iterable.items():
            func(i, j, **funckwargs)
    else:
        for i in the_iterable:
            func(i, **funckwargs)

def list_to_dict(the_list, default):
    return {i: deepcopy(default) for i in the_list}

def list_combine(list_a: list, list_b: list) -> dict:

    dictionary = list_to_dict(list_a, None)
    for i, (key, val) in enumerate(deepcopy(dictionary).items()):
        dictionary[key] = list_b[i % len(list_b)]

    return dictionary

