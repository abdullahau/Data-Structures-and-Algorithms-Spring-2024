def find(t):
    if len(t) < 2:
        return 0

    n = len(t)
    fb = sb = -t[0]
    fs = ss = 0
    rest = 0 

    for i in range(1, n):
        ss = max(ss, sb + t[i])
        sb = max(sb, rest - t[i])
        rest = fs 
        fs = max(fs, fb + t[i])
        fb = max(fb, -t[i])

    return max(fs, ss)