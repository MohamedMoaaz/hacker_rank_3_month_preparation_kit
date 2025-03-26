def pickingNumbers(a):
    a = sorted(a)
    subarr = [a[0]]
    longest_subarr = []
    for i in range(1, len(a)):
        if (a[i] - a[i-1] <= 1) and (a[i] - subarr[0] <=1):
            subarr.append(a[i])
            longest_subarr = longest_subarr if len(longest_subarr) > len(subarr) else subarr[:]
        else:
            subarr = [a[i]]

    return len(longest_subarr)
