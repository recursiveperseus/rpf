# core/rpt/body.py

from core.rpt.animal import Animal

class Body:
    def __init__(self, mind=None):
        self.__animal = Animal()
        self.__mind = mind

    def get_animal(self):
        return self.__animal

