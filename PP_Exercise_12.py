import random

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

def main():
    list1 = random.sample(range(100), random.randint(0,100))
    FLList = [list1[0], list1[-1]]

    print(list1)
    print(FLList)

main()
