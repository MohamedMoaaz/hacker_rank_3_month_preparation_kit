def miniMaxSum(arr):
    arr.sort()
    miniSum = sum(arr[:4])
    maxSum = sum(arr[1:5])
    print(f"{miniSum} {maxSum}")
