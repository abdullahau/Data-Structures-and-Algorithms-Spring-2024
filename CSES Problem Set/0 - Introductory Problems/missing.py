n = int(input())
l = input()
l = set(map(int, l.split(" ")))

r = set(range(1,n+1))
for i in (r - l):
    print(i)