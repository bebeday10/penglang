import penglang.say as plsay
import penglang.modules.pengnoend as pne
import time as t
plsay.penguin_speech_bubble("welcome to the fighters battle")
fighters = pne.PenguinNoEnd(
    [
        "John Hitch",
        "Megata-chan",
        "Penguin the mighty",
        "Gorialla-san"
    ]
)
plsay.emergency_box("it will go")
while True:
    plsay.say(fighters)
    fighters.forward(3)
    t.sleep(0.04)
