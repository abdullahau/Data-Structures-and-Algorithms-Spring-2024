from functools import reduce

def find(t):
    return reduce(lambda x, y: x + y, t) - len(t) + 1