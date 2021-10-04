"""
Name: Lindy Mayes
Strings as a sequence.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter your first than last name")
    name_list = name.split(" ")
    print(name_list[1] + ", " + name_list[0])

def company_name():
    website = input("Enter a three-part internet domain")
    website_list = website.split(".")
    print(website_list[1])

def initials():
    students = eval(input("Enter how many students"))
    for names in range(students):
        first = input("Enter the first name of student " + str(names +1) + ":")
        last = input("Enter " + first + "'s last name:")
        print(first + "'s initials are " +first[0] +last[0] + ".")

def names():
    names = input("Enter people's names, separated by commas: ")
    names_list = names.split(", ")
    for names in names_list:
        individuals = names.split(" ")
        print("The initials are ", end=" " + individuals[0][0] + individuals[1][0] + " ")

def thirds():
    n = eval(input("Enter how many sentences"))
    for words in range(n):
        sentence = input("Enter sentence " + str(words + 1))
        print(sentence[2::3])

def word_average():
    acc = 0
    sentence = input("Enter a sentence")
    words = sentence.split(" ")
    num_words = len(words)
    for word in words:
        acc = acc + len(word)
    total_letters = acc
    print(total_letters / num_words)


def pig_latin():
    sentence = input("Enter a sentence:")
    sentence = sentence.lower()
    sentence = sentence.split(" ")
    for word in sentence:
        x = word[1:]
        x = x + word[0] + "ay"
        print(x, end=" ")




def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()



main()
