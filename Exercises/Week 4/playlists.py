def count(t):
    index = {}
    counter = 0
    result = 0
    anchor = 0
    for i, v in enumerate(t):
        
        if v not in index:
            index[v] = i
            counter += 1 
            anchor = i
            
        else:   
            if index[v] >= anchor:
                anchor = index[v]
                index[v] = i
                
            counter = i - anchor
            
        result += counter
        
    return result