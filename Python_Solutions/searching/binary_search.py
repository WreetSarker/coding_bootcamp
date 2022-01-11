# Implement a binary search algorithm

def binary_search(arr, val):
    low = 0
    hi = len(arr) - 1
    mid = (low + hi) // 2

    while low <= hi:
        mid = (low+hi) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            hi = mid-1
        else:
            low = mid + 1
    return None


print(binary_search([1, 2, 3, 5, 6, 7], 7))
