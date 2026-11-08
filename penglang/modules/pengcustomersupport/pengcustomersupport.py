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

    def to_customer_support_brain(self, lowercase: bool = False):
        clean_data = "".join(char for char in self.data if char.isalnum() or char.isspace())
        if lowercase:
            clean_data = clean_data.lower()
        words = clean_data.split()
        brain: dict[str, dict[str, int]] = {}
        for i in range(len(words) - self.model):
            current_word = tuple(words[i:i + self.model])
            next_word = words[i + self.model]

            if current_word not in brain:
                brain[current_word] = {}

            brain[current_word][next_word] = brain[current_word].get(next_word, 0) + 1

        return brain

    def inspect_brain(self):
        print(f"Model: {self.model}")
        print(f"Brain length: {len(self.brain.keys())}")
        brain_branches = 0
        for brain_k, brain_v in self.brain.items():
            brain_branches += len(brain_v.keys())
        print(f"Words the brain can form: {brain_branches}")
        while True:
            question = input("Put a topic or 'exit'... > ")
            if question == "exit":
                break
            question = "".join(char for char in question if char.isalnum() or char.isspace())
            current_word = tuple(question.split()[(0-self.model):])
            all_weights = 0
            if current_word not in self.brain:
                print("Nothing found!")
                continue
            for v in self.brain[current_word].values():
                all_weights += v
            print(f"Possible words: {len(self.brain[current_word].keys())}")
            print(f"Total next words found in data: {all_weights}")
            for k, v in self.brain[current_word].items():
                print(f"Next word could be {k:-<20} {f"{v} words found in the data ":*<30}{f" ({(v / all_weights) * 100}% of it choosing it)":>50}")

    def talk_to_customer_support(self, words_to_generate = 100):
        while True:
            question = input("Put a topic or 'exit'... > ")
            if question == "exit":
                break
            question = "".join(char for char in question if char.isalnum() or char.isspace())
            try:
                
                current_word = tuple(question.split()[(0-self.model):])
                generated_output = [question]
            except IndexError:
                print(f"have atleast {self.model} words")
                continue

            for _ in range(words_to_generate):
                if current_word in self.brain:
                    try:
                        next_word: str = pr.random_decisions(**self.brain[current_word])[0]
                    except IndexError:
                        continue
                    generated_output.append(next_word)
                    current_word = (*current_word[1:], next_word)
                else:
                    break
            print(" ".join(generated_output))
