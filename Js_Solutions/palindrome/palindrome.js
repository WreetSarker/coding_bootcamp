// Given a string, return true
// if the string is a palindrome


function palindrome(str) {
    let i = 0;
    while (i <= str.length - (i + 1)) {
        if (str[i] != str[str.length - (i + 1)]) {
            return false;
        }

        i++;
    }
    return true;
}


console.log(palindrome('baaab'))

// Alternate solution
// function palindrome(str) {
//     rev = '';

//     for (let i = str.length - 1; i >= 0; i--) {
//         rev = rev + str[i];
//     }

//     return str === rev;
// }