# This is a guess the number game
import random

# Variable Declarations
minNum = 1
maxNum = 20
secretNumber = random.randint(minNum, maxNum)
maxGuess = 5

# Main
print('I am thinking of a number between ' + str(minNum) + ' and ' + str(maxNum) + '.')

# Ask for the player to guess.
for guessTaken in range(maxGuess, 0, -1):       # Count down
    print('Take a guess.  You have ' + str(guessTaken) + ' guesses left.')
    guess = int(input())

    if guess < secretNumber:
        print('You guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break       # Guess is correct.

if guess == secretNumber:
    print('Good Job! you guessed my number in ' + str(maxGuess - guessTaken + 1) + ' guesses!')
else: 
    print('Nope.  The Number I was thinking of was ' + str(secretNumber))