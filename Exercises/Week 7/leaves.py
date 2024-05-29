class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    result = 0
    if len(node.children) == 0:
        return result + 1
    for child in node.children:
        result += count(child)
    return result