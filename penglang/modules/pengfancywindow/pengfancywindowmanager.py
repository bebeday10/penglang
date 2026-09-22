import customtkinter as ctk
import tkinter as tk

class PenguinFancyWindowManager(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("1280x720")
        self.title("penguin")
        self.wait = self.after

    def run(self):
        self.withdraw()
        self.mainloop()

    def stop(self):
        self.destroy()
