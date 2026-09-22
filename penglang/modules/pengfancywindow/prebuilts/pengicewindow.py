from .. import pengfancywindow as pfw
from .. import pengfancywindowmanager as pfwm
from typing import Callable
import difflib as dl
import inspect
import _tkinter as _tk

class PenguinIceWindow(pfw.PenguinFancyWindow):
    def __init__(
            self,
            *args,
            fg_color=None,
            window_title = "Penguin Ice Window",
            size = "1280x720",
            manager: pfwm.PenguinFancyWindowManager,
            keywords: dict[str, Callable] = None,
            exit_button: bool = True,
            help: bool = True,
            keyword_not_found_message: str = "",
            close_matches: bool = True,
            close_match_sense: float = 0.6,
            has_exit_cmd: bool = True,
            exit_cmd: Callable | None = None,
            before_exit: Callable | None = None,
            extra_help: str = "",
            arg_split: str = " ",
            **kwargs
            ):

        super().__init__(*args, fg_color=fg_color, window_title=window_title, size=size, **kwargs)
        self.exit_cmd = exit_cmd or self.exit_command
        self.add_frame("Main Frame", 30, 30)
        self.add_textbox("Main Textbox", owner=self.widgets["Main Frame"], side="top", x_space=30, y_space=20)
        self.widgets["Main Textbox"].configure(state="disabled")
        self.add_entry("Main Entry", owner=self.widgets["Main Frame"], command=self.check_for_keywords, side="top", x_space=30, y_space=20, placeholder_text="Type here...")
        if exit_button:
            self.add_button("Exit", text="Exit", command=self.exit_command, owner=self.widgets["Main Frame"], side="top", x_space=30, y_space=20)
        self.manager = manager
        self.keywords = keywords or {}
        if help:
            self.keywords["help"] = self.help_keyword
        self.keyword_not_found_message: str = keyword_not_found_message
        self.close_matches = close_matches
        self.close_match_sense = close_match_sense
        self.before_exit = before_exit
        self.when_closed(self.exit_command)
        if has_exit_cmd:
            self.keywords["exit"] = self.exit_cmd
        self.arg_split = arg_split
        self.extra_help = extra_help
        

    def add_text(self, text: str = ""):
        self.widgets["Main Textbox"].configure(state="normal")
        self.widgets["Main Textbox"].insert("end", f"\n{text}")
        self.widgets["Main Textbox"].configure(state="disabled")
    def check_for_keywords(self, event=None):
        result = None
        entered = self.get_entry("Main Entry").lower().strip()
        dash_replace = "--dash-replace" in entered
        if dash_replace:
            entered = entered.replace("--dash-replace", "").strip()
            
        for keyword, when_seen in self.keywords.items():
            if entered == keyword:
                result = when_seen()
                break
        else:
            for keyword, when_seen in self.keywords.items():
                if entered.startswith(keyword):
                    kw_words = len(keyword.split(self.arg_split))
                    if self.arg_split.join(entered.split(self.arg_split)[:kw_words]) != keyword:
                        continue
                    args = entered.split(self.arg_split)
                    if dash_replace:
                        args = list(map(lambda x: x.replace("-", self.arg_split), args))
                    try:
                        result = when_seen(*args[kw_words:])
                    except TypeError:
                        self.add_text("that does not support that many keywords")
                    break
            else:
                if self.keyword_not_found_message:
                    self.add_text(self.keyword_not_found_message)
                if self.close_matches:
                    self.close_match_check(entered)
        
        try:
            self.remove_entry_text("Main Entry")
        except _tk.TclError:
            pass
        if result:
            return result

    def add_keywords(self, **keywords):
        self.keywords.update(keywords)

    def help_keyword(self, size="short"):
        """
        Show this help message.

        Sub-Keywords:
            size: After "help", put "long" or "short".
        """
        self.add_text("--- Help ---")
        for keyword, does in self.keywords.items():
            args = inspect.signature(does)
            docs = inspect.getdoc(does)
            if size == "short":
                self.add_text(f"{keyword}: {docs}")
            else:
                self.add_text(f"{keyword}:\n{does.__name__}:\n{docs}\nSub-keywords (Keyword=Default): {args}")
                self.add_text()
        self.add_text("--- Other ---")
        self.add_text("Use '--dash-replace' to replace all dashes with the sub-keyword split.")
        self.add_text(f"The current sub-keyword split is: '{self.arg_split}'.")
        self.add_text("--- Extra Help ---")
        self.add_text(self.extra_help)

    def close_match_check(self, message):
        close_matches = dl.get_close_matches(message, self.keywords.keys(), 10, self.close_match_sense)
        if close_matches:
            self.add_text("close matches found:")
            for i, match in enumerate(close_matches, 1):
                self.add_text(f"{i}: {match}")

        else:
            self.add_text("no close matches...")

    def exit_command(self):
        """Exit the window."""
        if self.before_exit:
            self.before_exit()
        self.manager.stop()
        