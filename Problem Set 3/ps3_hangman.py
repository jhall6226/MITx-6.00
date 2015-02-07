# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/jmh0030/Documents/Github-Repositories/MITx-6.00/Problem Set 3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    result = True
    for c in secretWord:
        if c not in lettersGuessed:
            result = False
    return result


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for c in secretWord:
        if c in lettersGuessed:
            result += c
        else:
            result += '_'
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcedfghijklmnopqrstuvwxyz'
    
    result = ''
    for c in alphabet:
        if c not in lettersGuessed:
            result += c
    return result
    

def hangman(secretWord):
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
    print "Welcome to Hangman! The interactive word guessing game! I'm thinking of a word with", str(len(secretWord)), "letters!\n"
    
    guesses_made = 0
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters_guessed = []
    guessed_word = "_"*len(secretWord)

    while guesses_made < 8:
        guess = raw_input('Please guess a lowercase letter: ')
        if guess not in alphabet:
            print "Sorry, I didn't understand the value you entered. Please guess again.\n"
        elif guess in letters_guessed:
            print "You've already guessed that letter. Please guess again."
        else:
            guesses_made += 1
            letters_guessed.append(guess)
            
            if isWordGuessed(secretWord,letters_guessed):
                print 'You win! The word was ' + secretWord + '. It took you ' + str(guesses_made) + ' guesses.'
                exit
            else:
                guessed_word = getGuessedWord(secretWord,letters_guessed)
                    
                print guessed_word
                
                available_letters = getAvailableLetters(letters_guessed)
                
                print 'These letters remain to be guessed:', available_letters
                
    print '\nYou have run out of guesses. Try again next time.'
            
        




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
