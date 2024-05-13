def create(n):
    if n == 1:
        return [1]
    r = list(range(2, n+1, 2))
    odd = list(range(1, n+1,2))
    last = r[-1] if n % 2 == 0 else None
    while True:
        if len(r) == n:
            break
        
        if last == r[-1]:
            r = r + odd[1::2]
            last = r[-1]
            if odd[-1] != last:
                last = None
            odd = odd[0::2]
            
            if len(odd) < 2:
                r.append(odd[0])
        else:
            r = r + odd[0::2]
            last = r[-1]
            if odd[-1] != last:
                last = None
            odd = odd[1::2]
    
    return r