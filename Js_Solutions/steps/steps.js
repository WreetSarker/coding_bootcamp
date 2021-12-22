// Write a function that accepts a positive number N.
// The function should console log a step shape
// with N levels using the character '#'. Make sure
// the step has space on the right hand side.

function steps(n, row = 0, stair = '') {
    if (n === row) {
        return;
    }

    if (n === stair.length) {
        console.log(stair);
        steps(n, row + 1);
        return;
    }

    if (stair.length <= row) {
        stair += '#';
    } else {
        stair += ' ';
    }

    steps(n, row, stair);
}


// Alternate solution 1
// function steps(n) {
//     for (let i = 0; i < n; i++) {
//         let stair = '';
//         for (let j = 0; j < n; j++) {
//             if (j <= i) {
//                 stair += '#';
//             } else {
//                 stair += ' ';
//             }
//         }
//         console.log(stair);
//     }
// }



// Alternate solution 2
// function steps(n) {
//     for (let i = 1; i <= n; i++) {
//         console.log('#'.repeat(i) + ' '.repeat(n - i));
//     }
// }

steps(20);