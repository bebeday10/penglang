import json
from typing import Any

from ..pengprint import better_say

from ... import penglang as pl, say_in_a_box
from rich.markdown import Markdown as md

class PenguinCard:
    def __init__(self,
                body: str,
                type: str,
                title: str = "Card",
                color: str = "bright_blue",
                show_type: bool = True,
                    ) -> None:
        self.config: dict[str, dict[str, md]] = {
            "card": {
                "body": body,
                "type": type,
                "show_type": show_type,
                "title": title,
                'color': color,
            }
        }

    def show_card(self, log: bool = True) -> md:
        card = self.config.get("card")

        say_in_a_box(
                    md(card.get("body", "") + (card.get("type", "") if card.get("show_type", True) else "")),
                   card.get("title", "Card"), card.get("color", "bright_blue")) if log else None
        return card.get("body")
    
    def change_config(self, config_what: str, config_to: Any):
        card = self.config.get("card")
        card[config_what] = config_to

    def upper(self) -> PenguinCard:
        body = self.config.get("card", {}).get("body", "")

        self.config["card"]["body"] = body.upper()

        return self

    def reverse(self) -> PenguinCard:
        body = self.config.get("card", {}).get("body", "")
        self.config["card"]["body"] = body[::-1]

        return self
    
    def penguin(self) -> PenguinCard:
        body = self.config.get("card", {}).get("body", "")
        self.config["card"]["body"] = ", ".join("penguin" for _ in enumerate(body))

        return self
    
    def export(self, filename, export_as="md"):
        if export_as == "md":
            with open(filename, "w", encoding="utf-8") as f:
                f.write(self.config.get("card", {}).get("body"))

        elif export_as == "json":
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)

    def __add__(self, other: str | PenguinCard) -> PenguinCard:
        if isinstance(other, str):
            card: dict[str, md] | None = self.config.get("card")
            body: str = card.get("body", "")

            return PenguinCard(body + other, type=card.get("type"), show_type=card.get("show_type"))
        
        elif isinstance(other, PenguinCard):
            card: dict[str, md] | None = self.config.get("card")
            body: str = card.get("body", "")
            other_card = other.config.get("card", {})
            other_body = other.config.get("card", {}).get("body", "")

            return PenguinCard(body + other_body, card.get("type", "") + other_card.get("type"))


