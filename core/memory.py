from typing import Dict, List, Optional
from core.interfaces.memory_node_interface import MemoryNodeInterface

class MemoryNode(MemoryNodeInterface):
    def __init__(self, data: str, entropy_val: float = 0.0, label: Optional[str] = None):
        self.data = data
        self.label = label or "unnamed"
        self._entropy = entropy_val
        self.children: List[MemoryNodeInterface] = []
        self.parents: List[MemoryNodeInterface] = []
        self.id = hash((data, self.label))
        self.version = 1

    def compress(self) -> Dict:
        return {
            'id': self.id,
            'label': self.label,
            'summary': self.data[:16] + "..." if len(self.data) > 16 else self.data,
            'entropy': self._entropy,
            'children': len(self.children),
            'parents': len(self.parents)
        }

    def reflect(self) -> 'MemoryNode':
        # Increment version on mutation
        new_label = f"{self.label}.v{len(self.children)+1}"
        return MemoryNode(data=self.data, entropy_val=-self._entropy, label=new_label)

    def link_child(self, child: 'MemoryNodeInterface') -> None:
        self.children.append(child)
        child.parents.append(self)

    def entropy(self) -> float:
        return self._entropy
