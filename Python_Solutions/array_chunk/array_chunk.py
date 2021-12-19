# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size

def chunk(arr, size):
    chunked = []

    for element in arr:
        try:
            last = chunked[len(chunked) - 1]
        except:
            last = []
        if len(last) == 0 or len(last) == size:
            chunked.append([element])
        else:
            last.append(element)

    return chunked


print(chunk([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
