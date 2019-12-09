import string
alph = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    result = []
    for i in alph:
        if i not in lettersGuessed:
            result.append(i)
    return ''.join(result)

print(getAvailableLetters(['a', 'b']))

