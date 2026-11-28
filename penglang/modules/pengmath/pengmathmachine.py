from copy import copy
from dataclasses import dataclass
import random
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


    def make_math(self, math_string: float | str, step_show: bool = False, show_indent: bool = True, main_step_show_only: bool = False, indent=0, variety: int = 5, max_steps=10):
        evaluation_copy = str(math_string)
        while self._step_count < max_steps:
            for str_check, do in self.math_map.items():
                    if str_check in evaluation_copy:
                        evaluation_copy = " ".join(evaluation_copy.replace(" ", " ").strip().split(str_check)) # the evaluation copy splits the sides of the op

            evaluation_copy_list = evaluation_copy.strip().split()
            evaluation_copy_list_copy = copy(evaluation_copy_list)
            for i, num in enumerate(evaluation_copy_list):
                evaluation_copy_list_copy[i] = f"{self._math_undoing(random.choice(list(self.math_map.values())), variety, num)}"
                if step_show:
                    pl.say(f"{"    "*indent if show_indent else ""}{self._step_count}: {num} -> {evaluation_copy_list_copy[i]}, {"".join(evaluation_copy_list_copy)}")
                self._step_count += 1

            evaluation_copy = " ".join(evaluation_copy_list_copy)

        return evaluation_copy

            



    def reset_step_count(self):
        self._step_count = 1

    def _math_undoing(self, do, variety, evaluation_copy):
        evaluation_copy = float(evaluation_copy)
        int_copy = float(evaluation_copy)
        if do == "fac":
            variety = random.randint(1, variety)
            int_copy = float(evaluation_copy)
            if int_copy >= 1 or variety >= 1:
                for i in range((int(variety) % int(evaluation_copy)) - 1, int(variety), int(variety)):
                    i = i if i >= 1 else 1
                    int_copy /= i
                    return f"{int_copy}!{variety}"
        if do == "ter":
            variety = random.randint(1, variety)
            int_copy = float(evaluation_copy)
            if int_copy > 1 or variety >= 1:
                for i in range((int(variety) % int(evaluation_copy)) - 1, int(variety), int(variety)):

                    int_copy -= i
                    return f"{int_copy-1}!{variety}"

        elif do == "pow":
            variety = random.randint(-variety, variety)
            variety = 1 if variety == 0 else variety
            int_copy **= (1 / variety)
            return f"{int_copy}^{variety}"

        elif do == "root":
            variety = random.randint(-variety, variety)
            int_copy **= variety
            return f"{int_copy}r{variety}"

        elif do == "mul":
            variety = random.uniform(-variety, variety)
            int_copy /= variety
            return f"{int_copy}*{variety}"

        elif do == "flodiv":
            variety = random.uniform(-variety, variety)
            int_copy *= variety
            return f"{int_copy}//{variety}"

        elif do == "div":
            variety = random.uniform(-variety, variety)
            int_copy *= variety
            return f"{int_copy}/{variety}"

        elif do == "mod":
            variety = random.uniform(-variety, variety)
            variety_2 = random.uniform(-variety, variety)
            variety_2 =  variety_2 * variety + int_copy
            return f"{variety_2} % {variety}"

        elif do == "add":
            variety = random.uniform(-variety, variety)
            int_copy -= variety
            return f"{int_copy}+{variety}"

        elif do == "sub":
            variety = random.uniform(-variety, variety)
            int_copy += variety
            return f"{int_copy}-{variety}"

        return str(evaluation_copy)
    


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

            answer -= 1                

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

    
                
