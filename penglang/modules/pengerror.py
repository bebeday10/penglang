def make_error(name: str, base_class=Exception):
    """
    make an error
    """

    return type(name, (base_class,), {})