// Implement a selection sort algorithm

function selectionSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        let min = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[min]) {
                min = j;
            }
        }
        if (i !== min) {
            let temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
    return arr;
}

console.log(selectionSort([4, 1, 2, 51, 24, 56, 32, 12, 4, 7, 100, 9, -1, -12, 21, 30, 34, -3, -21, 31, 34]));