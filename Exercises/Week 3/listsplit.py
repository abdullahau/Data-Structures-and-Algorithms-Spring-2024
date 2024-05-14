def count(t):
    l = t[0]
    a = []
    for i, v in enumerate(t):
        if v < l:
            l = v
            a = [i]
        elif v == l:
            a.append(i)
    result = a[-1] - a[0] 
    return result