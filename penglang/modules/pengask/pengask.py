from dataclasses import dataclass
from . import pengquestion as pq
from ... import penglang as pl

@dataclass
class PenguinAsker:
    """
    Examples:
        {
            "question": "{answer} is cool"
        }
    """
    questions: dict[str, str]

    def ask_questions(self) -> list[str]:
        answers = []

        for question, answer in self.questions.items():
            question_answer = pq.PenguinQuestion(question).ask()
            answers.append(question_answer)
            if answer:
                pl.say(answer.format(answer=question_answer))

        return answers
