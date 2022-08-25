### Implement a simple binary search with tests


def binary_search(arr, n, k):
    """
    Binary search with array, length of array and search_element params
    """
    med = n // 2
    if n == 1 and arr[med] != k:
        return -1
    if arr[med] < k:
        ret = binary_search(arr[med + 1 : n], n - (med + 1), k)
        if ret > -1:
            return med + 1 + ret
        else:
            return ret
    elif arr[med] > k:
        return binary_search(arr[0:med], med, k)
    else:
        return med


def binary_search2(arr, low, high, x):
    pass
