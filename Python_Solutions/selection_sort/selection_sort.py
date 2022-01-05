# Implement a selection sort algorithm

def selection_sort(arr):
    for i in range(len(arr) - 1):
        lowest = i
        for j in range(i+1, len(arr), 1):
            if arr[j] < arr[lowest]:
                lowest = j
        if i != lowest:
            temp = arr[i]
            arr[i] = arr[lowest]
            arr[lowest] = temp
    return arr


print(selection_sort([4, 1, 2, 51, 24, 56, 32, 12, 4,
      7, 100, 9, -1, -12, 21, 30, 34, -3, -21, 31, 34]))
