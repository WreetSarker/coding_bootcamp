// Given an array and chunk size, divide the array into many subarrays
// where each subarray is of length size

function chunk(arr, size) {
    let chunked = [];

    for (let element of arr) {
        let last = chunked[chunked.length - 1];
        if (!last || last.length === size) {
            chunked.push([element]);
        } else {
            last.push(element);
        }
    }

    return chunked;
}

console.log(chunk([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))