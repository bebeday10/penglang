import penglang.modules.pengmustfollow as pmf
import penglang as pl
follows = pmf.PenguinIceOfMustFollows(
    [
        "penguin slip",
        "littering",
        "horsing around"
    ]
)

penguin = "littering"

if follows.is_must_follow(penguin):
    follows.add_to_must_follow_breakers("penguin")

pl.say(follows.must_follow_breakers)