# Implement a karatsuba multiplication algorithm for large numbers

def karatsuba(num1, num2):
    if len(str(num1)) == 1 or len(str(num2)) == 1:
        return num1*num2

    max_len = max(len(str(num1)), len(str(num2)))
    n = max_len // 2
    a = num1 // (10**n)
    b = num1 % (10**n)
    c = num2 // (10**n)
    d = num2 % (10**n)

    z0 = karatsuba(a, c)
    z1 = karatsuba(b, d)
    z2 = karatsuba((a+b), (c+d))

    return (z0*(10**(2*n)) + z1 + (z2-z1-z0) * (10**n))


print(karatsuba(10, 21))
print(karatsuba(1031382847249249,
                204289344328749244249824298492842984829842379423482412121212121212212121221212121212121212121212121212))
