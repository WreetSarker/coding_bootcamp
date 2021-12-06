# Given a string, return true
# if the string is a palindrome

def palindrome(string):
    i = 0
    while(i <= len(string)-(i+1)):
        if(string[i] != string[len(string) - (i+1)]):
            return False

        i = i + 1
    return True


print(palindrome('baab'))

# Alternate solution 1
# def palindrome(string):
#     rev = ''

#     for i in range(len(string)-1, -1, -1):
#         rev = rev + string[i]

#     return rev == string
