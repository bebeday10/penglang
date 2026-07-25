from rich.markdown import Markdown as md
from ... import penglang as pl

class PenguinAdvancedCard:
    def __init__(self, body: str, title: str, color: str) -> None:
        lines: list[str] = body.splitlines()
        self.config = {
            "advanced card": {
                "body": lines,
                "title": title,
                "color": color,
                "cursor": 0,
                "pins": {}
            }
        }
        self.body: list[str] = lines
        self.title: str = title
        self.color: str = color
        self.cursor: int = 0
        self.pins: dict = {}
        """
        the cursor. line 1 is 0. please read the wiki page Penguin's Friends on the GitHub repo for more info
        https://github.com/bebeday10/penglang/wiki/Penguin%27s%20Friends
        """


    def show_card(self):
        """
        show the card.
        """
        self._update_vars()
        body = "\n".join(f"{i}  " for i in self.body)

        pl.say_in_a_box(
            md(body),
            self.title,
            self.color
        )

    def change_cursor_line(self, line: int):
        """
        changes the cursor line.

        Args:
            line (int): the line to let the cursor go
        """
        self.config["advanced card"]["cursor"] = line
        self._update_vars()

    def get_cursor(self):
        self._update_vars()
        return self.cursor

    def get_body(self):
        self._update_vars()
        return self.body

    def insert_line(self, where: int = -1, line: str = "penguin"):
        """
        insert the line.

        Args:
            where (int): the place to insert the line. Based on line numbers
            line (str): the line to insert
        """
        self._update_vars()
        self.config["advanced card"]["body"].insert(where, line) if where != -1 else self.config["advanced card"]["body"].append(line)

    def upper(self):
        self._update_vars()
        self.config["advanced card"]["body"] = [line.upper() for line in self.body]
        self.config["advanced card"]["title"] = self.title.upper()

    def unpenguin(self):
        self.config["advanced card"]["body"] = ["Unfortunately cards do not have memory and cannot help"]

    def add_pin(self, pin_name, pin_line):
        self.config["advanced card"]["pins"][pin_name] = pin_line

    def get_pin(self, pin_name):
        self._update_vars()
        return self.pins.get(pin_name, 0)

    def insert_bullet_point(self, where: int = -1, line: str = "penguin", deep: int = 0):
        """
        insert a bullet point.

        Args:
            where (int): the place to insert the bullet point. Based on line numbers
            line (str): the point to insert
            deep (int): how deep the point is
        """
        self._update_vars()
        self.config["advanced card"]["body"].insert(where, f"{"    "*deep}- {line}")

    def reverse(self, type: str = "line", in_place = True):
        """
        reverse everything

        Args:
            type (str, optional): the type, "line", "word", "letter". Defaults to "line".
            in_place (bool, optional): whether to edit it directly. Defaults to True.

        Returns:
            list[str]: the result.
        """
        self._update_vars()
        match type:
            case "line":
                self.config["advanced card"]["body"] = self.body[::-1] if in_place else self.body
            
            case "word":
                rev_word = [" ".join(lines.split()[::-1]) for lines in self.body]
                self.config["advanced card"]["body"] = rev_word if in_place else self.body

            case "letter":
                rev_letter = [lines[::-1] for lines in self.body]
                self.config["advanced card"]["body"] = rev_letter if in_place else self.body

        return self.body[::-1] if type == "line" else rev_word if type == "word" else rev_letter if type == "letter" else None

    def penguin(self):
        self._update_vars()
        self.config["advanced card"]["body"] = ["".join("🐧" for _ in lines) for lines in self.body]
        self.config["advanced card"]["title"] = " ".join("🐧" for _ in self.title)

    def _update_vars(self):
        self.card = self.config.get("advanced card", {})
        self.body = self.card.get("body", [])
        self.title = self.card.get("title", "")
        self.color = self.card.get("color", "")
        self.cursor = self.card.get("cursor", "")
        self.pins = self.card.get("pins", {})

    def _get_var(self, var: str, default=None):
        self.card = self.config.get("advanced card", {})
        return self.card.get(var, default)
        