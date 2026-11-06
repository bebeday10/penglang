from .. import pengfancywindow as pfw
from .. import pengfancywindowmanager as pfwm

class PenguinImageWindow(pfw.PenguinFancyWindow):
    def __init__(self, *args, image_path: str, fg_color=None, window_title = "Penguin Image Window", image_size = (256, 256), destroy_manager: pfwm.PenguinFancyWindowManager | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, window_title=window_title, size=f"{image_size[0] + 100}x{image_size[1] + 100}", **kwargs)
        self.add_image("img", image_path, image_size=image_size)
        if destroy_manager is not None:
            self.when_closed(destroy_manager.destroy)