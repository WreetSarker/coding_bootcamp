// Implement a merge sort algorithm

function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    let mid = Math.trunc(arr.length / 2)
    let left = mergeSort(arr.slice(0, mid));
    let right = mergeSort(arr.slice(mid));
    return merge(left, right);
}

function merge(arr1, arr2) {
    const result = [];
    let i = 0;
    let j = 0;

    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] < arr2[j]) {
            result.push(arr1[i]);
            i++;
        } else {
            result.push(arr2[j]);
            j++
        }
    }
    while (i < arr1.length) {
        result.push(arr1[i]);
        i++;
    }

    while (j < arr2.length) {
        result.push(arr2[j]);
        j++;
    }
    return result;
}

// console.log(merge([1, 2, 3], [2, 2, 4, 5, 6]));
console.log(mergeSort([2, 5, 1, 7, 2, 87, 45, 89, 21, 34, 65, 21, 57, 38, 81, 1, 3, 4, 6, 2, 92, 31, 53, 424, 593, 420, 429847, 2432, 42310, 139344, 1, 2, 33, 35, 1211212212, 12, 1433534525, 1313, 131, 146, 96, 2, 35, 73, 12, 5353535, 7573, 1346, 24341, 75786, 13125, 53, 131, 53536, 4642, 13186, 5789, 869464]));
