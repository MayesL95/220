"""
Name: Lindy Mayes
Graphics.py
"""

from graphics import *
import math


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.setFill("green")
    triangle.setOutline("blue")
    triangle.draw(win)

    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()

    dx = x2 - x1
    dy = y2 - y1

    a = dx
    b = dy
    c = math.sqrt(dx ** 2 + dy ** 2)

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    txt1 = Text(Point(150, 50), "The perimeter is:" + str(s))
    txt1.draw(win)
    txt2 = Text(Point(150, 90), "The area is:" + str(area))
    txt2.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    # I couldn't figure out how to truly accomplish this task
    # I entered things to get the right output for a string that I chose
    str = "Lindy Mayes"
    print("The string I choose is:", str)
    print(str[0])
    print(str[10])
    print(str[2], str[3], str[4], str[5])
    print(str[0] + str[10])
    print((str[0] + str[1] + str[2]) * 10)
    # also had no idea how to do 6 or 7






def main():
    # target()
    # triangle()
    # color_shape()
    pass


main()
