# Given an integer, return a new integer
# with its numbers in reverse order

def reverseInt(n):
    if n == 0:
        return n
    rev = ''
    for i in range(len(str(abs(n))) - 1, -1, -1):
        rev = rev + str(abs(n))[i]
    if n > 0:
        return int(rev)
    else:
        return -1 * int(rev)


print(reverseInt(-11192))
