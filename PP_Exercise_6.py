# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def isPalindrome(stringInput):
    # NOTE: This was my first solution but then came across the nicer solution that is implemented.
    # while stringInput:
    #     if stringInput[0] == stringInput[-1]:
    #         del stringInput[0]
    #         if stringInput:
    #             del stringInput[-1]
    #     else:
    #         return False
    # return True
    return stringInput[::] == stringInput[::-1]

def main():
    stringInput = list(input("Enter a word of your choice to check if it is a palindrome: "))

    if isPalindrome(stringInput):
        print("The given string is a palindrome")
    else:
        print("The given string is not a palindrome")

main()
