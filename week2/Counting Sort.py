# Counting Sort

def countingSort(arr):
    my_arr = [0] *100
    for i in arr:
        my_arr[i] += 1
    return my_arr
