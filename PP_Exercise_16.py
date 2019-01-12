import random
import string

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

def strongPassword():
    charChoices = []
    validOptions = list(string.ascii_letters + string.digits + string.punctuation)
    for value in validOptions:
        charChoices.append(value)
    password = random.choices(charChoices, k = random.randint(14, 100))
    return "Your new password is: " + "".join(password)

def main():
    passwordCreated = False
    password = ""
    while passwordCreated == False:
        strength = input("Would you like a strong or weak password? ")
        strength.lower()
        random.seed()
        if strength == "strong":
            password = strongPassword()
            passwordCreated = True
        elif strength == "weak":
            password = weakPassword()
            passwordCreated = True
        else:
            print("Invalid selection. Please select again.")
    return password

def weakPassword():
    words = open("C:\\13 - Code\\00 - Practice\\Python\\PracticePython_org\\rockyou.txt", encoding="utf8").read().split()
    return random.choice(words)

print(main())
