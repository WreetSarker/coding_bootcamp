# Implement a linear searching algorithm

def linear_search(arr, val):
    last = arr[-1]
    arr[-1] = val
    i = 0

    while arr[i] != val:
        i += 1

    arr[-1] = last

    if i < len(arr) - 1 or arr[-1] == val:
        return i
    return None


print(linear_search([1, 2, 3, 4, 5, -1, 22, 33, 23, 15, 17], -1))
