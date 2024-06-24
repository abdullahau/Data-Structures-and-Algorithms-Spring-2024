from sys import stdin, stdout
input, print = stdin.readline, stdout.write

n = int(input())
 
for i in range(1,n+1):
    a = ((i**2)-1)*(i**2)//2
    b = (4*(i-1)**2) - 4*(i-1)
    print(str(a - b) + "\n")