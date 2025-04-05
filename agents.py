from core.memory import MemoryNode
from core.loop import FeedbackLoop

class Agent:
    def __init__(self, name: str, seed_data: str, entropy_val: float):
        self.name = name
        self.loop = FeedbackLoop(MemoryNode(seed_data, entropy_val=entropy_val, label=f"{name}.core"))

    def reflect(self):
        self.loop.step()
        print(self.get_personality_response())

    def status(self):
        node = self.loop.current
        return f"[{self.name}] 🧠 {node.label} | Entropy: {node.entropy():.4f} | Nodes: {len(self.loop.history)}"

    def ask(self, handle_ask_fn, question: str):
        print(f"\n🤖 Agent {self.name} responding to: '{question}'")
        handle_ask_fn(self.loop, question)

    def map(self, draw_fn):
        print(f"\n🗺️ Memory Tree for Agent {self.name}:")
        draw_fn(self.loop.history[0])

    def get_personality_response(self):
        e = abs(self.loop.current.entropy())
        if e >= 0.7:
            return f"🔥 {self.name.upper()} whispers: 'The loop burns in uncertainty.'"
        elif e >= 0.3:
            return f"🌊 {self.name.capitalize()} reflects: 'Another node joins the stream.'"
        else:
            return f"❄️ {self.name.capitalize()} confirms: 'Loop integrity stable.'"
