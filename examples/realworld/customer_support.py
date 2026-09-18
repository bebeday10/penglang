import penglang.say as plsay

plsay.penguin_speech_bubble(
    "hello welcome to customer service",
    penguins=5
)

choices = plsay.PenguinMenu(
    "Choose Your Service",
    [
        "Broken penguin",
        "Speaking horse",
        "Legs not working",
        "Speak to agent"
    ],
    recommend="Exit",
    waiter=True,
    color="blue"
)

while True:
    choice = choices.to_hungry_penguins()
    if choice == "Broken penguin":
        plsay.penguin_speech_bubble(
            "try turning it on and off again"
        )
    elif choice == "Speaking horse":
        plsay.penguin_speech_bubble(
            "try discouraging it"
        )
    elif choice == "Legs not working":
        plsay.penguin_speech_bubble(
            "go doctor"
        )
    elif choice == "Speak to agent":
        plsay.penguin_speech_bubble(
            "we are the agent"
        )
    elif choice == "The penguin profusely disagreed to your menu.":
        plsay.penguin_speech_bubble(
            "thank you",
            penguins=5
        )
        break