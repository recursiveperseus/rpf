from agents import Agent
from ask import handle_ask
from map import draw_memory_tree
from message_router import MessageRouter
from debate_manager import DebateManager

def launch_shell():
    print("\n🤖 Multi-Agent Recursive Debate Shell")
    print("Type `help` to see available commands.\n")

    # Create agents
    agents = {
        "alpha": Agent("alpha", "I am alpha.", entropy_val=0.2),
        "beta": Agent("beta", "I am beta.", entropy_val=0.8),
    }
    current = agents["alpha"]

    # Register in router
    router = MessageRouter()
    for name, agent in agents.items():
        router.register(name, agent)

    # Initialize Debate Manager
    debate_manager = DebateManager(agents)

    while True:
        cmd = input(f"[{current.name}] rpf > ").strip()

        if cmd == "help":
            print("""\nAvailable commands:
  agent <name>         → Switch agent
  reflect              → Reflect one step
  status               → Show current node status
  ask <question>       → Reflective question
  map                  → Show memory tree
  send <msg> <to>      → Send message to another agent
  inbox                → Show last 3 received messages
  debate               → Start a recursive debate between agents
  exit                 → Quit shell""")
        elif cmd.startswith("agent "):
            name = cmd[6:].strip()
            if name in agents:
                current = agents[name]
                print(f"✅ Switched to agent: {name}")
            else:
                print(f"❌ Agent '{name}' not found.")
        elif cmd == "reflect":
            current.reflect()
        elif cmd == "status":
            print(current.status())
        elif cmd.startswith("ask "):
            q = cmd[4:].strip()
            current.ask(handle_ask, q)
        elif cmd == "map":
            current.map(draw_memory_tree)
        elif cmd.startswith("send "):
            parts = cmd.split()
            if len(parts) < 3:
                print("❌ Use format: send <message> <to_agent>")
            else:
                msg = " ".join(parts[1:-1])
                to_agent = parts[-1]
                router.send_message(current.name, to_agent, msg)
        elif cmd == "inbox":
            messages = [
                node for node in current.loop.history
                if node.label and ".message" in node.label
            ]
            print(f"📥 Inbox ({len(messages)} messages):")
            for m in messages[-3:]:
                print(f"🧠 {m.label} → {m.data}")
        elif cmd == "debate":
            debate_manager.start_debate()
        elif cmd == "exit":
            print("👋 Exiting multi-agent shell.")
            break
        else:
            print("❓ Unknown command. Type `help`.")

if __name__ == "__main__":
    launch_shell()
