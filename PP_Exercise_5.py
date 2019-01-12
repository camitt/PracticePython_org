################ IMPORTS #####################################
import random

# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

def main():
    ################# VARIABLE DECLARATION #####################
    list1 = []
    list2 = []
    newList = []
    random.seed()
    listLength1 = random.randint(0,100)
    listLength2 = random.randint(0,100)

    ################ PROCESSING LOGIC ##########################
    for value in range(listLength1):
        list1.append(random.randint(0,100))

    for value in range(listLength2):
        list2.append(random.randint(0,100))

    for value in list1:
        if value in list2:
            if value not in newList:
                newList.append(value)

    print(sorted(newList))

main()
