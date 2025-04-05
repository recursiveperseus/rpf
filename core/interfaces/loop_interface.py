from abc import ABC, abstractmethod
from .memory_node_interface import MemoryNodeInterface

class LoopInterface(ABC):
    @abstractmethod
    def start(self, node: MemoryNodeInterface) -> None:
        pass

    @abstractmethod
    def step(self) -> None:
        pass

    @abstractmethod
    def terminate(self) -> None:
        pass
