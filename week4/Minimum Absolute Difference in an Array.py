def minimumAbsoluteDifference(arr):
    arr.sort()
    mini = sys.maxsize
    for i in range(len(arr)-1):
        a, b = arr[i], arr[i+1]
        mini = min(mini, abs(a - b))
    return mini
