from dataclasses import dataclass
from . import pengprint as pr
from . import pengnoend as pne
import random as r
@dataclass
class PenguinRubberDuckFishVirusChecker:
    duck_name: str = "Duck"
    user_name: str = "You"
    adjectives: list | None = None
    colors: list | None = None
    delay: float = 0.05
    dynamic_delay: bool = True
    dynamic_sense: float = 1.6
    send_msg: str = "SN"
    bubble_size: int = 28
    def __post_init__(self):
        self.adjectives = self.adjectives or [
            "happy",
            "clear",
            "amazed",
            "undestands",
            "angry",
            "sad",
            "totally know",
            "beautiful",
            "clearly",
            "spectacularly",
            "messy",
            "bad",
            "good",
            "wrong",
            "correct",
            "thoughtfully",
            "sensically"
        ]
        self.colors = self.colors or [
            "red",
            "green",
            "orange",
            "yellow",
            "pink",
            "purple",
            "blue",
            "sky blue",
            "saharan yellow",
            "rice white",
            "toothbrushed",
            "turquoise",
            "navy blue",
            "sun yellow",
            "space black",
            "jamaican purple",
            "vibrant colors",
            "forest green",
            "heart pink",
            "chocolate brown",
            "sleepy dry grey",
            "golden yellow",
            "lava orange",
            "mushroom red"
        ]
    def talk_to_duck(self):
        while True:
            print(f"Talk to {self.duck_name}, paste some code, enter on a line saying '{self.send_msg}' to send. (or 'exit')")
            lines = []

            while True:
                line = input(">")
                if line == self.send_msg:
                    break

                lines.append(line)


            answer = "\n".join(lines).strip()
            if answer == "exit":
                break
            delay = self.delay
            if self.dynamic_delay:
                delay = delay / (len(answer.split()) ** self.dynamic_sense)
            pr.penguin_side_speech_bubble_typewrite(answer, penguin_looks=self.user_name, delay=delay, bubble_size=self.bubble_size)
            saying = self._duck_speech(answer)
            delay = self.delay
            if self.dynamic_delay:
                delay = delay / (len(saying.split()) ** self.dynamic_sense)
            pr.penguin_side_speech_bubble_typewrite(saying, penguin_looks=f"{self.duck_name}", delay=delay, bubble_size=self.bubble_size)

    def duck_to_duck(self, starting_question: str = "placeholder", context_aware: bool = True, duck_amount: int = 2, question_only_context: bool = False):
        full_saying = starting_question
        saying = self._duck_speech(starting_question)
        full_saying += saying
        delay = self.delay
        if self.dynamic_delay:
            delay = delay / (len(saying.split()) ** self.dynamic_sense)
        pr.penguin_side_speech_bubble_typewrite(saying, penguin_looks=f"{self.duck_name} 1", delay=delay, bubble_size=self.bubble_size)
        while True:
            for i in range(1, duck_amount + 1):
                saying = self._duck_speech(full_saying if context_aware else starting_question if question_only_context else saying)
                full_saying += saying
                delay = self.delay
                if self.dynamic_delay:
                    delay = delay / (len(saying.split()) ** self.dynamic_sense)
                pr.penguin_side_speech_bubble_typewrite(saying, penguin_looks=f"{self.duck_name} {i}", delay=delay, bubble_size=self.bubble_size)




    def _duck_speech(self, replied: str):
        replied_split = pne.PenguinNoEnd(replied.split())
        start = r.randint(1, 10000)
        end = r.randint(1, 10000)
        chosen = self._fix_speech(replied_split[start:end])
        adj = r.choice(self.adjectives)
        color = r.choice(self.colors)
        duck_sayings = [
            f"i do not understand what you are saying please say {adj}",
            f"absolutely. seeing by '{chosen}', the last part seemt wrong. try adding {adj} things to it",
            f"that '{chosen}' part seems ok. i do not know about the other parts. wishing the best",
            f"right. you need {adj} less.",
            f"have you tried thinking about '{chosen}' harder?",
            f"be patient with me. look at '{chosen}', that's {adj}",
            f"you seen it wrong. look at '{chosen}'. that's wrong.",
            f"after thinking {adj}, see it from a different perspective.",
            f"what are you talking about on '{chosen}'? please tell me more info about that {adj}",
            f"right, '{chosen}' seems correct. the others... not so",
            f"sorry for my previous chat. it seems that '{chosen}' right here breaks my community guidelines. that means you need it better.",
            f"you forgot to put the return statement in '{chosen}'. this should help",
            f"after close investigation of '{chosen}' {adj}, you put + instead of +=.",
            f"yes, that is correct, {adj} for '{chosen}'",
            f"no, that's wrong, {adj} for '{chosen}'",
            f"i do not see anything wrong, '{chosen}'",
            "hello there",
            f"i am glad i helped you on '{chosen}'.",
            "this is impeccable to solve, sorry.",
            f"have you tried bringing a white twintailed {adj} elf with a purple hair named after a plant in to solve '{chosen}'?",
            f"have you tried reversing it around? i see '{chosen}'.",
            f"this isn't my field of work. ask someone {color} to help '{chosen}'",
            f"try changing up the setting of '{chosen}' to {color}.",
            f"just now i solved the problem according to your description of '{chosen}', in which i needed to change the {adj} to a better {color}.",
            f"try enabling Vibrant Colors to fix this '{chosen}' of yours. i do not know anything else about this {adj} problem.",
            f"change '{chosen}' to {color}. trust me, it will fix the underlying problem.",
            f"finally, i see the issue, '{chosen}' is {adj} not defined.",
            f"this seems like a circular {adj} import in '{chosen}'. try changing it {color}",
            f"reviewing the question, i've {adj} fixed it. here's the answer: {chosen[::-1]}",
            f"great for '{chosen}', we're getting closer to the answer at {color} pace",
            f"from the original question, '{chosen}' does not contribute anything. i recommend we do not talk about this {adj} again",
            f"your type annotations are being interpreted as real code. try changing '{chosen}' to something like {color}",
            f"this is {adj}, the answer is in reach because '{chosen}' is a big thing.",
            f"the problem is that '{chosen}' makes you think it's sensical. obviously, it's not.",
            f"something that immediately caught my {color} {adj} eye is '{chosen}', that is the problem we must be looking at here.",
            f"due to '{chosen}', the scheduling is wrong. however, we cannot change anything as it is a {adj} in the language.",
            f"this language, '{chosen}' i don't {adj} understand.",
            f"in '{chosen}' you are using the bitwise xor (^) instead of exponentiation (**). many people get this {adj}.",
            f"in '{chosen}', you are using tabs AND spaces. some languages don't like this {adj}, and they will most likely tell you in {color}. why did you ask me?",
            f"i see the ways {adj}. in '{chosen}', everything goes to 0, thus dividing by 0.",
            f"there is nothing wrong in '{chosen}'. i suggest it being something in the backend.",
            f"i specialize in this field, but '{chosen}' seems to be a subspecies of the field that only seasoned experts specializing specifically there knows. try asking another {color} duck near here."
        ]
        saying = r.choice(duck_sayings)
        return saying

    def _fix_speech(self, speech):
        return " ".join(speech)
