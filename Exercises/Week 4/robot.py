def count(s):
    directions = {'U': (0, 1), 'D': (0, -1), 'R': (1,0), 'L': (-1, 0)}
    position = {(0,0)}
    pos = (0, 0)
    
    for c in s:
        pos = pos[0] + directions[c][0], pos[1] + directions[c][1]
        position.add(pos)
    
    return len(position)