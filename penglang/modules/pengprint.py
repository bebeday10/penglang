from .. import penglang as pl

def emergency_box(message, title="🚨 EMERGENCY 🚨",):
    pl.say_in_a_box(f"[bold bright_red]{message}[/bold bright_red]", title, "bold bright_red")

def info_box(message, title="Info ℹ️",):
    pl.say_in_a_box(f"[bold cyan]{message}[/bold cyan]", title, "bold cyan")

def warning_box(message, title="⚠️  Warning ⚠️",):
    pl.say_in_a_box(f"[bold yellow]{message}[/bold yellow]", title, "bold yellow")