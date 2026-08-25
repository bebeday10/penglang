from concurrent.futures import ThreadPoolExecutor
from threading import Event
from ... import penglang as pl
from .. import pengsymbol as ps
from . import pengrandom as pr
from .. import pengiterable as pi
import os

class PenguinIceOfRandom:
    def __init__(self, random_list: list = list(map(str, ps.alphanums)), length=50):
        self.random_list = list(map(str, random_list))
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

    
