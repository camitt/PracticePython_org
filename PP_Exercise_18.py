import random
import re

# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

def main():
    random4digit = str(random.randint(1000, 9999))
    totalGuess = 0
    cows = 0
    while cows != 4:
        guessDigit, totalGuess = getValidInput(totalGuess)
        cows, bulls = calcCowsBulls(random4digit, guessDigit)
        if cows == 4:
            print("Congratulation! You guessed correctly!")
            print("It only took you " + str(totalGuess) + " guesses!")
        else:
            print("Cows:Bulls      " + str(cows) + ":" + str(bulls))


def calcCowsBulls(winningDigits, guessDigit):
    guessDigitIndex = 0
    cows = 0
    bulls = 0

    for digit in guessDigit:
        if digit in winningDigits:
            if digit == winningDigits[guessDigitIndex]:
                cows += 1
            else:
                bulls += 1
        guessDigitIndex += 1
    return cows, bulls

def getValidInput(guessNumber):
    while True:
        guess = input("Enter a 4-digit number: ")
        if not re.match("^\d\d\d\d$", guess):
            print("Invalid entry. Try again.")
            continue
        else:
            guessNumber += 1
            return str(guess), guessNumber

main()
