import re

# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
#
# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
#
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
#
# Remember that in Python 3, printing to the screen is accomplished by
#
#   print("Thing to show on screen")
# Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet, like this TutorialsPoint link.
def getInput():
    while True:
        size = input("What size of gameboard would you like drawn? Example: 3x3 \n")
        size = size.lower()
        if not re.match("\d*x\d*", size):
            print("Invalid entry. Try again.")
            continue
        else:
            return size.split("x")

def main():
    boardLength, boardHeight = getInput()
    makeBoard(boardLength, boardHeight)

def makeBoard(length, height):
    length = int(length)
    height = int(height)
    for y in range(height):
        for x in range(length):
            if x != length - 1:
                print(" ---", end = '')
            if x == length - 1:
                print(" ---")
        for x in range(length):
            print("|   ", end = '')
            if x == length - 1:
                print("|")
    for x in range(length):
        print(" ---", end = '')
main()
