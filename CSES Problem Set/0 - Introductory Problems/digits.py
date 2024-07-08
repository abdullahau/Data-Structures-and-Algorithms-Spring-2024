q = int(input())

indices = []
m = 0
for _ in range(q):
    num = int(input())
    indices.append(num)
    m = max(num, m)

mins = {}
i = start = 0
while start < m:
    start = 10**(i)*(i+1)-(1/9)*10**(i+1)+(10/9)
    mins[i+1] = [int(start), 10**(i)]
    i += 1

for i in indices:
    for diff, j in mins.items():
        if i >= j[0]:
            anchor = j
            index = diff
        else:
            break
    num = (i-anchor[0])/index + anchor[1]
    prop = num - int(num)
    print(str(int(num))[int(round(prop * index))])