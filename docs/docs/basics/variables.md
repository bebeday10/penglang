# Variables
Penguins think.  
They think a lot.
Like... a lot a lot.  
Like too much.  
Well, the penguins need memory.  
!!! note
    Do not fear the "memory". It will not eat the RAM. Like a bit.  
    But it is like a bit.  
    Do not fear.
    

We have made the memory thing.  
Make sure you remember.

```python title="variables.py" linenums="1" hl_lines="3 4"
import penglang.penglang as pl # (1)!

pl.penguin_variable("banana", 2) # (2)!
better_banana = 2 # (3)!

pl.say(pl.banana) # (4)!
pl.say(better_banana) # (5)!
```

1. use this way if you want **runtime** variables.
2. the authentic, *PengLang* way of making variables. Very janky.
3. the pythonic way of making variables. not full *PengLang*, but recognized if you want a less janky way of coding.
4. use the module name when using the authentic way.
5. use no module name when using the pythonic way.