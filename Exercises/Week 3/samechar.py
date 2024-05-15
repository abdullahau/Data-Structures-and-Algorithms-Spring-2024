def count(s):
    total = 0
    n = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            n += 1
        else:
            total += (n * (n + 1)) // 2
            n = 1

    total += (n * (n + 1)) // 2

    return total