from dataclasses import dataclass
from typing import Literal
from . import pengcustomersupportdata as pcsd
from .. import pengrandom as pr
from .. import pengiterable as pi
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

    
    def to_backwards_customer_support_brain(self, lowercase: bool = False):
        clean_data = "".join(char for char in self.data if char.isalnum() or char.isspace())
        if lowercase:
            clean_data = clean_data.lower()

        words = clean_data.split()
        brain: dict[tuple[str, ...], dict[str, int]] = {}

        for i in range(self.model, len(words)):
            current_word = tuple(words[i - self.model + 1:i + 1])
            previous_word = words[i - self.model]

            if current_word not in brain:
                brain[current_word] = {}

            brain[current_word][previous_word] = brain[current_word].get(previous_word, 0) + 1

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

    def talk_to_customer_support(self, words_to_generate = 100, talk_algorithm=pr.random_decisions, direction: Literal["front", "back", "both"] = "front", return_instead: bool = False, prequestion: str = ""):
        """
        Talk to customer support

        Args:
            words_to_generate (int, optional): Amount of words to generate. Defaults to 100.
            talk_algorithm (Callable, optional): Algorithm that chooses words. Defaults to pr.random_decisions (classic).

        ## Qualify For An Algorithm:
            Receives infinite keyword arguments, of which is a dictionary of dict[str (next word), int (chance)].
            Returns a list.
            Next word has to be the first item in said list.

        """
        while True:
            if not return_instead:
                question = input("Put a topic or 'exit'... > ")
                if question == "exit":
                    break
            else:
                question = prequestion
            question = "".join(char for char in question if char.isalnum() or char.isspace())
            if not direction == "both":
                try:
                    if direction == "front":
                        current_word = tuple(question.split()[(0-self.model):])
                    else:
                        current_word = tuple(question.split()[:self.model])
                    generated_output = [question]
                except IndexError:
                    print(f"have atleast {self.model} words")
                    continue

                for _ in range(words_to_generate):
                    if current_word in self.brain:
                        try:
                            next_word: str = talk_algorithm(**self.brain[current_word])[0]
                        except IndexError:
                            continue
                        if direction == "back":
                            generated_output.insert(0, next_word)
                            current_word = (next_word, *current_word[:-1])
                        else:
                            generated_output.append(next_word)
                        
                            current_word = (*current_word[1:], next_word)
                    else:
                        break
                if not return_instead:
                    print(" ".join(generated_output))
                else:
                    return generated_output
            else:
                generated_output = [question]
                self.brain = self.to_backwards_customer_support_brain()
                generated_output = self.talk_to_customer_support(words_to_generate // 2, talk_algorithm, "back", True, question)
                self.brain = self.to_customer_support_brain()
                generated_output += self.talk_to_customer_support(words_to_generate // 2, talk_algorithm, "front", True, question)[1:]

                if not return_instead:
                    print(" ".join(generated_output))
                else:
                    return generated_output

    def choose_last(self, **chances):
        return [pi.index_dictionary(chances, -1, "key")]

    def choose_first(self, **chances):
        return [pi.index_dictionary(chances, 0, "key")]

    def choose_n(self, n, **chances):
        """
        Choose nth (zero-indexed) in word chances. Use as ``lambda **chances: choose_n(1, **chances)``

        Args:
            n (int): chance choose
        """
        for i in range(n, -1, -1):
            try:
                return [pi.index_dictionary(chances, n, "key")]
            except pi.PenguinIndexError:
                pass

        return pr.random_decisions(**chances)

    def choose_word(self, words: list[str], **chances):
        for word in words:
            if word in chances:
                return [word]

        return pr.random_decisions(**chances)