"""
Name: Lindy Mayes
conditionals.py
"""

from graphics import *
import math

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def writeSumOfSquares():
    infile = input("myfile.txt")
    outfile = input("answer.txt")
    readfile = open(infile, "r")
    writefile = open(outfile, "w+")
    for line in infile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        writefile.write("sum of Squares = " + str(summation))

def starter():
    weight = eval(input("enter your weight with the decimal ex.130.0"))
    numWins = eval(input("enter the number of wins you have"))
    if ((weight >= 150 and weight < 160) and numWins >= 5) or (weight > 199 and numWins > 20):
        print("you qualify as a starter")
    else:
        print("you do not qualify as a starter")

def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")




def circleoverlap():
    win = GraphWin("Circle Shift", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    r2 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r1)
    c1.draw(win)
    c2 = Circle(p2, r2)
    c2.draw(win)
    if p1 <= r1 + r2 and p2 <= r1 + r2:
        message = Text(Point(200, 100), "Circles Overlap")
        message.draw(win)
    else:
        message = Text(Point(200, 100), "circles do not overlap")
        message.draw(win)

    win.getMouse()
    win.close()





def main():
    addTen([5, 2, 3])
    squareEach([3, 5.7, 2])
    sumList([3, 5.7, 2])
    toNumbers(["3","5.7", "2"])
    writeSumOfSquares()
    starter()
    leapYear(2000)
    circleoverlap()
    pass


main()
