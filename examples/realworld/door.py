import penglang.say as plsay

answer = plsay.penguin_ask("what question: ")

plsay.penguin_speech_bubble(
    f"yes to {answer}",
    speech_direction="^",
    penguins=5,
    penguin_looks="🚪"
)