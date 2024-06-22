from itertools import chain

n = int(input())
 
if n == 1: 
    print(1)
elif n > 3:
    i, z = (n, n - 1) if n % 2 == 0 else (n - 1, n)
    print(" ".join(map(str, chain(range(2, n + 1, 2), range(1, n + 1, 2)))))
else:
    print("NO SOLUTION")