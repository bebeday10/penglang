import penglang as pl
import penglang.say as plsay

@pl.horse
def remake_nonsense():
    plsay.penguin_speech_bubble(
        "making the nonsense",
        28,
        "^",
        3
    )

remake_nonsense()