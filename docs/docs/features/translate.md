# Translating

Penguins and dogs cannot *converse* with each other.  
They want to converse with each other.

That's why they made a penguin translate machine.  

??? question "Why do dogs want to talk. Aren't they weird?"
    You have never heard of unity in your entire life.  

    How are you going to work together with your friends[^1]?
    [^1]: If you have any.


## Basics
The penguin translate machine has a `translate_from`, and a `translate_to`.  
Translate from is the one that came first,  
and translate to is the one you want.

!!! quote "Penguin"
    I thought I fell,  
    Ante is so high,  
    One stopping burger,  
    ??? question "A burger?"
        It's a sandwich.
        ??? question "A sandwich?"
            It's 2 bread top and bottom with things in the middle.
            ??? question "Bread?"
                Good penguin food.

        !!! note "The above may be controversial, but who cares?"
    Lie all night.  
    *Ooowouh, ooowouh!*  
    When, I *translate from*,  
    I get the language it was.  
    If a dog speaks dog,  
    ??? question "A dog speaks dog?"
        It's common knowledge.  
        Did you get sweesh swashed?
    Dog is that language,  
    If it gets translated,  
    Into a penguin-understandable thing,  
    It is **translated to**.
    ??? question "To what?"
        To your brain.  
        ??? question "I'm not that smart in maths[^2]. What did you say?"
            I said it went to your brain.
            [^2]: It's not maths.
    *Intense jazz plays*

For example,   
If you have a dog that says "woof woof",  
and you have a penguin that says "buaak buaak",  
you may be interested in this.  
```python linenums="1"
import penglang as pl
import penglang.modules.pengtranslate as pt

pl.say(
    pt.PenguinTranslateMachine(
        translate_from="woof woof",
        translate_to="buaak buaak",
    ).translate("woof. i am dog. woof.")

)
```
Penguins might get:
```
buua.aiaamadug.abuua.
```
Penguins will understand what it means.

## With inverse and back

Penguins can make letters mapped to their counterparts. For example:

```python linenums="1"
import penglang as pl
import penglang.modules.pengtranslate as pt

text = pt.PenguinTranslateMachine(
    ps.alphabet[::-1],
    
).translate(
    "hello world"
)

pl.say(text)

```

will say:
```
svool dliow
```

This is because A -> Z, B -> Y, and so on.  

??? question "What does it mean?"
    For example,  
    The first letter of the alphabet is A, and the last is Y.  
    The second letter of the alphabet is B, and the second last is V.  

    Wait...

    ??? question "I have waited long and there has been nothing."
        A rhetorical question is a question that doesn't want an answer.

## Making units
Automatically, your `translate_to` is by letter.  
If you want to stitch up your letters,  
that's called a word according to penguins.

`translate_to` can be: `["banana", "horse", "penguin"]` and it will replace the whole word.

## How it works
### When making a new translating machine
1. At PengTranslate, a penguin goes to the Translate Factory™.
2. They take your `translate_to` and `translate_from`.
3. They do important checks.  
    1. Check if your `translate_to` is anything.  
        1. If not:
        2. Go to PengSymbol
        3. Get alphanumerics.
    2. Check if your `translate_to` is a number.
        1. If so:
        2. String it.
    3. Check if your `translate_to` is a string.
        1. If so:
        2. List it.
    4. Check if your `translate_from` is anything.
        1. If not:
        2. Go to PengSymbol
        3. Get alphanumerics.
    5. Check everything else.
    6. Stich everything up with PengIterable's `list_combine` into `translate_key`.

### When translating a text
1. Take the text, and turn it into a list.
2. Make a loop for each letter in the text.
    1. Make that letter into `translate_key`'s letter corresponding to that key's letter.
    2. If the letter corresponding to that key is not found: continue.
3. Return the text joined.