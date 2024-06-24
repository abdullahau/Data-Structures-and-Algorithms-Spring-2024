from sys import stdin
input = stdin.readline

total = int(input())

for _ in range(total):
    y, x = map(int, input().split())
    n = max(y,x)
    mid = (n-1)**2 + (n-1) + 1
    delta = min(y,x)

    if y == x:
        print(mid)
    elif (n % 2 == 0 and y == n) or (n % 2 != 0 and x == n):
        print(mid+(n-delta))
    else:
        print(mid-(n-delta))