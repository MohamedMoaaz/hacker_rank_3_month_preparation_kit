#Page counter

def pageCount(n, p):
    return min(p//2, (n - (p//2) * 2) // 2)
