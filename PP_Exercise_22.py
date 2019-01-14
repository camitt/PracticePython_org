import re

# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!
#
# Extra:
#
# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.

def names():
    name_count = {}
    with open('PP_Exercise_22_names.txt', 'r') as file:
        fileContents = file.readlines()

        for line in fileContents:
            line = line.rstrip()
            if line in name_count:
                name_count[line] = name_count[line] + 1
            else:
                name_count[line] = 1
    print(name_count)

def categories():
    category_count = {}
    with open('PP_Exercise_22_categories.txt', 'r') as file:
        fileContents = file.readlines()

        for line in fileContents:
            splitValues = line.split('/')
            if splitValues[2] in category_count:
                category_count[splitValues[2]] = category_count[splitValues[2]] + 1
            else:
                category_count[splitValues[2]] = 1
    print(category_count)

def main():
    method = ""

    while True:
        method = input("Would you like to count names or categories? (c/n) ")
        if not re.match("^[cn]$", method):
            print("Invalid entry. Try again.")
            continue
        else:
            break

    if method == "c":
        categories()
    elif method == "n":
        names()
    else:
        print("You broke my code! Please document what you did and inform me so I can fix it. Thank you!")

main()
