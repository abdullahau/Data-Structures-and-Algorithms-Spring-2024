def find(t):
    sub = []
    for i in t:
        if i not in sub:
            sub.append(i)
        else:
            rep = i
    return sub[sub.index(rep) - 1]