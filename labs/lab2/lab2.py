"""
Name: <Lindy Mayes>
<Arithmetic>.py
"""

import math
def sum_of_threes():
    acc = 0
    a = eval(input("Enter the upper bound:"))
    for x in range(0, a, 3):
        acc = acc + x
    print(acc)

def multiplication_table():
    for h in range(1,11):
        for l in range(1,11):
            print (h * l, end = " ")
        print ()


def triangle_area():
    a = eval(input("Enter side a of triangle:"))
    b = eval(input("Enter side b of triangle:"))
    c = eval(input("Enter side c of triangle:"))
    s = (a + b + c)/2
    A = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(A)

def sumSquares():
    acc = 0
    l = eval(input("Enter the lower bound"))
    u = eval(input("Enter the upper bound"))
    for x in range(l, u + 1):
        acc = acc + x**2
    print (acc)


def power():
    base = eval(input("Enter the base"))
    exp = eval(input("Enter the exponent"))
    acc = 1
    for x in range(exp):
        acc = acc * base
    print(acc)

def main():
    sum_of_threes()
    multiplication_table()
    triangle_area()
    sumSquares()
    power()
main()
