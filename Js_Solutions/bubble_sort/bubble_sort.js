// Implement a bubble sort algorithm

function bubbleSort(arr) {
    for (let i = arr.length - 1; i >= 0; i--) {
        for (let j = 0; j < i; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}


// Optimized bubbleSort solution
// function bubbleSort(arr) {
//     let noSwap;
//     for (let i = arr.length - 1; i >= 0; i--) {
//         noSwap = true;
//         for (let j = 0; j < i; j++) {
//             if (arr[j] > arr[j + 1]) {
//                 const temp = arr[j];
//                 arr[j] = arr[j + 1];
//                 arr[j + 1] = temp;
//                 noSwap = false;
//             }
//         }
//         if (noSwap) break;
//     }
//     return arr;
// }

console.log(bubbleSort([4, 1, 2, 51, 24, 56, 32, 12, 4, 7, 100, 9, -1, -12, 21, 30, 34, -3]));