from struct import pack
from typing import Any, Callable, Literal
from PIL import Image
import customtkinter as ctk
import tkinter as tk

class PenguinFancyWindow(ctk.CTkToplevel):
    def __init__(self, *args, fg_color = None, window_title: str = "Penguin Fancy Window", size: str = "1280x720", **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.title(window_title)
        self.geometry(size)
        self.widgets: dict[str, ctk.CTkBaseClass] = {}
    def add_widget(self, widget: ctk.CTkBaseClass, widget_name: str, x_space: int = 10, y_space: int = 10, side: Literal["left", "right", "top", "bottom"] = "left", owner=None, packother=None, corner_radius=10, border_width=10, fill="both", expand=True, **other):
        if packother is None:
            packother = {}
        if owner is None:
            owner = self

        self.widgets[widget_name] = widget(owner, corner_radius=corner_radius, border_width = border_width, **other)
        self.widgets[widget_name].pack(padx=x_space, pady=y_space, fill=fill, expand=expand, side=side, **packother)

    def get_widget(self, widget_name: str, *args, **kwargs):
        if self.widgets.get(widget_name) is None:
            return "It doesn't exist!!!"

        return self.widgets[widget_name].get(*args, **kwargs)
    def add_button(
            self,
            widget_name,
            command: Callable | None = None,
            x_space: int = 10,
            y_space: int = 10,
            side: Literal["left", "right", "top", "bottom"] = "left",
            text: str = "Penguin Button",
            owner=None
            ):
        if owner is None:
            owner = self

        self.widgets[widget_name] = ctk.CTkButton(owner, corner_radius=10, border_width=10, command=command, text=text)
        self.widgets[widget_name].pack(padx=x_space, pady=y_space, fill="both", expand=True, side=side)

    def remove_widget(self, widget_name = None):
        if self.widgets.get(widget_name) is None:
            return "It doesn't exist!!!"

        self.widgets[widget_name].pack_forget()

    def add_textbox(
            self,
            widget_name: str,
            x_space: int = 10,
            y_space: int = 10,
            side: Literal["left", "right", "top", "bottom"] = "left",
            command: Callable | None = None,
            owner=None
    ):
        self.add_widget(ctk.CTkTextbox, widget_name, x_space, y_space, side=side, owner=owner)
        if command:
            self.widgets[widget_name].bind("<Return>", command)

    def get_textbox(self, widget_name):
        return self.get_widget(widget_name, "0.0", "end")

    def remove_textbox_text(self, widget_name):
        """Clear the textbox."""
        if self.widgets.get(widget_name) is None:
            return "It doesn't exist!!!"
        self.widgets[widget_name].delete("0.0", "end")

    def add_entry(
            self,
            widget_name: str,
            x_space: int = 10,
            y_space: int = 10,
            side: Literal["left", "right", "top", "bottom"] = "left",
            command: Callable | None = None,
            placeholder_text: str = None,
            fill="x",
            expand=False,
            height=50,
            owner=None
    ):
        self.add_widget(ctk.CTkEntry, widget_name, x_space, y_space, side=side, owner=owner, placeholder_text=placeholder_text, fill=fill, expand=expand, height=height)
        if command:
            self.widgets[widget_name].bind("<Return>", command)

    def add_frame(
            self,
            widget_name: str,
            x_space: int = 10,
            y_space: int = 10,
            side: Literal["left", "right", "top", "bottom"] = "left",
            
            owner=None
    ):
        self.add_widget(ctk.CTkFrame, widget_name, x_space, y_space, side=side, owner=owner, packother={"ipadx": 15, "ipady": 15})

    def get_entry(self, widget_name):
        return self.get_widget(widget_name)

    def remove_entry_text(self, widget_name):
        if self.widgets.get(widget_name) is None:
            return "It doesn't exist!!!"
        self.widgets[widget_name].delete(0, "end")

    def when_closed(self, command: Callable):
        self.protocol("WM_DELETE_WINDOW", command)

    def configure_widget(self, widget_name: str, make_ice_again: bool = False, **to_configure):
        if self.widgets.get(widget_name) is None:
            return "It doesn't exist!!!"

        self.widgets[widget_name].configure(make_ice_again, **to_configure)

    def app_icon(self, icon_path):
        self._app_icon = tk.PhotoImage(file=icon_path)
        self.after(201, lambda: self.iconphoto(False, self._app_icon))

    def add_image(
            self,
            image_widget_name: str,
            image_file: str,
            label_widget_name: str | None = None,
            x_space: int = 10,
            y_space: int = 10,
            side: Literal["left", "right", "top", "bottom"] = "left",
            image_size: tuple[int, int] = (256, 256),
            owner=None,
            corner_radius = 0,
            border_width = 0,

    ):
        if owner is None:
            owner = self
        if label_widget_name is None:
            label_widget_name = image_widget_name + "_label"
        self.widgets[image_widget_name] = ctk.CTkImage(
            Image.open(image_file),
            Image.open(image_file),
            image_size
        )

        self.add_widget(
            ctk.CTkLabel,
            label_widget_name,
            x_space,
            y_space,
            side,
            owner,
            text="",
            image=self.widgets[image_widget_name],
            corner_radius=corner_radius,
            border_width=border_width
        )




