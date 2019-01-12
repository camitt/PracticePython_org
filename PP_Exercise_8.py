import re
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

def main():
    invalidInput = True
    input1 = ""
    input2 = ""
    print("Classic rock paper scissors! Each player chooses either rock(r), paper(p), or scissors(s).")
    while invalidInput:
        input1, input2 = getResponses()
        winner, invalidInput = checkWinner(input1, input2)
        if not invalidInput:
            if winner == input1:
                print("Congratulations Player 1 you won!!!")
            else:
                print("Congratulations Player 2 you won!!!")
            again = input("Would you like to play again (y/n)? ")
            again.lower()
            if again == "y":
                invalidInput = True
            else:
                print("Goodbye!")

def checkWinner(input1, input2):
    if input1 == input2:
        print("Draw! Try again!")
        return None, True
    elif input1 == "r" and input2 == "s" or input1 == "s" and input2 == "p" or input1 == "p" and input2 == "r":
        return input1, False
    else:
        return input2, False

def getResponses():
    while True:
        input1 = input("Player 1 what is your selection (r/p/s)? ")
        input1.lower()
        input1 = input1[0]
        if not re.match("[rps]", input1):
            print("Invalid selection")
        else:
            break
    while True:
        input2 = input("PLayer 2 what is your selection (r/p/s)? ")
        input2.lower()
        input2 = input2[0]
        if not re.match("[rps]", input2):
            print("Invalid selection")
        else:
            break
    return input1, input2

main()
