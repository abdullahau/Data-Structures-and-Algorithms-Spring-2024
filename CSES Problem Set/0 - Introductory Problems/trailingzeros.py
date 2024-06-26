from math import log

n = int(input())

a = n // 5

l = log(n, 5)
b = 0
for i in range(2,int(l)+1):
    b += (n//(5**i))

print(a+b)