# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def isEven(number):
    if number % 4 == 0:
        return "4"
    elif number % 2 == 0:
        return True
    else:
        return False

def inputsDivisible(number, number2):
    if number % number2 == 0:
        return True
    else:
        return False

def returnStatement(state, number, number2):
    if state == True:
        print("The first number you gave is even")
    elif state == "4":
        print("The first number you gave is evenly divisible by 4")
    else:
        print("The first number you gave is odd")

    if inputsDivisible(number, number2):
        print("The second number evenly divides into the first number given.")
    else:
        print("The second number does not evenly divide into the first number given.")

def main():
    number = int(input("Enter a number: "))
    number2 = int(input("Enter a second number: "))
    state = isEven(number)
    returnStatement(state, number, number2)

main()
