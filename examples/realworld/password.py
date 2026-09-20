import penglang.say as plsay
import penglang.modules.pengrandom as pr


plsay.penguin_speech_bubble(
    "The penguins are making a password...",
    speech_direction="^",
    penguins=3
)

pr.PenguinIceOfRandom(random_list = list("penguinlabanana"),length=30).to_ice()

plsay.penguin_speech_bubble(
    "Now use this unsecure password",
    speech_direction="^",
    penguins=3
)