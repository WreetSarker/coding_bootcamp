# Implement an insertion sort algorithm

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        currentValue = arr[i]
        while j >= 0 and arr[j] > currentValue:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = currentValue
    return arr


print(insertion_sort([4, 1, 2, 51, 24, 56, 32, 12, 4,
      7, 100, 9, -1, -12, 21, 30, 34, -3, -21, 31, 34, -200, 300]))
