// Implement a binary search algorithm

function binarySearch(arr, val) {
    let low = 0;
    let hi = arr.length - 1;
    let mid;

    while (low <= hi) {
        mid = (low + hi) / 2;
        if (arr[mid] === val) {
            return mid;
        } else if (val < arr[mid]) {
            hi = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return null;
}

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7], 400));