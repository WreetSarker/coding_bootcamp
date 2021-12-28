# Print out the N - th entry in the fibonacci series.
# The fibonacci series is an ordering of numbers where
# each number is the sum of preceding throw.


def fib(n):
    result = [0, 1]
    for i in range(2, n+1):
        result.append(result[i-1] + result[i-2])
    return result[n]

# Alternate solution
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)


print(fib(10))
