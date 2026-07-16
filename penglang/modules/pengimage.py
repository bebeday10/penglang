import ascii_magic as am

def make_text_picture(dir_to_img, size=120):
    """
    make a picture from text

    Args:
        dir_to_img (_type_): _description_
        size (int, optional): _description_. Defaults to 120.
    """
    output = am.from_image(dir_to_img)
    output.to_terminal(columns=size)



