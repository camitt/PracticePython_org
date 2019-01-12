import sys
import re
import math

# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
def getValidInput():
    while True:
        iNumber = input("Enter a number: ")
        if not re.match("\d", iNumber):
            print("Invalid entry. Try again.")
            continue
        else:
            iNumber = int(iNumber)
            break
    return iNumber

def isPrime(iNumber):
    isPrime = True
    if iNumber == 1:
        isPrime = False
        return isPrime

    elif iNumber == 2:
        isPrime = True
        return isPrime

    for x in range(2,math.ceil(iNumber / 2)):
        if iNumber % x == 0:
            isPrime = False
            break

    return isPrime

def main():
    iNumber = getValidInput()
    if isPrime(iNumber):
        print("The given number is a prime number.")
    else:
        print("The given number is not a prime number.")

main()
