# core/rpt/animal.py

class Animal:
    def __init__(self):
        self.__systems = [
            "Integumentary", "Skeletal", "Muscular", "Nervous", "Endocrine",
            "Cardiovascular", "Lymphatic", "Respiratory", "Digestive", "Urinary", "Reproductive"
        ]
        self.__instincts = {
            "seek_safety": 0,
            "seek_food": 0,
            "reproduce": 0
        }
        self.__evolutionary_memory = []

    def stimulate(self, stimulus_type):
        if stimulus_type in self.__instincts:
            self.__instincts[stimulus_type] += 1

    def adapt(self, outcome):
        self.__evolutionary_memory.append(outcome)

    def get_state(self):
        return {
            "instincts": self.__instincts,
            "evolutionary_memory": self.__evolutionary_memory,
            "systems": self.__systems
        }

