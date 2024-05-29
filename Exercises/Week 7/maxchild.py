class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    result = len(node.children)
    for child in node.children:
        result = max(result, count(child))
    return result