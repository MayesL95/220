"""
Name: Lindy Mayes
Loops.py

"""

def average():
    acc = 0
    total_grades = eval(input("Input the number of grades you have received"))
    for x in range(total_grades):
        grades = eval(input("Enter the HW" + str(x + 1)))
        acc = acc + grades
    print(acc / total_grades)

def tip_jar():
    acc = 0
    for x in range(5):
        donations = eval(input("enter uour donation amount"+ str(x +1)))
        acc = acc +donations
    print("The total amount in the jar is", acc)

def newton():
    x = eval(input("enter the number for x"))
    refine = eval(input("enter the amount of times to refine"))
    approx = x / 2
    for i in range(refine):
        approx = (approx + (x / approx)) / 2
    print(approx)

def sequence():
    terms = eval(input("Enter the amount of terms in series"))
    for x in range(1, terms +1):
        print(1 + (x // 2) * 2)

def pi():
    n = eval(input("Enter the number of terms in series"))
    acc = 1
    for x in range(n):
        num = 2 + ((x // 2) * 2)
        den = 1 + (((x + 1) // 2) *2)
        frac = num / den
        acc = acc * frac
    print(acc)










