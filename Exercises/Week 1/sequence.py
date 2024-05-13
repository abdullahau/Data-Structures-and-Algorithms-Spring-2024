def generate(n):
    if n // 10 == 0:
        return n
    else:
        n = (n - 9) * 10
        str_n = str(n)
        return int(str_n[:-1] + str_n[0])