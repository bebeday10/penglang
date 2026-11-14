

from ..pengfancywindow import PenguinFancyWindow
from customtkinter import CTkLabel
from .. import pengfancywindowmanager as pfwm
class PenguinBadgeWindow(PenguinFancyWindow):
    def __init__(self, *args, fg_color=None, window_title = "Penguin Badge Window", size = "900x400", achievement_image: str | None = None, image_size: tuple[int, int] = (256, 256), badge_name: str = "Badge", badge_description: str = "Earned badge.", destroy_manager: pfwm.PenguinFancyWindowManager | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, window_title=window_title, size=size, **kwargs)
        self.add_frame("Main Frame", 20, 20, "top")
        if achievement_image:
            self.add_image("img", achievement_image, None, 10, 10, "left", image_size, self.widgets["Main Frame"])
        self.add_frame("Body Frame", 20, 20, "left", self.widgets["Main Frame"])
        self.add_widget(CTkLabel, "Title", 10, 10, "top", self.widgets["Body Frame"], None, 10, 3, font=("Roboto", 24, "bold"), text=badge_name)
        self.add_widget(CTkLabel, "Body", 10, 10, "top", self.widgets["Body Frame"], None, 10, 3, text=badge_description)
        if destroy_manager is not None:
            self.when_closed(destroy_manager.destroy)

