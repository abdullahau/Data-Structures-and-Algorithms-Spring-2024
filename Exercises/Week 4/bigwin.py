def count(t):
    d = {}
    
    counter = 0
    for i, v in enumerate(t):
        if v not in d:
            d[v] = []
        d[v].append(i)
    
    for k, v in d.items():
        if k*2 in d:
            for i in v:
                for j in d[k*2]:
                    if j > i:
                        counter += 1
        
    return counter