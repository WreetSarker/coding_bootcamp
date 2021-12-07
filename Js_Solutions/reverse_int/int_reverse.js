// Given an integer, return a new integer
// that is in reverse order of numbers

function reverseInt(n) {
    reversed = n.toString().split('').reverse().join('');

    return Math.sign(n) * parseInt(reversed);
}

console.log(reverseInt(-100));