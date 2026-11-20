from dataclasses import dataclass
from .. import pengfancywindow as pfw
from rich import print
import customtkinter as ctk

from .pengant import PenguinAnt
from .pengantplace import PenguinAntPlace

@dataclass
class PenguinAntMachine:
    app_icon: str
    ants: list[PenguinAnt] | None = None
    locations: list[PenguinAntPlace] | None = None
    running: bool = False
    current_turn: int = 0
    current_ant: int = 1
    turn_cooldown: int = 1000


    def __post_init__(self):
        self.manager = pfw.PenguinFancyWindowManager()
        self.main_window = pfw.PenguinFancyWindow(window_title="Penguin Ant Window")
        self.main_window.app_icon(self.app_icon)
        self.main_window.add_textbox("log", 15, 15, "top")
        self.main_window.add_widget(ctk.CTkScrollableFrame, "stat frame", 15, 15, "top", orientation="horizontal")
        self.main_window.add_widget(ctk.CTkLabel, "pop", 10, 10, "left", owner=self.main_window.widgets["stat frame"], text=f"population: {self.current_ant}", width=300)
        self.main_window.add_widget(ctk.CTkScrollableFrame, "btn frame", 15, 15, "top", orientation="horizontal")
        self.main_window.add_button("stop btn", self.stop, 10, 10, "left", "Stop ants", self.main_window.widgets["btn frame"])
        self.main_window.protocol("WM_DELETE_WINDOW", self.stop)
        self.locations = self.locations or [PenguinAntPlace("Colony")]
        self.ants = self.ants or [PenguinAnt(self, f"#{self.current_ant}")]
        self.current_ant += 1

        
    def start(self):
        self.running = True
        
        self.turn()
        self.manager.run()
        
    def add_text(self, text: str = ""):
        self.main_window.widgets["log"].configure(state="normal")
        self.main_window.widgets["log"].insert("end", f"\n{text}")
        self.main_window.widgets["log"].configure(state="disabled")
    def stop(self):
        self.running = False
        self.manager.destroy()
    def turn(self):
        self.current_turn += 1
        events = [ant.turn() for ant in self.ants.copy()]
        events = self.filter_events(events)
        self.add_text(f"[Turn {self.current_turn}] {', '.join(events)}")
        self.update()
        if self.running:
            self.main_window.after(self.turn_cooldown, self.turn)

    def filter_events(self, events):
        return [event for event in events if event]

    def update(self):
        self.main_window.configure_widget("pop", text=f"population: {self.current_ant}")
