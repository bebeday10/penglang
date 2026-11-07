from dataclasses import dataclass
from . import pengcustomersupportdata as pcsd
from .. import pengrandom as pr
from rich import print
@dataclass
class PenguinCustomerSupport:
    data: str = pcsd.data
    model: int = 2
    def __post_init__(self):
        self.brain = self.to_customer_support_brain()

    def to_customer_support_brain(self):
        clean_data = "".join(char for char in self.data if char.isalnum() or char.isspace())
        words = clean_data.split()
        brain: dict[str, dict[str, int]] = {}
        for i in range(len(words) - self.model):
            current_word = tuple(words[i:i + self.model])
            next_word = words[i + self.model]

            if current_word not in brain:
                brain[current_word] = {}

            brain[current_word][next_word] = brain[current_word].get(next_word, 0) + 1

        return brain

    def talk_to_customer_support(self, words_to_generate = 100):
        while True:
            question = input("Put a topic or 'exit'... > ")
            if question == "exit":
                break
            try:
                
                current_word = tuple(question.split()[(0-self.model):])
                generated_output = list(current_word)
            except IndexError:
                print(f"have atleast {self.model} words")
                continue

            for _ in range(words_to_generate):
                if current_word in self.brain:
                    next_word: str = pr.random_decisions(**self.brain[current_word])[0]
                    generated_output.append(next_word)
                    current_word = (*current_word[1:], next_word)
                else:
                    break
            print(" ".join(generated_output))
        