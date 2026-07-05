def make_thing(name, bases=(), things_it_has: list =None, things_it_can_do=None) -> type:
    attrs = things_it_has or {}
    methods = things_it_can_do or {}

    namespace = {
        "__init__": start_maker(things=attrs),
        "show": show_maker(things=attrs),
        "__repr__": show_maker(things=attrs),
        "__add__": lambda self, other: self.__class__.__name__ + "-" + other.__class__.__name__
    }
    namespace.update(methods)
    

    
    return type(name, bases, namespace)

def start_maker(things):
    def __init__(self, *values):
        for name, value in zip(things, values):
            setattr(self, name, value)

    return __init__

def show_maker(things):
    def show(self):
        parts = []
        for t in things:
            parts.append(f"{t}={getattr(self, t)}")
        return f"<{self.__class__.__name__} " + ", ".join(parts) + ">"
    
    return show