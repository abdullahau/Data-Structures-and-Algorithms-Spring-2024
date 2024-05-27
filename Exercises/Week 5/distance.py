def find(t, k):
    t = sorted(t)
    largest = t[0] - 1

    n = len(t)
    for i in range(1,n):
        largest = max(largest, (t[i] - t[i-1]) // 2)
    
    largest = max(largest, k - t[-1])
    return largest