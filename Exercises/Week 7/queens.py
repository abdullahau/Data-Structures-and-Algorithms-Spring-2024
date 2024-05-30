from itertools import combinations
from math import comb

def count(n, k):
    possibility = comb(n**2, k)
    coords = [(row, col) for row in range(n) for col in range(n)]
    combs = combinations(coords, k)
    return possibility - check_combs(combs, k)

def check_combs(combs, k):
    failed = 0
    for i in combs:
        fail = 0
        for queen1 in range(len(i)-1):
            for queen2 in range(queen1+1, len(i)):
                fail += attack(i[queen1], i[queen2])
        if fail > 0:
            failed += 1
    return failed

def attack(queen1, queen2):
    if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
        return 1
    if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
        return 1
    return 0