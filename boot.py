import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from core.memory import MemoryNode
from core.loop import FeedbackLoop
from core.rpt.human import Human  # 🧬 rPT kernel import

def main():
    print("\n🚀 Booting rPF: Recursive Processing Framework\n")

    # Seed memory node
    seed = MemoryNode("The loop begins.", entropy_val=0.01)
    print("🧠 Seed Memory:", seed.compress())

    # Reflect seed for feedback
    reflection = seed.reflect()
    print("🪞 Reflected Memory:", reflection.compress())

    # Link reflection as child to seed
    seed.link_child(reflection)
    print("🔗 Updated Seed (linked to reflection):", seed.compress())
    print("🔗 Reflection's parent(s):", len(reflection.parents))

    # Launch feedback loop
    print("\n🔁 Launching recursive feedback loop...")
    loop = FeedbackLoop(seed)
    loop.run(5)

    # 🧬 Boot rPT Human kernel
    print("\n🔧 Loading rPT kernel: Mind ↔ Body recursive architecture")
    human = Human()
    human.boot_self_reflection()

    print("\n✅ rPF + rPT boot complete. Recursive cycles and cognition initialized.\n")

if __name__ == '__main__':
    main()

