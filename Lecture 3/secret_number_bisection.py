# MITx 6.00
# Lecture 3 - Discussion Question
# Jordan Hall

# Create a program that will guess a user-defined integer between 0 and 100 using bisection search.

# Tell the user to think of a number between 0 and 100.
print 'Please think of a number between 0 and 100!'

# Set the initial upper and lower bounds
upper_bound = 100
lower_bound = 0

response = ''

while response != 'c':

    # Supply a guess for the user's number
    guess = (upper_bound + lower_bound)/2
    print 'Is your secret number ' + str(guess) + '?'

    # Ask the user for feedback
    response = raw_input(r"Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    # Change the upper and lower bounds if the guess is incorrect.
    if response == 'h':
        upper_bound = guess
    elif response == 'l':
        lower_bound = guess
    elif response == 'c':
        print 'Game over. Your secret number was:', guess
    else:
        print 'I do not understand your input.'