from dataclasses import dataclass
from .. import pengfancywindow as pfw
from rich import print
import customtkinter as ctk
from .. import pengrandom as pr
from .pengant import PenguinAnt
from .pengantplace import PenguinAntPlace
from .pengantenemy import PenguinAntEnemy
from .pengenemynames import enemy_names

@dataclass
class PenguinAntMachine:
    app_icon: str
    ants: list[PenguinAnt] | None = None
    locations: list[PenguinAntPlace] | None = None
    running: bool = False
    current_turn: int = 0
    current_ant: int = 1
    turn_cooldown: int = 1000
    enemies: list[PenguinAntEnemy] | None = None
    enemy_chance: int | float = 20
    enemy_base_offense: int | float = 5
    enemy_base_defense: int | float = 5
    enemy_base_hp: int | float = 10


    def __post_init__(self):
        self.enemies = self.enemies or []
        self.locations = self.locations or [PenguinAntPlace("Colony")]
        self.ants = self.ants or [PenguinAnt(self, f"#{self.current_ant}")]
        self.manager = pfw.PenguinFancyWindowManager()
        self.main_window = pfw.PenguinFancyWindow(window_title="Penguin Ant Window")
        self.main_window.app_icon(self.app_icon)
        self.main_window.add_textbox("log", 15, 15, "top")
        self.main_window.add_widget(ctk.CTkScrollableFrame, "stat frame", 15, 15, "top", orientation="horizontal")
        self.main_window.add_widget(ctk.CTkLabel, "pop", 10, 10, "left", owner=self.main_window.widgets["stat frame"], text=f"population: {len(self.ants)}", width=300)
        self.main_window.add_widget(ctk.CTkLabel, "enemy count", 10, 10, "left", owner=self.main_window.widgets["stat frame"], text=f"enemies: {len(self.enemies)}", width=300)
        self.main_window.add_widget(ctk.CTkScrollableFrame, "btn frame", 15, 15, "top", orientation="horizontal")
        self.main_window.add_button("stop btn", self.stop, 10, 10, "left", "Stop ants", self.main_window.widgets["btn frame"])
        self.main_window.protocol("WM_DELETE_WINDOW", self.stop)

        self.current_ant += 1
        
        self.enemy_defense_offset = 0
        self.enemy_offense_offset = 0
        self.enemy_hp_offset = 0

        
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

        events = [entity.turn() for entity in (self.ants + self.enemies).copy()]
        events = self.filter_events(events)
        if pr.random_decimal(0, self.enemy_chance) <= 1:
            self.enemies.append(PenguinAntEnemy(self, pr.random_decision(*enemy_names), self.enemy_base_offense + self.enemy_offense_offset, self.enemy_base_defense + self.enemy_defense_offset, pr.random_decision(*self.locations), self.enemy_base_hp + self.enemy_hp_offset))
            self.enemy_offense_offset += pr.random_decimal(-0.5, 0.5)
            self.enemy_defense_offset += pr.random_decimal(-0.5, 0.5)
            self.enemy_hp_offset += pr.random_decimal(-5, 5)
            events.append(f"Enemy {self.enemies[-1].name} has appeared at {self.enemies[-1].location.name} with {self.enemies[-1].offense} offense {self.enemies[-1].defense} defense and {self.enemies[-1].hp} HP")
        self.add_text(f"[Turn {self.current_turn}] {', '.join(events)}")
        self.update()
        if self.running:
            self.main_window.after(self.turn_cooldown, self.turn)

    def filter_events(self, events):
        return [event for event in events if event]

    def update(self):
        self.main_window.configure_widget("pop", text=f"population: {len(self.ants)}")
        self.main_window.configure_widget("enemy count", text=f"enemy count: {len(self.enemies)}")
