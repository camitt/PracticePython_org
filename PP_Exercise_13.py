import re

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def main():
    while True:
        n = input("What is the number of the Fibonnaci number you would like to retrieve the value for? ")
        if not re.match("[\d]", n):
            print("Invalid entry. Try again.")
            continue
        else:
            n = int(n)
            break

    value = fibonnaciValue(n)
    print(value)

def fibonnaciValue(n):
    x = 0
    y = 0
    for z in range(1, n + 1):
        if x == 0:
            x = 1
        elif y == 0:
            y = 1
        elif x <= y:
            x = y + x
        else:
            y = y + x
    if x > y:
        return x
    else:
        return y

main()
