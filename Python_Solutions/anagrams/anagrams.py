# Check to see if two provided strings are anagrams of each other.
# One string is anagram of the other string if they use same characters
# in sane quantity. Only consider characters not spaces or
# punctuations. Consider capital letters to be same as lower case.

import re


def make_char_map(string):
    d = {}
    for char in string:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


def clean_str(string):
    return re.sub("[\W]", "", string).lower()


def anagrams(stringA, stringB):
    cleanA = clean_str(stringA)
    cleanB = clean_str(stringB)

    if len(cleanA) != len(cleanB):
        return False

    char_map_a = make_char_map(cleanA)
    char_map_b = make_char_map(cleanB)

    for key in char_map_a:
        try:
            char_map_a[key] != char_map_b[key]
        except:
            return False
    return True


print(anagrams('care!!!!!!!!!!!!!!!!!,...1  aa', 'raceaa!!!!1'))
