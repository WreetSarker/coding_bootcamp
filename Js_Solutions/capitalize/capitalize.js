// Write a function that accepts a string. The function
// should capitalize first letter of each word of the
// sentence and then return the capitalized string.

function capitalize(str) {
    let sentence = '';
    for (i = 0; i < str.length; i++) {
        if (i === 0 || str[i - 1] === ' ') {
            sentence += str[i].toUpperCase();
        } else {
            sentence += str[i];
        }
    }
    return sentence;
}

// Alternate solution
// function capitalize(str) {
//     const words = [];
//     str.split(' ').forEach(element => {
//         words.push(element[0].toUpperCase() + element.slice(1));
//     });

//     return words.join(' ');
// }

console.log(capitalize('hi! i am not coming!!'))