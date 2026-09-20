import penglang.modules.pengtimer as pt
import penglang as pl
timer = pt.PenguinTimer(
    seconds=2,
    name="Alarm o' Penguin"
)

for penguin in range(5):
    timer.start_timer()
