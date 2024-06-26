n = int(input())
s = n*(n+1)//2

if s % 2 == 0:
    print("YES")
    ss = s//2
    balance = ss - (1 + n)
    d = 1-(4*(-balance*2 - 2))
    i = (-1+(d**(1/2)))/(2)
    s1 = set(range(1,int(i)))
    s1.add(n)
    s1.add(ss - sum(s1))
    print(len(s1))
    print(*s1)
    s2 = set(range(1,n+1)) - s1
    print(len(s2))
    print(*s2)
else:
    print("NO")