import penglang.modules.pengtranslate as pt
import penglang as pl
import penglang.modules.pengprint as pprint
import penglang.modules.pengsymbol as ps
import penglang.modules.pengrandom as pr

pprint.info_box(
    "Elevator Motion",
    "'vator 🛗"
)
horse_translator = pt.PenguinTranslateMachine(
    translate_to=ps.alphabet,
    translate_from="horse"
)

pl.say("horse is saying something!!!")
horse_talker = pr.PenguinIceOfRandom(
    random_list=list("horse"),
    length=20
)

speech = horse_talker.to_no_ice()

pl.say(f"it says: '{speech}'")
pl.say(f"here's what it means in english: '{horse_translator.translate(speech)}'")

pprint.info_box(
    "You have reached destination of Level 1. Now go ahead",
    "Go"
)