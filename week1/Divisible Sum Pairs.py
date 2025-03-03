# Divisible Sum Pairs

def divisibleSumPairs(n, k, ar):
    num = 0
    for i in range (len(ar)):
        for j in range (i, len(ar)):
            if i == j:
                continue
            elif (ar[i] + ar[j]) % k == 0:
                num += 1
    return num
