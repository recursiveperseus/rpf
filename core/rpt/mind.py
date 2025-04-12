from core.rpt.memory import Memory

class Mind:
    def __init__(self, body=None):
        self.__memory = Memory()
        self.__body = body

    def get_memory(self):
        return self.__memory

    def reflect(self):
        print("🌀 Mind reflecting on memory...")
        return self.__memory.compress()

