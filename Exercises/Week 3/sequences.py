def count(s):
    last = {'t': -1, 'i': -1, 'r': -1, 'a': -1}
    result = 0
    n = len(s)
        
    for i in range(n):
        if s[i] in last:
            last[s[i]] = i
        
        minimum = min(last.values())
        
        if minimum != -1:
            result += minimum + 1
    
    return result