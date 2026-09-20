import penglang.modules.pengcursor as pc
import penglang as pl
import penglang.say as plsay

cursor = pc.PenguinCursor({"x": 0, "y": 0})

cursor.move("x", 4)
cursor.pin("house")
cursor.move("y", 7)
cursor.move("x", -3)
cursor.pin("restaurant")

cursor.move("y", -6)
plsay.say(cursor.get_far_from_pin("house"))
plsay.say(cursor.get_far_from_pin("restaurant"))
plsay.say(cursor.get_pin_far_from_pin("house", "restaurant"))
plsay.better_say(cursor.get_position(), cursor.pins)

cursor.go_to_pin("restaurant")
plsay.better_say(cursor.position, cursor.get_pin())
cursor.remove_pin("restaurant")
plsay.better_say(cursor.get_pin(), cursor.has_pin())
