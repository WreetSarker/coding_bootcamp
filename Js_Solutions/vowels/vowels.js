// Write a function that returns 
// the number of vowels in a String.

function vowelCount(str) {
    let count = 0;
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    for (let char of str.toLowerCase()) {
        if (vowels.includes(char)) count++;
    }
    return count;
}


// Alternate solution
// function vowelCount(str) {
//     let charMap = {};
//     const vowels = ['a', 'e', 'i', 'o', 'u'];
//     let count = 0;
//     for (char of str.toLowerCase()) {
//         charMap[char] ? charMap[char]++ : charMap[char] = 1;
//     }
//     for (let i = 0; i < vowels.length; i++) {
//         if (charMap[vowels[i]]) {
//             count += charMap[vowels[i]]
//         }
//     }
//     return count;
// }

console.log(vowelCount('HI there!'));