class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    depths = []
    helper(node, 0, depths)
    return sum(depths)

def helper(node, depth, depths):
    depths.append(depth)
    for child in node.children:
        helper(child, depth + 1, depths)