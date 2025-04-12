# core/rpt/human.py

from core.rpt.mind import Mind
from core.rpt.body import Body

class Human:
    def __init__(self):
        self.__mind = Mind()
        self.__body = Body()

        # Recursive link
        self.__mind._Mind__body = self.__body
        self.__body._Body__mind = self.__mind

    def boot_self_reflection(self):
        print("🧠 Human initialized: Recursive Mind ↔ Body loop active.")

    def get_memory(self):
        return self.__mind.get_memory()

    def get_animal(self):
        return self.__body.get_animal()

