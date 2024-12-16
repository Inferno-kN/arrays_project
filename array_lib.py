def sum_1d(arr):
    summa = 0
    for i in arr:
        summa += i
    return summa

def prod_1d(arr):
    multi = 1
    for i in arr:
        multi *= i
    return multi

def mean_1d(arr):
    average = sum_1d(arr) / arr(len(arr))
    return average

def max_1d(arr):
    max1 = arr[0]
    if max1 < arr[1]:
        max1 = arr[1]
    return max1

def min_1d(arr):
    min1 = arr[0]
    if min1 > arr[1]:
        min1 = arr[1]
    return min1

