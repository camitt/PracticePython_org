import re
import random
import math

# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
#
# Extras:
#
# Use binary search.

def main():
    givenList = sorted(random.sample(range(100), k = random.randint(3,25)))
    checkNumber = int(getNumber())
    # withinList = easy(givenList, checkNumber)
    withinList = binarySearch(givenList, checkNumber)
    print("Your number is within the boundaries of the list: " + str(withinList))

def getNumber():
    while True:
        givenNumber = input("Enter a number: ")
        if not re.match("[\d]", givenNumber):
            print("Invalid entry. Try again.")
            continue
        else:
            return givenNumber

def easy(givenList, checkNumber):
    withinList = False
    if checkNumber in givenList:
        withinList = True
    return withinList

def binarySearch(searchList, searchNumber):
    workingList = searchList
    while len(workingList) >= 1:
        start = 0
        end = len(workingList)
        middle = math.floor((end - start) / 2)

        if searchNumber == workingList[middle]:
            return True
        elif searchNumber < workingList[middle]:
            workingList = workingList[0:middle]
        elif searchNumber > workingList[middle]:
            workingList = workingList[middle::]

main()
