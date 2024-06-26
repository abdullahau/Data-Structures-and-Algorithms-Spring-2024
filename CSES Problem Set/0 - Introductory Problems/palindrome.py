def main():
    n = input()
    d = {}

    for i in n:
        d[ord(i)-65] = d.get(ord(i)-65, 0) + 1

    r = []
    if len(n) % 2 == 0:
        for l,v in d.items():
            if v % 2 != 0:
                return "NO SOLUTION"
            else:
                r.append(chr(l+65)*(v//2))
        return "".join(r+r[::-1])
    else:
        odd = 0
        for l,v in d.items():
            if v % 2 != 0:
                odd += 1
                index = l
            else:
                r.append(chr(l+65)*(v//2))
        if odd > 1:
            return "NO SOLUTION"
        return "".join(r+[chr(index+65)]*d[index]+r[::-1])

print(main())