// Implement a linear searching algorithm

function linearSearch(arr, val) {
    const last = arr[arr.length - 1];
    arr[arr.length - 1] = val;
    let i = 0;

    while (arr[i] != val) {
        i++;
    }

    arr[arr.length - 1] = last;
    if (i < arr.length - 1 || arr[arr.length - 1] === val) {
        return i;
    }
    return null;
}

console.log(linearSearch([1, 2, 3, 4, 5, -1, 22, 33, 23, 15, 17], 10));