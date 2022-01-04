# Implement a bubble sort algorithm

def bubbleSort(arr):
    for i in range(len(arr)-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

# Bubble sort optimized solution
# def bubbleSort(arr):
#     noSwap = None
#     for i in range(len(arr)-1, -1, -1):
#         for j in range(0, i, 1):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#                 noSwap = False
#         if noSwap == True:
#             break
#     return arr


print(bubbleSort([4, 1, 2, 51, 24, 56, 32, 12,
      4, 7, 100, 9, -1, -12, 21, 30, 34, -3]))
