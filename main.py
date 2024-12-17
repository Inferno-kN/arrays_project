from logger import log_action


def sum_arrays(arr1, arr2):
    log_action("arr1=", arr1, "arr2=",  arr2)
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result

def diff_arrays(arr1, arr2):
    log_action("arr1=", arr1, "arr2=",  arr2)
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] - arr2[i])
    return result

def prod_arrays(arr1, arr2):
    log_action("arr1=", arr1, "arr2=",  arr2)
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] * arr2[i])
    return result