def count(t):
    n = len(t)
    prefix_sum = 0
    prefix_sum_map = {0: [-1]}
    counter = 0

    for i in range(n):
        prefix_sum += t[i]
        
        if prefix_sum in prefix_sum_map:
            for j in prefix_sum_map[prefix_sum]:
                if t[j + 1] == t[i]:
                    counter += 1
            prefix_sum_map[prefix_sum].append(i)
        else:
            prefix_sum_map[prefix_sum] = [i]

    return counter