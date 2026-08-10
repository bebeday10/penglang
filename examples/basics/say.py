import penglang as pl
import penglang.modules.pengprint as pprint
pl.say("HELLO PENGUIN world")
pl.say_in_a_box("box world", "awesome cool box i made", "yellow")

pprint.better_say("advance penguin", " the second", end=" banana line end \n", seperator="-")
pprint.better_say_in_a_box(
    message="advanced box for advanced penguin",
    title="the dance peng",
    box_color="green",
    subtitle="the bottom text",
    title_side="left",
    subtitle_side="right"
)