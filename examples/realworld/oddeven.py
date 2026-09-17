import penglang as pl
while True:

    answer = pl.penguin_ask("give number to john (or 'exit'): ")

    try:
        if int(answer) % 2 == 0:
            pl.say("john: that even")
        elif int(answer) % 2 == 1:
            pl.say("john: that odd")
    except ValueError:
        if answer == "exit":
            pl.say("john finished his service")
            break
        else:
            pl.say("john: that is no number")


