# Write a function that accepts a positive number N.
# The function should print a step shape
# with N levels using the character '#'. Make sure
# the step has space on the right hand side.

def steps(n, row=0, stair=''):
    if n == row:
        return

    if n == len(stair):
        print(stair)
        steps(n, row + 1)
        return

    if len(stair) <= row:
        stair += '#'
    else:
        stair += ' '

    steps(n, row, stair)


# Alternate solution 1
# def steps(n):
#     for i in range(n):
#         stair = ''
#         for j in range(n):
#             if j <= i:
#                 stair += '#'
#             else:
#                 stair += ' '
#         print(stair)


# Alternate solution 2
# def steps(n):
#     for i in range(1, n+1):
#         print('#'*i + ' '*(n-i))


steps(10)
