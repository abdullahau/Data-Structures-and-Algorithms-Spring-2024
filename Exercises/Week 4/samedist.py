def find(t):
    last_index = {}
    d = 0
    for i, v in enumerate(t):
        if v not in last_index:
            last_index[v] = i
        else:
            d = max(d, i - last_index[v]) 
    return d