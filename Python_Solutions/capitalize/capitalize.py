# Write a function that accepts a string. The function should
# capitalize first letter of each word of the sentence and
# then return the capitalized string.

def capitalize(string):
    sentence = ''
    for i in range(len(string)):
        if i == 0 or string[i-1] == ' ':
            sentence += string[i].upper()
        else:
            sentence += string[i]
    return sentence

# Alternate solution
# def capitalize(string):
#     words = []
#     for word in string.split(' '):
#         words.append(word[0].upper() + word[1:])
#     return (' ').join(words)


print(capitalize('look, it is working!'))
