import penglang.say as plsay
import penglang.modules.pengboxofstuff as pbos

plsay.info_box(
    "welcome to the weather service",
    "the weather"
)

weathers = pbos.PenguinBoxOfStuff(
    [
        "sunny",
        "windy",
        "cloudy",
        "hazardly",
        "snowy",
        "clearly",
        "ominous rain"
    ],
    "Weather Box"
)

hour = 0
while weathers:
    plsay.say(f"a forecast in {hour} hours: {weathers()}")
    hour += 1