import penglang.say as plsay
import penglang.modules.pengtranslate as pt
import penglang.modules.pengsymbol as ps

plsay.info_box(
    "Welcome to the penguin translation booth."
)

translator = pt.PenguinTranslateMachine(
    translate_to=ps.alphabet,
    translate_from=ps.alphabet[::-1]
)

plsay.say(translator.translate("kvmtfrmh ziv xllo yvxzfhv yzmzmz"))