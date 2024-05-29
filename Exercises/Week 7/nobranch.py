class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

def check(node):
    result = []
    check_helper(node, (len(node.children) <= 1), result)
    if all(result):
        return True
    else:
        return False

def check_helper(node, length, result):
    result.append(length)
    for child in node.children:
        check_helper(child, (len(child.children) <= 1), result)