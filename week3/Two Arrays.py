def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for i, j in zip(A, B):
        if i + j < k:
            return ("NO")
    return ("YES")
