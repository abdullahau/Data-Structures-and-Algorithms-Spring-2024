def count(t):
    t = sorted(list(set(t)))
    counter = 1
    maximum = 1
    n = len(t)
    for i in range(1, n):
        if t[i-1] + 1 != t[i]:
            maximum = max(maximum, counter)
            counter = 0
        counter += 1
        if i == n-1:
            maximum = max(maximum, counter)
            
    return maximum