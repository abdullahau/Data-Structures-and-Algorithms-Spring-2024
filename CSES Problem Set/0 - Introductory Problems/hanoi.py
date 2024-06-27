n = int(input())
r = [str((2**n)-1)]

d = {1: [_ for _ in range(n, 0, -1)], 2: [], 3: []}

ones = [2,0,3,0,1,0] if n % 2 == 0 else [3,0,2,0,1,0]

for i in range(int(r[0])):
    if i % 2 == 0:
        move, target = ones[(i-2)%6], ones[i % 6]
    else:
        if target == 3:
            na, nb = 1, 2
        elif target == 2:
            na, nb = 1, 3
        else:
            na, nb = 2, 3
        target = na if (d[na][-1:] > d[nb][-1:] and d[nb] != []) or d[na] == [] else nb
        move = na if target == nb else nb
    
    d[target].append(d[move].pop())
    r.append(f"{move} {target}")

print("\n".join(r))