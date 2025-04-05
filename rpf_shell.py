from core.memory import MemoryNode
from core.loop import FeedbackLoop

def launch_shell():
    print("\n🧠 Welcome to the rPF Interactive Shell")
    print("Type `help` to see available commands.\n")

    # Start seed + loop
    seed = MemoryNode("The loop begins.", entropy_val=0.01, label="genesis")
    loop = FeedbackLoop(seed)

    while True:
        cmd = input("rpf > ").strip()

        if cmd.lower() == "help":
            print("""
Available commands:
  reflect           → Create a new reflection (1 step)
  snapshot          → Show ghost memory log
  status            → Show current node entropy and count
  label <text>      → Set label for current memory node
  info              → Show current node's label, data, and entropy
  reset             → Reset loop to seed node
  exit              → Quit the shell
""")
        elif cmd.lower() == "reflect":
            loop.step()
        elif cmd.lower() == "snapshot":
            print(loop.logger.snapshot())
        elif cmd.lower() == "status":
            print(f"🧠 Current Entropy: {loop.current.entropy():.4f}")
            print(f"🔗 Total Nodes: {len(loop.history)}")
        elif cmd.startswith("label "):
            label = cmd[6:].strip()
            loop.current.label = label
            print(f"🏷️  Updated label to: {label}")
        elif cmd.lower() == "info":
            print(f"🧠 ID: {loop.current.id}")
            print(f"🏷️  Label: {loop.current.label}")
            print(f"📝 Data: {loop.current.data}")
            print(f"🔥 Entropy: {loop.current.entropy():.4f}")
            print(f"🔗 Parents: {len(loop.current.parents)} | Children: {len(loop.current.children)}")
        elif cmd.lower() == "reset":
            loop.reset()
        elif cmd.lower() == "exit":
            print("👋 Exiting rPF shell.")
            break
        else:
            print("❓ Unknown command. Type `help` for options.")

if __name__ == "__main__":
    launch_shell()
