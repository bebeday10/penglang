from ... import penglang as pl
from .. import pengsymbol as ps
from . import pengrandom as pr
from .. import pengiterable as pi

class PenguinIceOfRandom:
    def __init__(self, random_list: list = list(map(str, ps.alphanums)), length=50):
        self.random_list = random_list
        self.length = length

    def to_ice(self):
        pl.say("".join(pr.random_decisions(**pi.list_to_dict(self.random_list, 1), times=self.length)))
