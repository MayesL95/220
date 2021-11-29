"""
Name: Lindy Mayes
ListsSearching.py
"""

def is_in_binary(search_val, values):
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = left + right // 2
        middle_value = values[middle]
        if search_val == middle_value:
            return middle
        if search_val < middle_value:
            right = middle - 1
        if search_val > middle_value:
            left = middle + 1
    return -1

def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        position = i
        for j in range(i + 1, len(values)):
            if j < i:
                lowest = values[j]
                position = j
        values[i], values[position] = values[position], values[i]

def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy

def rect_sort(rectangles):
    dict = {}
    areas = []
    for rectangle in rectangles:
        rectangle = dict[calc_area(rectangle)]
        areas.append(calc_area(rectangle))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = dict[i]

def star_find(filename):
    file = open(filename, "r")
    signals = file.read().split()
    found = []
    for i in range(len(signals)):
        low = 4000
        high = 5000
        if low <= int[i] <= high:
            found = found + i
            if found == 5:
                break
    print(found)
    if found != 5:
        print("five signals were not found")
    else:
        print(found)

def main():
    is_in_binary()
    selection_sort()
    rect_sort()
    star_find(signals.txt)
    pass


main()
