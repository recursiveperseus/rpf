from core.memory import MemoryNode
from typing import List
from core.ghost_log import GhostLog

class FeedbackLoop:
    def __init__(self, seed: MemoryNode):
        self.history: List[MemoryNode] = [seed]
        self.current = seed
        self.logger = GhostLog()
        self.logger.write(f"Seed memory initialized with entropy {seed.entropy()}")

    def step(self):
        reflection = self.current.reflect()
        self.current.link_child(reflection)
        self.history.append(reflection)
        self.logger.write(f"Reflected node with entropy {reflection.entropy():.4f}")
        self.current = reflection
        print(f"🔁 Step: Entropy = {reflection.entropy():.4f} | Total nodes: {len(self.history)}")

    def run(self, cycles: int = 5):
        print(f"🌀 Running feedback loop for {cycles} cycles...\\n")
        for _ in range(cycles):
            self.step()
        print("\\n🗃 Ghost Snapshot:")
        print(self.logger.snapshot())

    def reset(self):
        self.current = self.history[0]
        self.history = [self.current]
        print("♻️ Loop reset to seed memory.")

