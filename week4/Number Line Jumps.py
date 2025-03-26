def kangaroo(x1, v1, x2, v2):
    if v1 - v2 == 0:
        return 'NO'
    count = (x1 - x2) / (v2 - v1)
    print(count)
    return 'YES' if count % 1 == 0 and count >= 0 else 'NO'
