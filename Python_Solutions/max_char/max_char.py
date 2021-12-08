# Given a string, return a character
# that is most used in the string

def maxChar(string):
    charMap = dict()
    max_Occurrance = 0
    max_Ch = ''

    for ch in string:
        if ch not in charMap:
            charMap[ch] = 1
        else:
            charMap[ch] += 1

    for ch in charMap:
        if charMap[ch] > max_Occurrance:
            max_Occurrance = charMap[ch]
            max_Ch = ch

    return max_Ch


print(maxChar('Hello everyone'))
