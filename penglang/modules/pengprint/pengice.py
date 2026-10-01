from os import terminal_size
import shutil as su

def get_ice_size(fallback: tuple[int, int] = (80, 24)) -> terminal_size:
    """
    get the size of the ice. for when a penguin wants a line that goes just right.

    Args:
        fallback (tuple[int, int], optional): if the ice is gone use this instead. Defaults to (80, 24).

    Returns:
        terminal_size: the ice size
    """
    return su.get_terminal_size(fallback)