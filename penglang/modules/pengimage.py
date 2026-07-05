import ascii_magic as am

def make_text_picture(dir_to_img, size=120):
    output = am.from_image(dir_to_img)
    output.to_terminal(columns=size)



