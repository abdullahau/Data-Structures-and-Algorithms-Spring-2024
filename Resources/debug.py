def permutations(array: list) -> list:
    result = []
    
    def permute(array, path, result):
        if not array:
            result.append(path[:])
            return
        
        for i in range(len(array)):
            path.append(array[i])
            permute(array[:i] + array[i+1:], path, result)
            path.pop()
        return result
    
    return permute(array, [], result)


arr = [1, 2, 3]
print(permutations(arr))

arr = [0, 1]
print(permutations(arr))

arr = ["B1", "B2", "G1"]
print(permutations(arr))