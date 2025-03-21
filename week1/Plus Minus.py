def plusMinus(arr):
    arrSize = len(arr)
    countPositive = sum(1 for x in arr if x > 0)
    countNegative = sum(1 for x in arr if x < 0)
    countZeros = arrSize - countPositive - countNegative
    
    print(f"{countPositive/arrSize:.6f}")
    print(f"{countNegative/arrSize:.6f}")
    print(f"{countZeros/arrSize:.6f}")

