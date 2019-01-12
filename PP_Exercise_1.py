from datetime import date

# Exercise 1
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
#
# 1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button) 

def returnYear(age):
    intAge = int(age)
    birthYear = date.today().year - intAge
    birthdayOccurred = input("Has your birthday already occurred this year? (Y/N): ")
    if birthdayOccurred.lower() == "n":
        birthYear -= 1
    return birthYear + 100

def getInfo():
    name = input("What is your name? ")
    age = input("Please enter your current age: ")
    repeat = input("Enter a number: ")
    return name, age, repeat

def main():
    name, age, repeat = getInfo()
    centuryAge = returnYear(age)

    for i in range(int(repeat)):
        print(name + " you will turn 100 in the year " + str(centuryAge))

main()
