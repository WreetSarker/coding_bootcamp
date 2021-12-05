# Given a string, return a new string with
# reversed order of characters


def str_reverse(string):
    rev = ''
    for ch in range(len(string)):
        rev = string[ch] + rev

    return rev


print(str_reverse('12345'))

# Alternate solution 1
# def str_reverse(string):
#     rev = ''
#     for ch in range(len(string)-1, -1, -1):
#         rev += string[ch]

#     return rev
