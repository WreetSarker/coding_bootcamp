// Check to see if two provided strings are anagrams of each other.
// One string is anagram of the other string if they use same characters
// in sane quantity. Only consider characters not spaces or
// punctuations. Consider capital letters to be same as lower case.

function anagrams(stringA, stringB) {
    const cleanA = cleanStr(stringA);
    const cleanB = cleanStr(stringB);

    if (cleanA.length != cleanB.length) return false;

    let charMapA = makeCharMap(cleanA);
    let charMapB = makeCharMap(cleanB);

    for (let key in charMapA) {
        if (charMapA[key] !== charMapB[key]) return false;
    }

    return true;
}

function makeCharMap(str) {
    let charMap = {};
    for (let char of str) {
        charMap[char] ? charMap[char] += 1 : charMap[char] = 1;
    }
    return charMap;
}

function cleanStr(str) {
    return str.replace(/[^\w]/g, '').toLowerCase();
}
console.log(anagrams('care!!!!!!!!!!!!!!!!!,...1  aa', 'raceaa!!!!1'))