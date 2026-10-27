# Mathematical machine
Some penguins hated doing math.

So they made something to *do it for them*.

??? question "Are they lazy? What's wrong with them?"
    True.  
    How would **they** know?


## How does one math?
Simply,
```python linenums="1"
import penglang.modules.pengmath.pengmathmachine as pm
import penglang as pl
machine = pm.PenguinMathMachine()
long_depression = "1+2" # (1)!
pl.say(machine.evaluate_math(long_depression, step_show=True, main_step_show_only=False)) # (2)!
```

1. This is the long depression because many non-mathematicians don't know the answer to this expression.
2. The machine has decided to help them solve this seemingly impossible question.

It will then do math.

```python
1: ['1', '2'] (doing + (add)) # (1)!
2: [1.0, 2.0] (doing + (add)) (evaluates as 3.0) # (2)!
3.0
```

1. The machine will talk in a language no one understands.
2. The penguins are questioning how it did the impossible question.

Clearly so, it has done the question.

??? question "That's extremely hard. You're sure that's the correct answer?"
    We're not sure.  
    The math machine is.

## What can it **do**?
It can do many.

- Add (+)
- Subtract (-)
- Multiply (*)
- Divide (/)
- Floor divide (//)
- Exponentiation (** or ^)
- Factorial (!)
??? tip "Pro tip"
    The factorial is customized.  
    Doing a double factorial (!!), is !2. !n = ! of n amount.
    ??? question "What?"
        You'll figure it out.
- Termial
??? info "A termial is..."
    A termial is triangle.  
    Example: 3? = 3+2+1
- Remainder (%)
- Root \(r)
??? tip "Ultra Pro tip"
    nth root: _rn

## PEMDAS
Kinda. Penguins can also set their own rules if they're smart enough.