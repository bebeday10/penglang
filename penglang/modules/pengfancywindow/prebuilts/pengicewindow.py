from .. import pengfancywindow as pfw
from .. import pengfancywindowmanager as pfwm
from typing import Callable

class PenguinIceWindow(pfw.PenguinFancyWindow):
    def __init__(self, *args, fg_color=None, window_title = "Penguin Ice Window", size = "1280x720", manager: pfwm.PenguinFancyWindowManager, keywords: dict[str, Callable] = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, window_title=window_title, size=size, **kwargs)
        self.add_frame("Main Frame", 30, 30)
        self.add_textbox("Main Textbox", owner=self.widgets["Main Frame"], side="top", x_space=30, y_space=20)
        self.widgets["Main Textbox"].configure(state="disabled")
        self.add_entry("Main Entry", owner=self.widgets["Main Frame"], command=self.check_for_keywords, side="top", x_space=30, y_space=20, placeholder_text="Type here...")
        self.add_button("Exit", text="Exit", command=manager.stop, owner=self.widgets["Main Frame"], side="top", x_space=30, y_space=20)
        self.keywords = keywords or {}

    def add_text(self, text: str):
        self.widgets["Main Textbox"].configure(state="normal")
        self.widgets["Main Textbox"].insert("end", f"\n{text}")
        self.widgets["Main Textbox"].configure(state="disabled")
    def check_for_keywords(self, event=None):
        result = None
        for keyword, when_seen in self.keywords.items():
            if self.get_entry("Main Entry").lower() == keyword:
                result = when_seen()
                break
        

        self.remove_entry_text("Main Entry")
        if result:
            return result