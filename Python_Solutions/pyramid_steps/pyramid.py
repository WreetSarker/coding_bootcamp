# Write a function that accepts a positive number N.
# The function should console log a pyramid shape
# of N levels with the '#' symbol. Make sure the
# pyramid has space on both sides of the '#' symbol.

def pyramid(n, row=0, level=''):
    mid = (2*n-1)//2
    if n == row:
        return
    if len(level) == (2*n-1):
        print(level)
        pyramid(n, row+1)
        return
    if len(level) < (mid-row) or len(level) > (mid+row):
        level += ' '
    else:
        level += '#'
    pyramid(n, row, level)

# Alternate solution
# def pyramid(n):
#     mid = (2*n-1)//2
#     for row in range(n):
#         level = ''
#         for col in range(2*n - 1):
#             if col < (mid-row) or col > (mid+row):
#                 level += ' '
#             else:
#                 level += '#'
#         print(level)


pyramid(3)
