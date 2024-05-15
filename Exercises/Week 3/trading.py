def find(t):
    lowest = lowest_prev = [t[0], -1]
    best = [0, -1]
    n = len(t)
    for i, price in enumerate(t):
        if price < lowest[0]:
            lowest = [price, i]
        profit = price - lowest[0]
        if profit > best[0]:
            lowest_prev = lowest
            best = [profit, i]
            
    j = best[1] + 2
    best_left = 0
    if n - j > 1 and best[0] > 0:
        lowest = t[j]
        for i in range(j, n):
            lowest = min(lowest, t[i])
            best_left = max(best_left, t[i] - lowest)
    
    k = lowest_prev[1] - 1
    best_right = 0
    if k > 1 and best[0] > 0:
        lowest = t[0]
        for i in range(k):
            lowest = min(lowest, t[i])
            best_right = max(best_right, t[i] - lowest)
        
    return best[0] + max(best_left, best_right)