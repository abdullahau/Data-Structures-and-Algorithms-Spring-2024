def count(t):
    index = {}
    result = 0
    anchor = 0
    for i, v in enumerate(t):
        if v in index and index[v] >= anchor:
            anchor = index[v] + 1

        index[v] = i
        
        result += i - anchor + 1
        
    return result