def find(a, d):
    events = []
    
    for time in a:
        events.append((time, 1))
    for time in d:
        events.append((time, 2))
    
    events.sort()
    
    max_vacancy = 0
    present = 0
    
    n = len(events)
    for i in range(n):
        if present == 0 and i != 0:
            vacancy = events[i][0] - events[i-1][0]
            max_vacancy = max(max_vacancy, vacancy)
            
        if events[i][1] == 1:
            present += 1
        elif events[i][1] == 2:
            present -= 1
    
    return max_vacancy