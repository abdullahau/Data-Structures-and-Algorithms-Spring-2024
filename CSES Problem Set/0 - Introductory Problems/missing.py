n = int(input())
l = map(int,input().split(" "))
print(n*(n+1)//2-sum(l))