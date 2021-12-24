# Write a function that returns
# the number of vowels in a String.

def vowel_count(string):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string.lower():
        if char in vowels:
            count += 1
    return count


# Alternate solution
# def vowel_count(string):
#     count = 0
#     charMap = {}
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for char in string.lower():
#         if char not in charMap:
#             charMap[char] = 1
#         else:
#             charMap[char] += 1
#     for vowel in vowels:
#         try:
#             count += charMap[vowel]
#         except:
#             pass
#     return count


print(vowel_count('Why do YOU Ask?'))
