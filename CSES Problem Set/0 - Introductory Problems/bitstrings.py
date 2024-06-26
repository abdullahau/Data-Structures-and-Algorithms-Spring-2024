from sys import stdin, stdout
input, print = stdin.readline, stdout.write
 
n = int(input())
print(str(2**n % (10**9 +7)))