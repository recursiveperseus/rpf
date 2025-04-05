from abc import ABC, abstractmethod
from .memory_node_interface import MemoryNodeInterface

class NodeInterface(ABC):
    @abstractmethod
    def receive_memory(self, memory: MemoryNodeInterface) -> None:
        pass

    @abstractmethod
    def send_memory(self) -> MemoryNodeInterface:
        pass

    @abstractmethod
    def merge(self, other: 'NodeInterface') -> None:
        pass
