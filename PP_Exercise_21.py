import requests
from bs4 import BeautifulSoup
# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.
#
# Extras:
#
# Ask the user to specify the name of the output file that will be saved.

def main():
    url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    filename = input("What would you like to name this file? ")
    page = requests.get(url)
    pageHTML = page.text
    soup = BeautifulSoup(pageHTML, "lxml")
    pTags = soup.find('div',class_="article-main").find_all("p")
    for p_tag in pTags:
        with open(filename + ".txt", 'a+') as file:
            file.write(str(p_tag.text) + " ")
    print("Results have been saved in the " + filename + ".text file stored in the directory you issued this script from.")
main()
