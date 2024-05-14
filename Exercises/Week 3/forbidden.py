def count(s):
    a = -1
    result = 0
    n = len(s)
    
    for i in range(n):
        if s[i] == "a":
            a = i
            
        result += i - a
    
    return result