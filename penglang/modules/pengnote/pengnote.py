from ..pengprint import better_say_in_a_box
from . import pengerrors as pe
from ... import penglang as pl
from typing import Literal
class PenguinNotebook:
    def __init__(self) -> None:
        self.body: list[dict[str, str | None | bool]] = []
        self.name: str = "Notebook"
        self.name_direction: Literal["left", "right", "center"] = "center"
        self.color: str = "white"
        self.author: str = ""
        self.author_direction: Literal["left", "right", "center"] = "center"
        self.bookmarks: dict[str, int] = {}

    def add_note(self, note) -> None:
        self.body.append(
            {
                "note": note,
                "comment": None,
                "show comment": False,
            }
        )

    def display_body(self):
        body = "\n".join(f"Note {i}\n{note["note"]}" for i, note in enumerate(self.body, 1))
        better_say_in_a_box(
            body,
            self.name,
            title_side=self.name_direction,
            box_color=self.color,
            subtitle=self.author,
            subtitle_side=self.author_direction
        )

    def change_color(self, color: str):
        self.color = color
    def change_author(self, author: str):
        self.author = author

    def change_direction(self, what: Literal["author", "name"], direction: Literal["left", "right", "center"]):
        if what == "author":
            self.author_direction = direction
        elif what == "name":
            self.name_direction = direction

    def add_bookmark(self, name: int, where: int):
        try:
            self.body[where]
        except IndexError:
            raise pe.BookmarkError("Tried to bookmark outside of body")

        self.bookmarks[name] = where

    def read_note(self, which: int):
        """
        read a note.

        Args:
            which (int): it starts from 0.

        Raises:
            pe.NotebookError: when tried to read note outside notebook length.
        """
        try:
            note = self.body[which]
        except IndexError:
            raise pe.NotebookError("Tried to read note outside of notebook length")
        pl.say(note["note"])
        
    def get_raw_body(self) -> list[dict[str, str | None | bool]]:
        return self.body
    def get_formatted_body(self):
        body = "\n".join(f"Note {i}\n{note["note"]}" for i, note in enumerate(self.body, 1))
        return body
    