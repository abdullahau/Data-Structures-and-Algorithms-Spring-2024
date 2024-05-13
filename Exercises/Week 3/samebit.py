def count(s):
    zeros = 0
    ones = 0
    for bit in s:
        if bit == '0':
            zeros += 1
        else:
            ones += 1
    zeros = (zeros - 1) * zeros // 2
    ones = (ones - 1) * ones // 2
    return zeros + ones 