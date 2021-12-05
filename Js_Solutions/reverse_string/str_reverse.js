// Given a string, return a new string
// with its characters reversed

function str_reverse(str) {
    let rev = '';

    for (let i = str.length - 1; i >= 0; i--) {
        rev += str[i];
    }

    return rev;
}


console.log(str_reverse('123456'))

// Alternate solution 1
// function str_reverse(str) {
//     return str.split('').reverse().join('');
// }

// Alternate solution 2
// function str_reverse(str) {
//     let rev = '';

//     for (let character of str) {
//         rev = character + rev;
//     }

//     return rev;
// }
