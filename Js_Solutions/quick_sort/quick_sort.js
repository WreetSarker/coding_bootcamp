// Implement a quick sort algorithm

function quickSort(arr, left = 0, right = arr.length - 1) {
    if (left < right) {
        let pivotIdx = partition(arr, left, right);
        quickSort(arr, left, pivotIdx - 1);
        quickSort(arr, pivotIdx + 1, right);
    }
    return arr;
}

function partition(arr, start = 0, end = arr.length + 1) {
    let pivot = arr[0];
    let currentPivot = start;

    for (let i = start; i <= end; i++) {
        if (pivot > arr[i]) {
            currentPivot++;
            [arr[i], arr[currentPivot]] = [arr[currentPivot], arr[i]]
        }
    }
    [arr[currentPivot], arr[start]] = [arr[start], arr[currentPivot]]
    return currentPivot;
}





console.log(quickSort([1, 2, 51, 24, 56, 32, 12, 4,
    7, 100, 9, -1, -12, 21, 30, 34, -3, -21, 31, 34, -200, 300]));