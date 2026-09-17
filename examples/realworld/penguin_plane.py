import penglang as pl
import penglang.modules.pengprint as pprint
import penglang.modules.pengrandom as pr
import penglang.modules.pengiterable as pi
import penglang.modules.pengmenu as pm

pprint.info_box(
    "Welcome to your flight. Please the flight wait",
    "Flight ℹ️"
)

pl.say(f"FLIGHT P-{pr.random_number(0, 999)}")
pl.say("every gate")
pl.say("probably boarding")

passengers = [
    "Licknash Mcgee",
    "Steave",
    "Ultra Horse",
    "Anon... Anon... Anyonnyomus"
]

def passenger_namer(name):
    pprint.penguin_speech_bubble(
        f"here is the penguin that is boarding this flight today: {name}",
        speech_direction="^",
        penguins=5
    )

pi.iterate_a_function(passengers, passenger_namer)

pl.say(
"""
probably luggage
and ice
"""
)

pl.say("you are the board")
board_choices = [
    "board passengers",
    "inspect luggage",
    "check flight status",
    "buy bananas",
    "cause incident, crash into small pond",
    "depart"
]

while True:
    render_penguin = pm.PenguinMenu(
        "flight board",
        board_choices,
        color="blue",
        waiter=True,
        hungry_penguins=3,
        recommend="depart"
    )
    choice = render_penguin.to_hungry_penguins()
    match choice:
        case "board passengers":
            pl.say("they has board")
        case "inspect luggage":
            pl.say("probably ok")
        case "check flight status":
            pl.say("maybe needs ice")
        case "buy bananas":
            pl.say("you bought and ate them")
        case "cause incident, crash into small pond":
            pl.say("✈️🚤💥")
            pprint.emergency_box("AAAAAAAAAA IT CRASHED")
            break
        case "depart":
            pl.say("it safely departs")
            break
        case "The penguin profusely disagreed to your menu.":
            pl.say("you disagreed")
            break