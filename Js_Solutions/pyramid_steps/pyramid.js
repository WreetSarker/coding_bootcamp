// Write a function that accepts a positive number N.
// The function should console log a pyramid shape
// of N levels with the '#' symbol.Make sure the
// pyramid has space on both sides of the '#' symbol.

function pyramid(n, row = 0, level = '') {
    const mid = Math.floor((2 * n - 1) / 2);
    if (row === n) {
        return;
    }

    if ((2 * n - 1) === level.length) {
        console.log(level);
        pyramid(n, row + 1);
        return;
    }

    if (level.length < (mid - row) || level.length > (mid + row)) {
        level += ' ';
    } else {
        level += '#';
    }
    pyramid(n, row, level);
}



// Alternate solution
// function pyramid(n) {
//     const mid = Math.floor((2 * n - 1) / 2);
//     for (let row = 0; row < n; row++) {
//         let level = '';
//         for (let col = 0; col < 2 * n - 1; col++) {

//             if (col < (mid - row) || col > (mid + row)) {
//                 level += ' ';
//             } else {
//                 level += '#';
//             }
//         }
//         console.log(level);
//     }
// }

pyramid(20);