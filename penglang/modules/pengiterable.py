from .. import penglang as pl
from collections import defaultdict

def get_answer(key: str | int, dictionary: dict, if_no_exist=None):
    return dictionary.get(key, if_no_exist)

def add_to_list(the_list: list, *items):
    for i in items:
        the_list.append(i)
    return the_list

def add_to_dict(the_dict: dict, **items):
    the_dict.update(items)
    return the_dict

def remove_from_list(the_list: list, *items):
    for i in items:
        if i in the_list:
            the_list.remove(i)
    
    return the_list

def remove_from_dict(the_dict: dict, *items):
    for i in items:
        if i in the_dict.keys():
            the_dict.pop(i)

    return the_dict

def reverse_the_list(the_list: list):
    the_list.reverse()

    return the_list

def reverse_the_dict(the_dict: dict):
    return dict(reversed(the_dict.items()))

def invert_the_dict(the_dict: dict):
    inverted_dict =defaultdict(list)

    for key, value in the_dict.items():
        inverted_dict[value].append(key)

    return inverted_dict
            
