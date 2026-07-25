from ... import penglang as pl
from . import pengbulletinmessage as pbs
from .. import pengrandom as pd

class PenguinBulletin:
    def __init__(self, body) -> None:
        self.config = {
            "bulletin_item": {
                "body": body
            }
        }

    def change_body(self, body) -> None:
        self.config["bulletin_item"]["body"] = body

    def change_random_body(self):
        self.config["bulletin_item"]["body"] = f"[{"".join(i for i in pd.random_decisions(**pbs.news))}] {pd.random_decision(*pbs.objects)} are currently {pd.random_decision(*pbs.actions)} {pd.random_decision(*pbs.places)}, and others are {pd.random_decision(*pbs.aftermath)}."

    def get_body(self):
        return self.config.get("bulletin_item", {}).get("body")

    def __str__(self) -> str:
        return self.config.get("bulletin_item", {}).get("body")