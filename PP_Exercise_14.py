import random

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def main():
    random.seed()
    list1 = random.choices(range(100), k = random.randint(0,100))
    noDupList = removeDuplicates(list1)
    noDupList2 = returnListNoDup(list1)
    print(noDupList)
    print(noDupList2)

def removeDuplicates(list):
    return set(list)

def returnListNoDup(list):
    newList = []
    for x in list:
        if x not in newList:
            newList.append(x)
    newList.sort()
    return newList

main()
