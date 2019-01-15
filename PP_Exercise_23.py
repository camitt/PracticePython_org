# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)
def main():
    primesList = []
    happyList = []
    overLappingList = []

    primesList = makeList("primes.txt")
    happyList = makeList("happy.txt")
    overLappingList = findOverlap(primesList, happyList)
    print(overLappingList)

def makeList(openFile):
    tempList = []
    with open(openFile, 'r') as file:
        fileContents = file.readlines()

        for line in fileContents:
            tempList.append(int(line))
    return tempList

def findOverlap(list1, list2):
    tempList = []
    for value in list1:
        if value in list2:
            tempList.append(value)
    return tempList

main()
