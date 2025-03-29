def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    result = []
    
    for q, x, y in queries:
        idx = (x ^ lastAnswer) % n
        if q == 1:
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            result.append(lastAnswer)
    
    return result
