# this is a funny penguin language using python as syntax, but with penguin words instead of python keywords
"""This is a funny penguin language using python as syntax.
    This language is not meant to be taken seriously, it's just for fun!
    You can use this language to write code that looks like it's written by a penguin, but it's still valid python code!
    things you can do with this language:
    - say things
    - make lists and dictionaries
    - make variables
    - make functions that do things
    - make functions that do things if a condition is true"""

def say(message):
    print(message)

def fish(thing):
    return thing # this is a function that does nothing, just for fun

def task(function):
    return function # this is a decorator that does nothing, just for fun

def do(function):
    function()

# what else to add?

def penguin_do_over(iterable):
    if isinstance(iterable, dict):
        for key, value in iterable.items():
            say(f"{key}: {value}")
    else:
        for item in iterable:
            say(item)

def shout(message):
    print(message.upper() + "!!!")

# how to make a rhing that makes a list using a function? how about this:
def penguin_list(*items):
    return list(items)

def penguin_dict(**kwargs):
    return dict(kwargs)

def penguin_variable(name, value):
    globals()[name] = value # how to make a thing that makes a variable? this is a hacky way to do it, but it works! # this doesn't declare the variable though, so anywhere else you want to use it, you have to use the same name as a string, which is not ideal, but it's the best I can do with this language


# sadly you can't make statements like if, for, while, etc. in this language, but you can make functions that do things!

def penguin_yesno_question(thing, condition = True, log: bool = False):
    if thing == condition:
        if log:
            say(f"{thing} is {condition}!")
        return True
    else:
        if log:
            say(f"{thing} is not {condition}!")
        return False
    
# what if we want to make a function that does something if a condition is true? we can use the penguin_yesno_question function for that!
# do we want to make modules for this language? maybe we can make a module for math functions, a module for string functions, etc. that use penguin words instead of python keywords? that could be fun!
# what should we make first? maybe a math module? we can make functions for addition, subtraction, multiplication, division, etc. that use penguin words instead of python keywords!

# should we make error messages that are more penguin-like? maybe we can make a function that raises an error with a penguin message instead of a python message? that could be fun!
class PenguinError(Exception):
    pass
def penguin_error(type, message):
    raise PenguinError(f"{type} - {message}")

# what other fun things can we add to this language? maybe we can make a function that makes a penguin noise? or a function that makes a penguin dance? the possibilities are endless!

def dance(dance_style = "penguin", shouting: bool = False):
    say(f"The penguin is dancing the {dance_style} dance!")
    if shouting:
        shout("Penguin dance!")

def penguin_noise(noise = "penguin", shouting: bool = False, times: int = 1):
    for _ in range(times):
        say(f"The penguin says: {noise}!")
        if shouting:
            shout(f"{noise}!")

# could we make like a tkinter type of module for this language? that would be fun! we could make functions for creating windows, buttons, labels, etc. that use penguin words instead of python keywords! maybe we can call it pengtkinter or something like that!
# let's call it pengwindow! we can make functions for creating windows, buttons, labels, etc. that use penguin words instead of python keywords! that could be fun!