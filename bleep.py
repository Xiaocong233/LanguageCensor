from cs50 import get_string
import sys

# Creating a set to later store banned words from the dictionary
BadWords = set()


def main():
    Input = sys.argv
    # Check if user inputted only two commandline arguments besides the interpreter
    if len(Input) == 2:
        dictionary = sys.argv[1]
        # Prompt the user for the message he/she wants to censor
        text = get_string("What message would you want to censor?\n")
        # Load the formatted words from the dictionary into the set
        load(dictionary)
        # Check if each word from the text user inputted is needed to be censored
        for word in text.split(' '):
            bleep(word)
            print(" ", end='')
        print()
        exit(0)

    else:
        # Give the user the correct instruction to run the program
        print("Usage: python bleep.py dictionary")
        exit(1)


# Loads up the dictionary from the command line argument containing words wanted to be censored (borrowed from speller, cs50 sandbox)
def load(Dictionary):
    file = open(Dictionary, "r")
    for line in file:
        BadWords.add(line.rstrip("\n"))
    file.close()


# Check if the word is contained within the dictionary; if it is, replace all characters in that word with asterisks, else leave the words alone
def bleep(word):
    if word.lower() in BadWords:
        for character in word:
            print('*', end="")
    else:
        print(word, end="")


# Call main
if __name__ == "__main__":
    main()
