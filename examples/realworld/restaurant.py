import penglang.say as plsay
import penglang.modules.pengnoend as pne

plsay.info_box("Welcome to John's","John's very suspicious restaurant (Bob included)")

customers = pne.PenguinNoEnd(
    [
        "Jane",
        "Penguin",
        "Sir Doodleton",
        "Ms Lichedtendestain"
    ]
)

plsay.dance(
    "dance dance dance rock",
    shouting=True
)
def to_the_next():
    customers.forward(1)
def serve():
    customer = customers.get()
    plsay.say(f"serving {customer} and to the next")

for _ in range(10):
    serve()
    to_the_next()