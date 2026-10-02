"""
# PengPrint

*PengPrint*: Print nicely, stylish, and presentation.

# Features:
    ## Boxes:
        emergency box
        info box
        warning box
    ## Typewriters:
        typewrite
        multitask typewrite
    ## Say:
        better say
"""

from os import terminal_size
from typing import Literal, Optional, TYPE_CHECKING

from ... import penglang as pl
import time as t
from rich import print
from rich.panel import Panel
import textwrap as tw
import shutil as su
from rich import box
if TYPE_CHECKING:
    from rich.box import Box

def emergency_box(message, title="🚨 EMERGENCY 🚨",):
    """
    make an emergency. Useful when you need to emergent the user.

    Args:
        message (str): the emergency message
        title (str, optional): the title of the emergency. Defaults to "🚨 EMERGENCY 🚨".
    """
    pl.say_in_a_box(f"[bold bright_red]{message}[/bold bright_red]", title, "bold bright_red")

def info_box(message, title="Info ℹ️",):
    """
    make an info box. useful when you need to tell the user some info.

    Args:
        message (str): the info message
        title (str, optional): the title of the info box. Defaults to "Info ℹ️".
    """
    pl.say_in_a_box(f"[bold cyan]{message}[/bold cyan]", title, "bold cyan")

def warning_box(message, title="⚠️  Warning ⚠️",):
    """
    make a warning box. useful when you want to warn the user.

    Args:
        message (str): the warning message
        title (str, optional): the title of the warning. Defaults to "⚠️  Warning ⚠️".
    """
    pl.say_in_a_box(f"[bold yellow]{message}[/bold yellow]", title, "bold yellow")






def better_say_in_a_box(
        message: str = "",
        title: str | None = None,
        box_color: str = "white",
        subtitle: str | None = None,
        title_side: Literal[
            "center",
            "left",
            "right"
        ] = "center",
        subtitle_side: Literal[
            "center",
            "left",
            "right"
        ] = "center",
        fill_area: bool = True,
        spacing: tuple[int] = (0, 1),
        highlight: bool = False,
        style: str = "none",
        width: Optional[int] = None,
        height: Optional[int] = None,
        box_type: "Box" | None = box.ROUNDED,
        safe_box: bool = True
        
        ) -> None:
    """
    say_in_a_box, but with many more options. useful for advanced penguins that want to up their box game.

    Args:
        message (str, optional): the message in the box. Defaults to "".
        title (str | None, optional): the title of the box. Defaults to None.
        box_color (str, optional): the box's color. Defaults to "white".
        subtitle (str | None, optional): the subtitle of the box. appears at the bottom. Defaults to None.
        title_side (Literal[ &quot;center&quot;, &quot;left&quot;, &quot;right&quot; ], optional): the title's side. Defaults to "center".
        subtitle_side (Literal[ &quot;center&quot;, &quot;left&quot;, &quot;right&quot; ], optional): the subtitle's side. Defaults to "center".
        fill_area (bool, optional): whether to fill the entire area, or make the box only shaped with the message inside. Defaults to True.
        spacing (tuple[int], optional): the spacing of the box. Defaults to (0, 1).
        highlight (bool, optional): whether to highlight the title automatically or not. Defaults to False.
        style (str, optional): the style of the message and box. Defaults to "none".
        width (Optional[int], optional): the width of the box. Defaults to None.
        height (Optional[int], optional): the height of the box. Defaults to None.
        box_type (Box, optional): the type of how the box looks. Defaults to box.ROUNDED.
        safe_box (bool, optional): whether to make the box safe or not. Defaults to True.
    """
    print(
        Panel(
            renderable=message,
            title=title,
            border_style=box_color,
            subtitle=subtitle,
            title_align=title_side,
            subtitle_align=subtitle_side,
            expand=fill_area,
            padding=spacing,
            highlight=highlight,
            style=style,
            width=width,
            height=height,
            box=box_type,
            safe_box=safe_box
        )
    )




