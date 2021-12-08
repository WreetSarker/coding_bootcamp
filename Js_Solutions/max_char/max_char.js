// Given a string, return a character
// that is most used in the string

function maxChar(str) {
    let charMap = {};
    let max = 0;
    let maxCh = '';

    for (let char of str) {
        if (charMap[char]) {
            charMap[char]++;
        } else {
            charMap[char] = 1;
        }
    }

    for (let char in charMap) {
        if (charMap[char] > max) {
            max = charMap[char];
            maxCh = char;
        }
    }

    return maxCh;
}
console.log(maxChar('Hello everyone'));
