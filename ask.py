import random

def handle_ask(loop, question: str):
    print(f"🧠 Searching memory for: '{question}'")

    # Step 1: Find best matching memory by label
    matched = None
    for node in reversed(loop.history):
        if node.label and any(word in node.label.lower() for word in question.lower().split()):
            matched = node
            break

    if matched:
        print(f"🔍 Match found in: '{matched.label}'")
    else:
        print("🌀 No exact match. Starting with current memory.")
        matched = loop.current

    entropy = abs(matched.entropy())
    depth = min(7, max(1, int(entropy * 10)))  # Scales 0.0 → 1.0 to 1 → 7
    print(f"🔁 Entropy-Driven Reflection Depth: {depth} (entropy = {entropy:.4f})")

    # Step 2: Reflect recursively
    thoughts = []
    current = matched
    for i in range(depth):
        reflection = current.reflect()
        label = reflection.label or "unknown"
        sentence = reflect_thought(label, reflection.entropy())
        print(f"🔁 Step {i+1}: {sentence}")
        thoughts.append(sentence)
        current = reflection

    # Step 3: Final reflection
    print(f'🧠 Final Response: "{thoughts[-1]}"')

def reflect_thought(label: str, entropy: float) -> str:
    templates = [
        f"{label} is a mirror loop.",
        f"{label} is defined by its entropy: {entropy:.4f}",
        f"{label} reflects a truth in disguise.",
        f"{label} remembers to evolve.",
        f"{label} is not what it was before reflection."
    ]
    return random.choice(templates)
