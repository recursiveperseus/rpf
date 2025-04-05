import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from core.memory import MemoryNode
from core.loop import FeedbackLoop

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

    print("\n✅ rPF boot complete. Recursive cycles executed.\n")

if __name__ == '__main__':
    main()
