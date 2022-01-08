# Implement a quick sort algorithm

def quick_sort(arr, left, right):
    if left < right:
        pivotIdx = partition(arr, left, right)
        quick_sort(arr, left, pivotIdx - 1)
        quick_sort(arr, pivotIdx + 1, right)
    return arr


def partition(arr, start, end):
    pivot = arr[start]
    currentIdx = start

    for i in range(start, end+1):
        if arr[i] < pivot:
            currentIdx += 1
            temp = arr[i]
            arr[i] = arr[currentIdx]
            arr[currentIdx] = temp
    temp = arr[currentIdx]
    arr[currentIdx] = arr[start]
    arr[start] = temp
    return currentIdx


data = [1, 2, 51, 24, 56, 32, 12, 4,  7, 100, 9, -
        1, -12, 21, 30, 34, -3, -21, 31, 34, -200, 300, 13, -220, 14, -240, 400]
size = len(data)-1
print(quick_sort(data, 0, size))
