class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def check(node):
    leaf_depth = set()
    helper(node, 0, leaf_depth)
    return len(leaf_depth) <= 1

def helper(node, depth, leaf_depth):
    if len(node.children) == 0:
        leaf_depth.add(depth)
    else:
        for child in node.children:
            helper(child, depth + 1, leaf_depth)