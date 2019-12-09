def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter in lettersGuessed:
            value = True
        else:
            value = False
            break
    return value

print(isWordGuessed('apple', ['e', 'l', 'k', 'p', 'r', 'a']))