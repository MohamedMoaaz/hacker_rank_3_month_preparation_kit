def diagonalDifference(arr):
    n1=0
    n2=0
    for idx in range(len(arr)):
        n1 += arr[idx][idx]
        n2 += arr[idx][len(arr) - 1 - idx]
    return abs(n2 - n1)
