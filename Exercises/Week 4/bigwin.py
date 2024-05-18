def count(t):
    d = {}
    counter = {}
    
    for i, v in enumerate(t):
        if v not in d:
            d[v] = 1
        elif v in d:
            d[v] += 1

        if v//2 in d and v % 2 == 0:
            if v//2 not in counter:
                counter[v//2] = 0
            counter[v//2] += d[v//2]
    
    count = 0
    for v in counter.values():
        count += v
    
    return count