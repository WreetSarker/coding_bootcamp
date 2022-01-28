// Implement a karatsuba multiplication algorithm for large numbers

function karatsuba(num1, num2) {
    if (((num1 + '').length === 1) || ((num2 + '').length === 1)) {
        return num1 * num2;
    }

    let maxLen = Math.max((num1 + '').length, (num2 + '').length);
    let n = Math.floor(maxLen / 2);
    let a = Math.floor(num1 / (10 ** n));
    let b = num1 % (10 ** n);
    let c = Math.floor(num2 / (10 ** n));
    let d = num2 % (10 ** n);

    let z0 = karatsuba(a, c);
    let z1 = karatsuba(b, d);
    let z2 = karatsuba((a + b), (c + d));

    return (z0 * (10 ** (2 * n)) + z1 + (z2 - z1 - z0) * (10 ** n))
}

console.log(karatsuba(1031382847249249, 204289344328749244249824298492842984829842379423482412121212121212212121221212121212121212121212121212));
// console.log(1031382847249249 * 204289344328749244249824298492842984829842379423482412121212121212212121221212121212121212121212121212);