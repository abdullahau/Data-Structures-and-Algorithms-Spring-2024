def count(a, b):
    b_map = {value: index for index, value in enumerate(b)}
    counter = 0
    for index, value in enumerate(a):
        if b_map[value] > index:
            counter += 1
    return counter 