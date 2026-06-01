import tkinter as tk
import penglang_language.penglang as peng

def penguin_window(title="Penguin Window", width=400, height=300,color="lightgray", log: bool = False):
    """
    add a root window

    Args:
        title (str, optional): The title of the window. Defaults to "Penguin Window".
        width (int, optional): The width of the window. Defaults to 400.
        height (int, optional): The height of the window. Defaults to 300.
        color (str, optional): The background color of the window. Defaults to "lightgray".
        log (bool, optional): Whether to log the creation of the window. Defaults to False.

    Returns:
        tk.Tk: the window object that was created
    """
    window = tk.Tk()
    window.title(title)
    window.geometry(f"{width}x{height}")
    window.configure(bg=color)
    if log:
     peng.say(f"Created a penguin window with title: {title}, width: {width}, height: {height}")
    return window

def wait_for_window(target_title, parent, action, log: bool = False, forever_check: bool = False, *action_args, **action_kwargs):
    """
    wait for a windows existance, then do the action

    Args:
        target_title (str): The title of the window to wait for.
        parent (tk.Tk): The parent window.
        action (callable): The function to call when the window is found.
        log (bool, optional): Whether to log the process. Defaults to False.
        forever_check (bool, optional): Whether to keep checking indefinitely. Defaults to False.
        *action_args: Positional arguments to pass to the action function.
        **action_kwargs: Keyword arguments to pass to the action function.
    """
    target_window = None
    for child in parent.winfo_children():
        if isinstance(child, tk.Toplevel) and child.wm_title() == target_title:
            target_window = child
            break

    if target_window == None:
        parent.after(100, lambda: wait_for_window(target_title, parent, action, log, forever_check, *action_args, **action_kwargs))
    else:
        if log:
            peng.say(f"Found the target window with title: {target_title}")
        try:
         action(*action_args, **action_kwargs)
        except Exception as e:
            if log:
                peng.say(f"tried to run the action, but the window closed before it could run.")
        if forever_check:
            parent.after(100, lambda: wait_for_window(target_title, parent, action, log, forever_check, *action_args, **action_kwargs))

def penguin_label(window, text="Penguin Label", log: bool = False):
    """
    make a label

    Args:
        window (tk.Tk): The window to add the label to.
        text (str, optional): The text for the label. Defaults to "Penguin Label".
        log (bool, optional): Whether to log the creation of the label. Defaults to False.

    Returns:
        tk.Label: The created label widget.
    """
    label = tk.Label(window, text=text)
    label.pack()
    if log:
        peng.say(f"Created a penguin label with text: {text}")
    return label

def penguin_button(window, text="Penguin Button", command=None, log: bool = False):
    """
    make a button

    Args:
        window (tk.Tk): The window to add the button to.
        text (str, optional): The text for the button. Defaults to "Penguin Button".
        command (callable, optional): The function to call when the button is clicked. Defaults to None.
        log (bool, optional): Whether to log the creation of the button. Defaults to False.

    Returns:
        tk.Button: The created button widget.
    """
    button = tk.Button(window, text=text, command=command)
    button.pack()
    if log:
        peng.say(f"Created a penguin button with text: {text}, command: {command}")
    return button

def color_widget(widget, color, log: bool = False):
    widget.configure(bg=color)
    if log:
        peng.say(f"Changed the penguin widget color to: {color}")

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

def penguin_window_maker(parent, name, sendfunc,width=400, height=300, log: bool = False):
    """
    make a window that's assigned to a dictionary

    Args:
        parent (tk.Tk): The parent window.
        name (str): The name of the window.
        sendfunc (callable): The function to send the window reference.
        width (int, optional): The width of the window. Defaults to 400.
        height (int, optional): The height of the window. Defaults to 300.
        log (bool, optional): Whether to log the creation of the window. Defaults to False.
    """
    w = tk.Toplevel(parent)
    w.title(name)
    w.geometry(f"{width}x{height}")
    sendfunc(name, w)
    if log:
        peng.say(f"Created a penguin window with name: {name}, sendfunc: {sendfunc}")

def penguin_spacing(window, spacing=10, log: bool = False):
    """
    add spacing to all widgets in a window

    Args:
        window (tk.Toplevel | tk.Tk): The window to add spacing to.
        spacing (int, optional): The amount of spacing to add. Defaults to 10.
        log (bool, optional): Whether to log the action. Defaults to False.
    """
    for widget in window.winfo_children():
        widget.pack_configure(padx=spacing, pady=spacing)
    if log:
        peng.say(f"Added spacing of {spacing} to all penguin widgets in the window")