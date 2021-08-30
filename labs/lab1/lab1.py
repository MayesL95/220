"""
Name: <Lindy Mayes>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    made = eval(input("Enter the made:"))
    taken = eval(input("Enter the taken:"))
    percentage = taken / made
    print("Percentage =", percentage)

def coffee():
    cost_per_pound = 10.50
    shipping_per_pound = .86
    cost_per_order = 1.50
    pounds_ordered = eval(input("Enter the pounds_ordered:"))
    total_cost = cost_per_pound * shipping_per_pound
    print("Total cost =", total_cost)


def kilometers_to_miles():
    kilometers = eval(input("Enter the kilometers"))
    conversion = 1.609
    miles = kilometers / conversion
    print("Miles =", miles)








