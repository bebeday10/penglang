from .. import pengfancywindow as pfw

class PenguinButtonWindow(pfw.PenguinFancyWindow):
    def __init__(self, *args, buttons: list = None, fg_color=None, window_title = "Penguin Fancy Window", size = "1280x720", self_destruct=True, destruct_manager=False, manager=None, **kwargs):
        super().__init__(*args, fg_color=fg_color, window_title=window_title, size=size, **kwargs)
        self.buttons = buttons or []
        self.current_selection = None
        self.self_destruct = self_destruct
        self.manager = manager
        self.destruct_manager = destruct_manager
        for button in self.buttons:
            self.add_button(f"{button} button", lambda button=button: self.set_selection(button), text=f"{button}")

    def set_selection(self, button): self.current_selection = button; self.manager.destroy() if self.destruct_manager and self.manager else self.destroy() if self.self_destruct else None
    def get_selection(self): self.wait_window(); return self.current_selection
