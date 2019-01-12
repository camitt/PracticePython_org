# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.

def main():
    sentence = input("Please enter a sentence to reverse: ")
    splitSentence = sentence.split(" ")
    reverseSplitSentence = [splitSentence[x] for x in range(len(splitSentence) - 1, -1, -1)]
    newSentence = " ".join(reverseSplitSentence)
    return newSentence

def easier():
    sentence = input("Please enter a sentence to reverse: ")
    splitSentence = sentence.split(" ")
    return " ".join(reversed(splitSentence))

reversed = main()
print(reversed)
