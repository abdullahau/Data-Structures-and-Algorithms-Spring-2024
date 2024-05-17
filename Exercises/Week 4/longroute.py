def count(s, k):
    visited = set()
    visited.add((0,0))
    y = x = 0
    n = max(len(s) // 2 + 1, 5)
    
    diffs = []
    
    for i in range(n):
        for c in s:
            if c == "U": y -= 1
            if c == "D": y += 1
            if c == "L": x -= 1
            if c == "R": x += 1
            visited.add((y,x))
        diffs.append(len(visited))
    
    increments = []

    for i in range(1, len(diffs)):
        increments.append(diffs[i]-diffs[i-1])
    
    return (diffs[n-1] - increments[-1]) + (increments[-1]) *(k-(n-1))