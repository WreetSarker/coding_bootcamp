// Write a program that console logs the numbers from 1 to n.
// But for multiple of 3 print "fizz", for multiple of 5 print
// "buzz". The numbers which are multiple of both 3 and 3, for
// those print "fizzbuzz". 

function fizzbuzz(n) {
    for (let i = 1; i <= n; i++) {
        if (i % 3 === 0 && i % 5 != 0) {
            console.log("fizz")
        } else if (i % 5 === 0 && i % 3 != 0) {
            console.log("buzz")
        } else if (i % 3 === 0 && i % 5 === 0) {
            console.log("fizzbuzz")
        } else {
            console.log(i)
        }
    }
}

fizzbuzz(100)