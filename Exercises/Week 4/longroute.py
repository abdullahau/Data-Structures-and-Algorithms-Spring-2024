def count(s, k):
    directions = {'U': (0, 1), 'D': (0, -1), 'R': (1,0), 'L': (-1, 0)}
    position = {(0,0)}
    pos = (0, 0)
    r = max(len(s) // 2 + 1, 5)
    
    for _ in range(r):
        old = len(position)
        for c in s:
            pos = pos[0] + directions[c][0], pos[1] + directions[c][1]
            position.add(pos)
            
        new = len(position)
        
    return new + (new - old)*(k - r) 