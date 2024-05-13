def count(t):
    flattened = []
    
    def flatten(l):
        for j in l:
            if type(j) == list:
                flatten(j)
            else:
                flattened.append(j)        
        
    for i in t:
        if type(i) == list:
            flatten(i)
        else:
            flattened.append(i)
    
    return len(flattened)