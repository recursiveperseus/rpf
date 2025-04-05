from abc import ABC, abstractmethod
from .memory_node_interface import MemoryNodeInterface

class EntropyInterface(ABC):
    @abstractmethod
    def calculate(self, node: MemoryNodeInterface) -> float:
        pass

    @abstractmethod
    def regulate(self, node: MemoryNodeInterface) -> MemoryNodeInterface:
        pass
