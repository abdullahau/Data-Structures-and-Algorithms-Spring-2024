def solve(t, x):
    t = sorted(t)
    total = 0
    packed = 0

    for p in t:
        total += p
        if total <= x:
            packed += 1
        else:
            break

    return packed