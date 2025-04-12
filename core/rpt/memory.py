# core/rpt/memory.py

class Memory:
    def __init__(self):
        self.__short_term = []
        self.__long_term = []
        self.__compressed_insight = None

    def store(self, data, importance=0.5):
        if importance > 0.7:
            self.__long_term.append(data)
        else:
            self.__short_term.append(data)

    def compress(self):
        # Simulate compression (reflection + entropy reduction)
        summary = f"Memory compressed: {len(self.__short_term)} short-term / {len(self.__long_term)} long-term"
        self.__compressed_insight = summary
        return summary

    def retrieve(self):
        return {
            "short_term": self.__short_term,
            "long_term": self.__long_term,
            "compressed": self.__compressed_insight
        }

