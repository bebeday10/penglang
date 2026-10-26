from dataclasses import dataclass
from ... import penglang as pl
from .. import pengsymbol as ps
from .. import pengiterable as pi
from typing import Literal
from functools import cache

@dataclass
class PenguinMathMachine:
    math_map: dict[
        str,
        Literal[
            "mul",
            "div",
            "pow",
            "add",
            "sub",
            "fac",
            "ter",
            "mod",
            "flodiv",
            "root"
        ]
    ] | None = None

    def __post_init__(self):
        self.math_map = self.math_map or {
            "!": "fac",
            "?": "ter",
            "**": "pow",
            "^": "pow",
            "r": "root",
            "*": "mul",
            "/": "div",
            "//": "flodiv",
            "%": "mod",
            "+": "add",
            "-": "sub"
        }
        
        self._step_count = 1

    def evaluate_math(self, math_string: str, step_show: bool = False, show_indent: bool = True, main_step_show_only: bool = False, indent=0):
        # this is unreadable so comments are needed
        evaluation_copy = None
        try:
            for str_check, do in self.math_map.items():
                # Check if any operator is in the string still

                if str_check in math_string:
                    evaluation_copy = math_string.replace(" ", "").strip().split(str_check) # the evaluation copy splits the sides of the op
                    pl.say(f"{("    "*indent) if show_indent else ""}{self._step_count}: {evaluation_copy} (doing {str_check} ({do}))") if step_show else None
                    self._step_count += 1
                    # for everything in the split side op
                    for split_eval_num, split_evaluate in enumerate(evaluation_copy):
                        # if ANY of the characters are not a number, decimal point, or the symbols:
                        if any(i not in list(map(str, [*ps.numbers, ".", *list("pie")])) for i in split_evaluate):
                            
                            evaluation_copy[split_eval_num] = self.evaluate_math(split_evaluate, (step_show if not main_step_show_only else False), show_indent, main_step_show_only, indent+1)
                            # at this point the side has been evaluated.
                            pl.say(f"{("    "*indent) if show_indent else ""}{self._step_count}: {evaluation_copy} (doing {str_check} ({do}))") if step_show else None
                            self._step_count += 1

                    try:
                        # Where the evaluation for the evaluated starts
                        # Factorial Termial check because parser needs second number
                        if do == "fac" or do == "ter":
                            if not evaluation_copy[1]:
                                evaluation_copy[1] = "1"

                        

                        # -- Symbol conversion --
                        for num_math, math_conversion_objs in enumerate(evaluation_copy):
                            if isinstance(evaluation_copy[num_math], str):
                                evaluation_copy[num_math] = evaluation_copy[num_math].replace("pi", "3.141592653589793")
                                evaluation_copy[num_math] = evaluation_copy[num_math].replace("e", "2.718281828459045")
                                if evaluation_copy[num_math] == "":
                                    evaluation_copy[num_math] = "0"

                        # Here EVERYTHING BEFOREHAND has been evaluated. 
                        # Convert strings to floats
                        evaluation_copy = list(map(float, evaluation_copy))

                        # --- Actually do math ---
                        answer = self._math_doing(evaluation_copy, do)
                        

                        pl.say(f"{("    "*indent) if show_indent else ""}{self._step_count}: {evaluation_copy} (doing {str_check} ({do})) (evaluates as {answer})") if step_show else None
                        self._step_count += 1
                    except Exception as e:
                        pl.say(f"your math is bad (answer will now be 0): {e}")
                        answer = 0
                    
            return answer

        except Exception as e:
            pl.say(f"your math is bad: {e}")


    def reset_step_count(self):
        self._step_count = 1

    def _math_doing(self, evaluation_copy: list[float], do) -> float:
        if do == "fac":
            answer = evaluation_copy[0]
            for i in range((int(evaluation_copy[1]) % int(answer)) - 1, int(answer), int(evaluation_copy[1])):
                
                i = i if i >= 1 else 1

                answer *= i
        elif do == "ter":
            answer = evaluation_copy[0]
            for i in range((int(evaluation_copy[1]) % int(answer)) - 1, int(answer), int(evaluation_copy[1])):
                
                answer += i                

        elif do == "pow":
            answer = evaluation_copy[0]
            for doings in evaluation_copy[1:]:
                answer **= doings

        elif do == "root":
            answer = evaluation_copy[0]
            for doings in evaluation_copy[1:]:
                answer **= (1 / doings)
        elif do == "mul":
            answer = evaluation_copy[0]
            for doings in evaluation_copy[1:]:
                answer *= doings

        elif do == "flodiv":
            answer = evaluation_copy[0]
            for doings in evaluation_copy[1:]:
                answer //= doings
            

        elif do == "div":
            answer = evaluation_copy[0]
            for doings in evaluation_copy[1:]:
                answer /= doings

        elif do == "mod":
            answer = evaluation_copy[0]
            for doings in evaluation_copy[1:]:
                answer %= doings

        elif do == "add":
            answer = evaluation_copy[0]
            for doings in evaluation_copy[1:]:
                answer += doings

        elif do == "sub":
            answer = evaluation_copy[0]
            for doings in evaluation_copy[1:]:
                answer -= doings     

        return answer

    
                
