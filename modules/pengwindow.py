import tkinter as tk
import penglang_language.penglang as peng

def penguin_window(title="Penguin Window", width=400, height=300,color="lightgray", log: bool = False):
    window = tk.Tk()
    window.title(title)
    window.geometry(f"{width}x{height}")
    window.configure(bg=color)
    if log:
     peng.say(f"Created a penguin window with title: {title}, width: {width}, height: {height}")
    return window

def wait_for_window(target_title, parent, action, log: bool = False, forever_check: bool = False, *action_args, **action_kwargs):
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
    label = tk.Label(window, text=text)
    label.pack()
    if log:
        peng.say(f"Created a penguin label with text: {text}")
    return label

def penguin_button(window, text="Penguin Button", command=None, log: bool = False):
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
    w = tk.Toplevel(parent)
    w.title(name)
    w.geometry(f"{width}x{height}")
    sendfunc(name, w)
    if log:
        peng.say(f"Created a penguin window with name: {name}, sendfunc: {sendfunc}")

def penguin_spacing(window, spacing=10, log: bool = False):
    for widget in window.winfo_children():
        widget.pack_configure(padx=spacing, pady=spacing)
    if log:
        peng.say(f"Added spacing of {spacing} to all penguin widgets in the window")