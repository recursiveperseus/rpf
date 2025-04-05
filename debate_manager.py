from core.memory import MemoryNode

class DebateManager:
    def __init__(self, agents, max_rounds=10, entropy_threshold=0.05):
        self.agents = agents
        self.max_rounds = max_rounds
        self.entropy_threshold = entropy_threshold
        self.current_debate_round = 0

    def start_debate(self):
        print("\n💬 Starting the recursive debate between agents...\n")
        while self.current_debate_round < self.max_rounds:
            self.debate_round()
            if self.check_debate_termination():
                break
        print("\n✅ Debate concluded.")

    def debate_round(self):
        self.current_debate_round += 1
        print(f"🔄 Debate Round {self.current_debate_round} begins.")

        for agent_name, agent in self.agents.items():
            self.debate(agent)

    def debate(self, agent):
        print(f"💭 {agent.name} begins reflecting...")
        agent.reflect()  # Each agent reflects on its position
        self.mutate_and_respond(agent)
        self.share_memory(agent)

    def mutate_and_respond(self, agent):
        reflection = agent.loop.current.reflect()  # Reflect and mutate the response
        reflection.data = f"Reflection #{self.current_debate_round}: {reflection.data}"

        # Create a counterpoint (mutation)
        counterpoint = MemoryNode(data=f"Counterpoint: {reflection.data}", entropy_val=reflection.entropy(), label=f"{agent.name}.counterpoint")
        agent.loop.current.link_child(counterpoint)
        agent.loop.history.append(counterpoint)

        print(f"💬 {agent.name} responds with counterpoint: {counterpoint.data}")

    def share_memory(self, agent):
        # Share the last n memories across agents
        for other_agent_name, other_agent in self.agents.items():
            if other_agent_name != agent.name:
                shared_memories = agent.loop.history[-3:]  # Share last 3 memories
                for mem in shared_memories:
                    copied_mem = MemoryNode(mem.data, entropy_val=mem.entropy(), label=f"shared.{agent.name}.{mem.label}")
                    other_agent.loop.current.link_child(copied_mem)
                    other_agent.loop.history.append(copied_mem)

                print(f"🔄 Memory shared from {agent.name} to {other_agent_name}")

    def check_debate_termination(self):
        # Check if the entropy of the last responses is below the threshold to end the debate
        for agent_name, agent in self.agents.items():
            last_reflection = agent.loop.history[-1] if agent.loop.history else None
            if last_reflection and abs(last_reflection.entropy()) < self.entropy_threshold:
                print(f"🛑 Debate terminated due to low entropy.")
                return True
        return False

