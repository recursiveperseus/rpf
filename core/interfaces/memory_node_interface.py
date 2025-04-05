from abc import ABC, abstractmethod
from typing import Dict

class MemoryNodeInterface(ABC):
    @abstractmethod
    def compress(self) -> Dict:
        pass

    @abstractmethod
    def reflect(self) -> 'MemoryNodeInterface':
        pass

    @abstractmethod
    def link_child(self, child: 'MemoryNodeInterface') -> None:
        pass

    @abstractmethod
    def entropy(self) -> float:
        pass
