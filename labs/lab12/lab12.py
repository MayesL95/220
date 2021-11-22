"""
Name: Lindy Mayes
looplists.py
"""

from random import randint
def find_and_remove_first(list, value):
    try:
        i = list: index(value)
        list[i] = "Lindy Mayes"
    except:
        pass

def read_data(filename):
    f = open(filename, "r")
    data = f.read()
    data = data.split()
    return data
def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if i == search_val:
            return True
        else:
            return False

def good_input():
    x = eval(input("Enter a number between 1 and 10"))
    while 10 < x < 1:
        x = eval(input("Enter a number between 1 and 10"))
    return x

def num_digits():
    num = eval(input("enter your number of 1 or greater"))
    while num > 1:
        digits = 0
        while num != 0:
            num //= 10
            digits += 1
        print("Your amount of digits is", digits)
        num = eval(input("enter your number of 1 or greater"))

def hi_lo_game():
    secret = randint(1, 100)
    guess = 1
    num = eval(input("guess a number"))
    while num != secret and guess < 7:
        guess += 1
        if num > secret:
            print("Your guess is to high")
        else:
            print("your guess is to low")
        num = eval(input("guess a number"))
    if num == secret:
        print("you got the correct number!")
    else:
        print("sorry the correct number was", secret)








def main():
    find_and_remove_first(list, "nothing")
    read_data(data_search.txt)
    is_in_linear(2, values)
    good_input()
    num_digits()
    hi_lo_game()
    pass


main()
