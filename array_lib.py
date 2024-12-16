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


def sum_2d(matrix):
    summa1 = 0
    for i in matrix:
        summa1 += i
    return summa1

def prod_2d(matrix):
    multi = 1
    for i in matrix:
        multi *= i
    return multi

def mean_2d(matrix):
    average_2d = sum_2d(matrix) / len(matrix)
    return average_2d


