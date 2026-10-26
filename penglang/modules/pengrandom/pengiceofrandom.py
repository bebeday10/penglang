from concurrent.futures import ThreadPoolExecutor
from threading import Event
from ... import penglang as pl
from ..pengsymbol import pengsymbol as ps
from . import pengrandom as pr
from .. import pengiterable as pi
import os
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress
import time as t
import psutil as pu
from datetime import timedelta, datetime, timezone
import uuid

class PenguinIceOfRandom:
    def __init__(self, random_list: list = list(map(str, ps.alphanums)), length=50):
        self.random_list = list(pi.list_to_dict(list(map(str, random_list)), None).keys())
        self.length = length

    def to_ice(self):
        pl.say("".join(pr.random_decisions(**pi.list_to_dict(self.random_list, 1), times=self.length)))

    def to_no_ice(self):
        return "".join(pr.random_decisions(**pi.list_to_dict(self.random_list, 1), times=self.length))

    def to_no_ice_target(self, target: str, worker_penguins=None, show_attempts: bool = False):
        if worker_penguins is None:
            worker_penguins = min(32, (os.process_cpu_count() or 1) + 4)
        stop_event: Event = Event()
        attempts = 0
        def search():
           while not stop_event.is_set():
               text = self.to_no_ice()

               if target in text:
                   stop_event.set()
                   return text

        def search_attempts():
            nonlocal attempts
            while not stop_event.is_set():
               text = self.to_no_ice()
               attempts += 1

               if target in text:
                   stop_event.set()
                   return text

        with ThreadPoolExecutor(max_workers=worker_penguins) as executor:
            if not show_attempts:
                futures = [
                    executor.submit(search)
                    for _ in range(worker_penguins)
                ]
            else:
                futures = [
                    executor.submit(search_attempts)
                    for _ in range(worker_penguins)
                ]
            for future in futures:
                result = future.result()
                if result is not None and not show_attempts:
                    return result
                elif result is not None:
                    return result, attempts

    def to_ice_target(self, target: str, worker_penguins=None, show_attempts: bool = False):
        if not show_attempts:
            pl.say(self.to_no_ice_target(target=target, worker_penguins=worker_penguins))
        elif show_attempts:
            result = self.to_no_ice_target(target=target, worker_penguins=worker_penguins, show_attempts=show_attempts)
            pl.say(result[0])
            pl.say(f"Attempts: {result[1]}")

    def to_detailed_ice_target(self, target: str, worker_penguins=None, fps: int = 60):
        with Live(refresh_per_second=fps) as l:
            if worker_penguins is None:
                worker_penguins = min(32, (os.process_cpu_count() or 1) + 4)
            stop_event: Event = Event()
            attempts = 0
            critical_hits = 0
            starting_time = t.time()
            critical_hit = None
            character_pool = ", ".join(self.random_list)
            pid = os.getpid()
            id = uuid.uuid4()

            def render(text):

                nonlocal critical_hit, critical_hits
                renderable = Text()
                if target in text:
                    stop_event.set()
                    renderable.append("Finished! Final text:\n")
                    renderable.append(f"{text}\n")

                current_time = t.time()
                seconds_elapsed = current_time - starting_time
                attempt_time = seconds_elapsed / attempts
                renderable.append(f"Word to find: {target}\n", "bold")
                attempts_estimate = int(1 / (1 - (1 - 1 / (len(self.random_list) ** len(target))) ** (self.length - len(target) + 1)))
                one_letter_cut_est = int(1 / (1 - (1 - 1 / (len(self.random_list) ** (len(target) - 1))) ** (self.length - (len(target) - 1) + 1)))
                estimated_time_end = (seconds_elapsed / attempts) * attempts_estimate
                true_estimated_time_end = timedelta(seconds=round(estimated_time_end - seconds_elapsed, 6)) 
                characters_generated = self.length * attempts
                cpu_usage = pu.cpu_percent()
                cpu_clock = pu.cpu_freq()
                ram_usage = pu.virtual_memory()
                page_swap = pu.swap_memory()
                network_usage = pu.net_io_counters()
                disk_usage = pu.disk_usage(str(pu.disk_partitions()[0].device))
                uptime = t.time() - pu.boot_time()
                disk_counter = pu.disk_io_counters()

                progress = (attempts / attempts_estimate) * 100
                renderable.append(f"Attempts: {attempts}\n")
                renderable.append(f"Estimated end: {attempts_estimate} attempts ({attempts_estimate * self.length} characters) ({timedelta(seconds=round(estimated_time_end, 6))}) ({round(progress, 6)}% ({true_estimated_time_end} left))\n")
                renderable.append(f"If you had just cut down a single letter: {one_letter_cut_est} attempts, and the difference: {attempts_estimate - one_letter_cut_est} attempts (Feel bad?)\n")
                renderable.append(f"How long an attempt gets made: {timedelta(seconds=round(attempt_time, 6))}\n")
                renderable.append(f"Characters generated: {characters_generated} ({self.length} characters per batch)\n")
                renderable.append(f"Critical hits made: {critical_hits} hits\n")
                renderable.append(f"Estimated critical hits: {len(self.random_list)} ({round((critical_hits / len(self.random_list)) * 100, 6)}%)\n")
                time_elapsed = timedelta(seconds=round(seconds_elapsed, 6))
                renderable.append(f"System uptime: {timedelta(seconds=round(uptime, 6))}\n")
                renderable.append(f"Time wasted: {time_elapsed} ({round(seconds_elapsed / uptime, 6)}% of system uptime)\n")
                renderable.append(f"Latest epoch time: {datetime.fromtimestamp(0, timezone.utc)} (UTC)\n")
                renderable.append(f"CPU usage: {cpu_usage}% (You probably can't see this because it keeps updating) ({worker_penguins} workers working on this)\n")
                renderable.append(f"CPU clock: {cpu_clock.current*1e6}Hz/{cpu_clock.max*1e6}Hz (min {cpu_clock.min*1e6}Hz)\n")
                renderable.append(f"RAM usage: {ram_usage.used}B/{ram_usage.total}B ({ram_usage.available}B vacant)\n")
                renderable.append(f"Page swap: {page_swap.used}B/{page_swap.total}B ({page_swap.percent}%) ({page_swap.free}B vacant) (Feel poor and slow?)\n")
                renderable.append(f"Network usage (we don't access the network): {network_usage.bytes_recv}B received, {network_usage.bytes_sent}B sent\n")
                renderable.append(f"{pu.disk_partitions()[0].device} disk usage: {disk_usage.used}B/{disk_usage.total}B ({disk_usage.free}B free)\n")
                renderable.append(f"System disk: Read count: {disk_counter.read_count} times ({disk_counter.read_bytes}B) ({disk_counter.read_time} milliseconds) Write count: {disk_counter.write_count} times ({disk_counter.write_bytes}B) ({disk_counter.write_time} milliseconds)\n")
                renderable.append(f"Process Identifier: {pid}\n")
                renderable.append(f"This run's UUID: {id}\n")
                renderable.append(f"Character pool ({len(self.random_list)} characters): {character_pool}\n")
                if target[:-1] in text:
                    critical_hit = text
                    critical_hits += 1
                if critical_hit is not None:
                    renderable.append("Critical hit:\n")
                    renderable.append(f"{critical_hit}\n")

                renderable.append("This attempt:\n")
                renderable.append(text)
                panel = Panel(renderable, title=f"Finding '{target}'...", subtitle=f"Attempts made: {attempts}")
                l.update(panel, refresh=True)




            def search_attempts():
                nonlocal attempts
                while not stop_event.is_set():
                    text = self.to_no_ice()
                    attempts += 1
                    render(text)
                    if target in text:
                        stop_event.set()
                        return text

            with ThreadPoolExecutor(max_workers=worker_penguins) as executor:
                futures = [
                    executor.submit(search_attempts)
                    for _ in range(worker_penguins)
                ]
                for future in futures:
                    result = future.result()

    
