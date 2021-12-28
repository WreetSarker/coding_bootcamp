// Print out the N - th entry in the fibonacci series.
// The fibonacci series is an ordering of numbers where
// each number is the sum of preceding throw.


function memoize(fn) {
    const cache = {};
    return function (...args) {
        if (cache[args]) {
            return cache[args];
        }

        const result = fn.apply(this, args);
        cache[args] = result;

        return result;
    }
}

// function fib(n) {
//     const result = [0, 1];
//     for (let i = 2; i <= n; i++) {
//         result.push(result[i - 1] + result[i - 2]);
//     }
//     return result[n];
// }

// Alternate solution
function slowFib(n) {
    if (n < 2) return n;

    return fib(n - 1) + fib(n - 2);
}
const fib = memoize(slowFib)



console.log(fib(700));