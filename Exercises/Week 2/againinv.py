def create(n, k):
    l = list(range(1, n+1))
    
    num = l.pop()
    if k < n:
        l.insert(len(l)-k, num)
    else:
        l.insert(0, num)
        inversion = len(l) - 1
        i = 1
        while inversion < k:
            num = l.pop()
            if len(l) - i < (k - inversion):
                l.insert(i, num)
            else:
                l.insert(-(k - inversion), num)
            i += 1
            inversion += len(l) - i
            
    return l