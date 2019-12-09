# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

alph = string.ascii_lowercase

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    length = len(secretWord)
    output = ['_'] * length
    for i in lettersGuessed:
        for index, element in enumerate(secretWord):
            if element == i:
                output[index] = i
    return ' '.join(output)


import string
alph = string.ascii_lowercase


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = []
    for i in alph:
        if i not in lettersGuessed:
            result.append(i)
    return ''.join(result)
    


def hangman():
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    wordlist = loadWords()
    secretWord = chooseWord(wordlist)

    length = len(secretWord)
    error_num = 0
    lettersGuessed = []

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', length, 'letters long.')

    while error_num <= 8:
        left_num = 8 - error_num
        guess = True
        while guess:
            print('You have', left_num, 'guesses left.')
            enter = input('Please guess a letter:')
            if enter.isalpha():
                guess = False
                if enter.islower():
                    letter = enter
                else:
                    letter = enter.lower()
            else:
                print('Error!! Please enter a letter')

        if letter in secretWord:
            lettersGuessed.append(letter)
            print('Good guess:', getAvailableLetters(lettersGuessed),'\n','----------')
            if isWordGuessed(secretWord, lettersGuessed):
                print('Congratulations, you won!')
        else:
            error_num += 1
            print('Oops! That letter is not in my word:', getAvailableLetters(lettersGuessed),'\n','----------')
    else:
        print('Sorry, you ran out of guesses. The word was else. ')






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

hangman()