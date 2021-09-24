"""
Name: Lindy Mayes

File Name: mean.py

Problem: Calculate three kinds of mean for the given values.

Certification of Authenticity:
I certify that this assignment is entirely my own work


1. This program will calculate three different equations to find the mean of the user input given values
2. inputs - will be user input values, for this we will be testing values 10, 5, and 2.
   outputs- will be the RMS Average, the Harmonic mean, and the Geometric mean.
3.It must:ask for the user input for number of values
          next it must ask the user what the values are (as many times as they need for the number of values)
          finally it must compute the 3 seperate equations and output the answers

"""

import math

def main():
    rms = 0
    hm = 0
    gm = 1
    n = eval(input("Enter the values to be entered:"))
    for i in range(n):
        values = eval(input("enter value:" + str()))
        rms = rms + (values ** 2)
        hm = hm + (1 / values)
        gm = gm * values
    geometric_mean = gm ** (1 / n)
    harmonic_mean = n / hm
    rms = rms / n
    rms_average = math.sqrt(rms)
    print(round(rms_average, 3))
    print(harmonic_mean)
    print(round(geometric_mean, 3))

if __name__ == '__main__':
    main()







