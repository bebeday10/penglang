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

from rich import print
from rich.panel import Panel
import asyncio as asy

def say(message):
    """
    This is a task that makes penguins say stuff

    Args:
        message (Any): the message to say, can be any type, it will be converted to a string before being printed
    """
    print(message)

def say_in_a_box(message, title, box_color):
    """
    say stuff, but in a box

    Args:
        message (Any): the message to say
        title (Any): the title of the box
        box_color (str): the color of the box
    """

    print(
        Panel(
           renderable=message,
           title=title,
           border_style=box_color

        )
    )

def fish(thing):
    """
    fish something (returns item)

    Args:
        thing (Any): the item to fish out

    Returns:
        Any: the item that was fished out
    """
    return thing # this is a function that does nothing, just for fun

def task(function):
    """
    do a task

    Args:
        function (Callable): the function to execute

    Returns:
        Any: the result of the function execution
    """
    return function # this is a decorator that does nothing, just for fun

def do(function):
    """
    does a task

    Args:
        function (Callable): the function to execute
    """
    function()

# what else to add?

def penguin_do_over(iterable):
    """
    says each item in the iterable

    Args:
        iterable (Iterable): the iterable to iterate over
    """
    if isinstance(iterable, dict):
        for key, value in iterable.items():
            say(f"{key}: {value}")
    else:
        for item in iterable:
            say(item)

def shout(message):
    """
    shout a message

    Args:
        message (Any): the message to shout, can be any type, it will be converted to a string before being printed
    """
    str(message) # convert message to string just in case it's not already a string
    print(message.upper() + "!!!")

# how to make a rhing that makes a list using a function? how about this:
def penguin_list(*items):
    """
    make a list of items

    Args:
        *items: the items to include in the list

    Returns:
        list: the list containing the items
    """
    return list(items)

def penguin_dict(**kwargs):
    """
    make a dictionary

    Args:
        **kwargs: the key-value pairs for the dictionary

    Returns:
        dict: the dictionary containing the key-value pairs
    """
    return dict(kwargs)

def penguin_variable(name, value):
    """
    make a variable

    Args:
        name (str): the name of the variable
        value (Any): the value of the variable
    """
    globals()[name] = value # how to make a thing that makes a variable? this is a hacky way to do it, but it works! # this doesn't declare the variable though, so anywhere else you want to use it, you have to use the same name as a string, which is not ideal, but it's the best I can do with this language


# sadly you can't make statements like if, for, while, etc. in this language, but you can make functions that do things!

def penguin_yesno_question(thing, condition = True, log: bool = False):
    """
    ask the penguin a question

    Args:
        thing (Any): the thing to check
        condition (Any, optional): the condition to check against. Defaults to True.
        log (bool, optional): whether to log the result. Defaults to False.

    Returns:
        bool: True if the condition is met, False otherwise
    """
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
    """
    the basic penguinerror when you decide it

    Args:
        Exception (str): the error message to raise
    """
    pass
def penguin_error(type, message):
    """
    raise a penguin error

    Args:
        type (str): the type of error
        message (str): the error message

    Raises:
        PenguinError: the penguin error
    """
    raise PenguinError(f"{type} - {message}")

# what other fun things can we add to this language? maybe we can make a function that makes a penguin noise? or a function that makes a penguin dance? the possibilities are endless!

def dance(dance_style = "penguin", shouting: bool = False):
    """
    make a penguin dance.

    Args:
        dance_style (str, optional): the style of dance. Defaults to "penguin".
        shouting (bool, optional): whether the penguin should shout while dancing. Defaults to False.
    """
    say(f"[bright_magenta]The penguin is dancing the {dance_style} dance![/bright_magenta]")
    if shouting:
        shout("Penguin dance!")

def penguin_noise(noise = "penguin", shouting: bool = False, times: int = 1):
    """
    make a penguin make a noise.

    Args:
        noise (str, optional): the noise to make. Defaults to "penguin".
        shouting (bool, optional): whether the penguin should shout the noise. Defaults to False.
        times (int, optional): how many times to make the noise. Defaults to 1.
    """
    for _ in range(times):
        say(f"The penguin says: {noise}!")
        if shouting:
            shout(f"{noise}!")

# could we make like a tkinter type of module for this language? that would be fun! we could make functions for creating windows, buttons, labels, etc. that use penguin words instead of python keywords! maybe we can call it pengtkinter or something like that!
# let's call it pengwindow! we can make functions for creating windows, buttons, labels, etc. that use penguin words instead of python keywords! that could be fun!
# i just did that just now, check it out!

# make a help function

def penguin_help(function):
    """
    get help on a function

    Args:
        function (Callable): the function to get help on
    """
    if hasattr(function, "__doc__") and function.__doc__:
        say(f"here is the help for {function.__name__}:")
        say(function.__doc__)
    else:
        say(f"penguin scoured the depths of the ocean but couldn't find any help for {function.__name__}!")


# make a function factory
# what else can we add to the factory?

def penguin_function_maker(typeofthing, log_: bool = False, **funcargs):
    """
    make a function

    Args:
        typeofthing (str): the type of function to create
        log_ (bool, optional): whether to log the creation of the function. Defaults to False.

    Returns:
        Callable: the created function
    """
    if log_:
        say(f"Creating a penguin function of type: {typeofthing} with message: {funcargs.get('message', 'No message provided')}")
    def inner():
        if typeofthing == "dance":

            return dance(funcargs.get("dance_style", "penguin"), funcargs.get("shouting", False))
        elif typeofthing == "noise":

            return penguin_noise(funcargs.get("noise", "penguin"), funcargs.get("shouting", False), funcargs.get("times", 1))
        elif typeofthing == "shout":

            return shout(funcargs.get("message", "Penguin Shout!"))
        elif typeofthing == "say":

            return say(funcargs.get("message", "Penguin says something!"))
        
        elif typeofthing == "help":

            return penguin_help(funcargs.get("function", lambda: None))
        
    return inner

# multi command func

def penguin_multi_command(*commands):
    """
    execute multiple commands in sequence

    Args:
        *commands (Callable): the commands to execute, each command should be a callable
    """
    for command in commands:
        command()

def penguin_execute(thing_to_execute: str):
    """
    execute a string

    Args:
        thing_to_execute (str): the thing the execute, make sure it's a string
    """
    exec(thing_to_execute)


# Horse

def horse(func):
    """
    make a function that does something horse-related NOTE: this is just for fun, it doesn't actually do anything horse-related, it's just a decorator that adds some horse-related messages before and after the function execution

    Args:
        func (Callable): the function to execute when the horse does its thing

    Returns:
        Callable: the decorated function that includes horse-related messages
    """
    def inner(*args, **kwargs):
        say("neeeeeigh! 🐎🐎🐎 hoooorse!")
        func(*args, **kwargs)
        say("the horse has finished its thing!")
    return inner

def multitask(func):
    """
    multitask that makes sleeping only to that func only, use await statement

    Args:
        func (Callable): the func

    Returns:
        the function but with async on
    """
    def wrapper(*args, **kwargs):
        return asy.run(func(*args, **kwargs))
    
    return wrapper