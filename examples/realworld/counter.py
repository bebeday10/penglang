import penglang.say as plsay
import importlib

pc = importlib.import_module("penglang.modules.pengcounter") # Python hates PengLang so we have to do this
plsay.info_box("WE count")

counter = pc.PenguinTitleCounter(0, 3, "Jenguin count")

counter.count_up()
counter.count_up()
counter.count_down()

plsay.say(counter)