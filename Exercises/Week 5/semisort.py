def solve(t):
    n = len(t)
    first = set(range(1, n//2+1))
    first_index = []
    for i, num in enumerate(t):
        if num in first:
            first_index.append(i)
    total = 0
    for i in range(n//2):
        total += first_index[i] - i
        
    return total