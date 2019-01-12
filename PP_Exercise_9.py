import random
import sys
import re

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
def main():
    winningNumber = random.randint(1,9)
    guesses = 0
    print("A number has been chosen at random between 1 and 9. Your goal is to guess which number has been selected. To exit the game at any time type \"exit\".")
    while True:
        guess = input("Please enter your guess: ")
        if not re.match("^[\d]$|^exit$", guess):
            print("Invalid entry. Try again.")
            continue
        elif re.match("^[\d]$", guess):
            guess = int(guess)
            guesses += 1
            if guess > winningNumber:
                print("Your guess is too high.")
            elif guess < winningNumber:
                print("Your guess is too low.")
            else:
                print("Congratulations! You guessed correctly with " + str(guesses) + " guesses! Let's do it again!")
                winningNumber = random.randint(1,9)
                guesses = 0
        else:
            print("Thanks for playing!")
            sys.exit()
main()
