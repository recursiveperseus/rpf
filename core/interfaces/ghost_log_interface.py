from abc import ABC, abstractmethod

class GhostLogInterface(ABC):
    @abstractmethod
    def write(self, event: str) -> None:
        pass

    @abstractmethod
    def read_all(self) -> list[str]:
        pass

    @abstractmethod
    def snapshot(self) -> str:
        pass
