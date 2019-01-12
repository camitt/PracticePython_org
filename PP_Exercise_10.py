import random

# Take two lists, say for example these two:
#
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this using at least one list comprehension.
# Extra:
#
# Randomly generate two lists to test this

# NOTE: Saving this example of my long strugglings for using try within a while loop.
def listCreation():
    random.seed()
    list1 = random.sample(range(100), random.randint(0,100))
    list2 = random.sample(range(100), random.randint(0,100))
    return list1, list2

def findOverlap(list1, list2):
    newList = [x for x in list1 for y in list2 if x == y]
    newList.sort()
    return newList

def removeDuplicates(newList):
    for value in range(len(newList) - 1):
        x = True
        while x == True:
            try:
                something = newList[value + 1]
            except IndexError:
                x = False
            else:
                if newList[value] == newList[value + 1]:
                    del newList[value + 1]
                else:
                    x = False
    return newList

def firstAttempt():
    list1, list2 = listCreation()
    newList = findOverlap(list1, list2)
    newList = removeDuplicates(newList)
    print(newList)

def main():
    random.seed()
    list1 = random.sample(range(100), random.randint(0,100))
    list2 = random.sample(range(100), random.randint(0,100))
    newList = [x for x in list1 if x in list2]
    print(sorted(newList))

main()
