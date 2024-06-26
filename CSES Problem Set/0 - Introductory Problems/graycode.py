n = int(input())

state = [1 for _ in range(n)]
byte = ["0" for _ in range(n)]
ref = [2**_ for _ in range(n-1,-1,-1)]

print("".join(byte))
for i in range(1,2**n):
    if i in ref:
        index = ref.index(i)
        byte[index] = str(int(byte[index]) + state[index])
        state[index] = -state[index]
        ref[index] += 2**(len(ref)-index)
        print("".join(byte))