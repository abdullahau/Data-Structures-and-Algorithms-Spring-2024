def find(s):
    length = len(s)
    for i in range(length):
        if s[:i+1] * (length // len(s[:i+1])) == s:
            return i + 1