def count(t):
    inversions = 0
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] > t[j]:
                inversions += 1
    return inversions