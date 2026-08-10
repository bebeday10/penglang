import penglang.modules.pengiterable as pi
import penglang.modules.pengthing.pengthinglist as ptl
import penglang as pl

def awesome_func(i):
    pl.dance(i)

awesome_list = ptl.PenguinList(["banana", "penguin", "the terrible dance"])
pi.iterate_a_function(awesome_list, awesome_func)