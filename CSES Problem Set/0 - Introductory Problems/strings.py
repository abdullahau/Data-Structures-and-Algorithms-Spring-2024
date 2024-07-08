def permutations(array: list) -> list:
    result = []
    
    def permute(array, path, result):
        if not array:
            if "".join(path[:]) not in result:
                result.append("".join(path[:]))
            return
        
        for i in range(len(array)):
            path.append(array[i])
            permute(array[:i] + array[i+1:], path, result)
            path.pop()
        return result
    
    print(len(permute(array, [], result)))
    return "\n".join(permute(array, [], result))


n = input()
print(permutations(n))