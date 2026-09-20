import penglang.say as plsay
import penglang.modules.pengboxofstuff as pbos

plsay.say_in_a_box(
    "welcome to disco™",
    "Disco 🕺🪩",
    "magenta"
)
dances = pbos.PenguinBoxOfStuff(
    [
        "the banana dance",
        "penguin",
        "rock",
        "disco",
        "cool penguin",
        "awkward dance"
    ]
)
while dances:
    plsay.dance(dances())
