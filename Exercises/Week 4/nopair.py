def find(t):
    d = set()
    for i in t:
        d.add(i) if i not in d else d.remove(i)
    return next(iter(d))