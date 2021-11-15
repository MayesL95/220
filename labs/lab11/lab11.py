"""
Name: Lindy Mayes
hangman.py
"""
from random import randint

def words (infile):
    infile = open(infile, "r")
    content = infile.read()
    return content.split("\n")

def random_word(list):
    return list[randint(0, len(list))]

def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)

def won(word, letters):



def play():
    w = words("wordslist.txt")
    secret = random_word(w)
    incorrect = 0
    guesses = []
    current = "_" * len(secret)
    while not won(): and while incorrect < 7:
        display = fill(secret, guesses)
        print(display)
        print(guesses)
        letter = input('guess your letter')
        while guesses in w:
            letter = input('guess a letter')
            guesses.append(letter)
            display = fill(secret, guesses)
            if incorrect:
                incorrect += 1
            else:
                current = display

def main():
    play()

main()
