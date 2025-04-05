from core.memory import MemoryNode

class MessageRouter:
    def __init__(self):
        self.registry = {}

    def register(self, agent_name: str, agent_obj):
        self.registry[agent_name] = agent_obj

    def send_message(self, from_agent: str, to_agent: str, content: str):
        if to_agent not in self.registry or from_agent not in self.registry:
            print("❌ One or both agents not found.")
            return

        sender = self.registry[from_agent]
        receiver = self.registry[to_agent]

        # Store message as node in receiver
        msg_node = MemoryNode(data=content, entropy_val=0.1, label=f"{from_agent}.message")
        receiver.loop.current.link_child(msg_node)
        receiver.loop.history.append(msg_node)

        print(f"📨 {from_agent} → {to_agent}: '{content}' stored as {msg_node.label}")

        # 🤖 Auto-response
        reflection = msg_node.reflect()
        reflection.data = f"Response to '{msg_node.data}'"
        reflection.label = f"{to_agent}.reply"
        reflection._entropy *= -1

        sender.loop.current.link_child(reflection)
        sender.loop.history.append(reflection)

        print(f'🤖 {to_agent} auto-responded to {from_agent}: "{reflection.data}"')

        # Share memory between agents
        self.share_memory(from_agent, to_agent)

    def share_memory(self, from_agent: str, to_agent: str):
        sender = self.registry[from_agent]
        receiver = self.registry[to_agent]

        # Share the last n memories from sender to receiver
        shared_memories = sender.loop.history[-3:]  # Sharing last 3 memories for learning
        for mem in shared_memories:
            # Copy the memory to the receiver's pool
            copied_mem = MemoryNode(mem.data, entropy_val=mem.entropy(), label=f"shared.{from_agent}.{mem.label}")
            receiver.loop.current.link_child(copied_mem)
            receiver.loop.history.append(copied_mem)
        
        print(f"🔄 Memory shared from {from_agent} to {to_agent}")
