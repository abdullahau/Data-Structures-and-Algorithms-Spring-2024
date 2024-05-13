def count(s):
    zeros = s.count("0")
    length = len(s)
    if zeros < -(-length//2):
        return zeros
    else:
        return length - zeros