import tkinter as tk
from ... import penglang as peng

def penguin_extra_window(title="Penguin Extra Window", width=400, height=300,color="lightgray", log: bool = False): # the problem is you can't add a widget to this window because we don't know if the window exists or not, but we can still create the window and show it!
    """
    add an extra window

    Args:
        title (str, optional): The title of the extra window. Defaults to "Penguin Extra Window".
        width (int, optional): The width of the extra window. Defaults to 400.
        height (int, optional): The height of the extra window. Defaults to 300.
        color (str, optional): The background color of the extra window. Defaults to "lightgray".
        log (bool, optional): Whether to log the creation of the extra window. Defaults to False.

    Returns:
        tk.Toplevel: The created extra window.

    Note:
        This function cannot be assigned to a variable from a button command, for that, use penguin_window_maker instead.
    """
    # how do we add a widget once it is created without having to use this function to edit the window
    # i know we can wait for the widget to make it when the window is created so the other funcs like color_widget can find it, but that is a bit hacky, but it is the best I can do with this language
    window = tk.Toplevel()
    window.title(title)
    window.geometry(f"{width}x{height}")
    window.configure(bg=color)
    if log:
        peng.say(f"Created a penguin extra window with title: {title}, width: {width}, height: {height}")
    return window