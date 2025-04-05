from abc import ABC, abstractmethod
from .memory_node_interface import MemoryNodeInterface

class MapInterface(ABC):
    @abstractmethod
    def map(self, node: MemoryNodeInterface) -> dict:
        pass

    @abstractmethod
    def visualize(self, node: MemoryNodeInterface) -> None:
        pass
