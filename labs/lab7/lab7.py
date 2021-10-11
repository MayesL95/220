"""
Name: Lindy Mayes
Partner: <your partner's name goes here – first and last>
functions & spy craft.py
"""

import math

def cash_conversion():
    number = eval(input("Enter an integer"))
    print("$" + '{:.2f}'.format(number))

def encode():
    x = input("Enter a message")
    key = eval(input("Enter a number value"))
    acc = " "
    for c in x:
        i = ord(c)
        new_chc = chr(key + i)
        acc = acc + new_chc
    print(acc)

def sphere_area(radius):
    area = 4 * math.pi * radius ** 2
    return area

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume

def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc

def sum_n_cubes(n):
    acc = 1
    for i in range(n):
        acc = acc + i**3
    return acc

def read_write_file_test():
    in_file_name = "input.txt"
    in_file = open(in_file_name, "r")

    out_file_name = "output.txt"
    out_file = open(out_file_name, "w")

    for line in in_file:
        print(line.rstrip('\n'), file=out_file)

    out_file.close()

def encode_better():
    m = input("Enter message")
    k = input("Enter key")
    acc = " "
    for i in range(len[m]):
        c = ord(m[i])
        key = ord(k[i])
        new_chrc = c + key - 97
        acc = acc + chr(new_chrc)
    print(acc)





def main():
    cash_conversion()
    encode()
    print(sphere_area(2))
    print(sphere_volume(5))
    print(sum_n(4))
    print(sum_n_cubes(3))
    read_write_file_test()
    encode_better()


main()
