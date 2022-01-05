// Implement an insertion sort algorithm

function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let j;
        let currentVal = arr[i];
        for (j = i - 1; j >= 0 && arr[j] > currentVal; j--) {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = currentVal
    }
    return arr;
}

console.log(insertionSort([4, 1, 2, 51, 24, 56, 32, 12, 4, 7, 100, 9, -1, -12, 21, 30, 34, -3, -21, 31, 34]));