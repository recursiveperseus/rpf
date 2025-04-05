def draw_memory_tree(node, depth=0, prefix=""):
    print(prefix + "└── " + node.label)

    for i, child in enumerate(node.children):
        is_last = (i == len(node.children) - 1)
        child_prefix = prefix + ("    " if is_last else "│   ")
        draw_memory_tree(child, depth + 1, child_prefix)
