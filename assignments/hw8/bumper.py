"""
Name: Lindy Mayes

File Name: bumper.py

Problem: simulate bumper cars with circles

Certification of Authenticity:
I certify that this assignment is entirely my own work but a tutor tried to help
"""

from graphics import *
from random import randint
import time

def main():
    win = GraphWin("Bumper Cars Simulation", 500, 500)
    win.setCoords(0, 0, 10, 10)
    radius = .5
    dx, dy = 1, 1

    circle_one_point = Point(randint(0, 10), randint(0, 10))
    circle_one = Circle(circle_one_point, radius)
    circle_one.setOutline("blue")
    circle_one.setFill("blue")
    circle_one.draw(win)

    circle_two_point = Point(randint(0, 10), randint(0, 10))
    circle_two = Circle(circle_two_point, radius)
    circle_two.setOutline("red")
    circle_two.setFill("red")
    circle_two.draw(win)

    x_bottom = radius
    x_top = win.getWidth() - radius
    y_bottom = radius
    y_top = win.getHeight() - radius

    while True:
        time.sleep(.5)
        circle_one.move(dx, dy)
        circle_two.move(dx, dy)
        if circle_one.getCenter().getY() <= y_bottom or circle_one.getCenter().getY() >= y_top:
            dy = -dy
        elif circle_one.getCenter().getX() <= x_bottom or circle_one.getCenter().getX() >= x_top:
            dx = -dx
        elif circle_two.getCenter().getY() <= y_bottom or circle_two.getCenter().getY() >= y_top:
            dy = -dy
        elif circle_one.getCenter().getX() <= x_bottom or circle_two.getCenter().getX() >= x_top:
            dx = -dx
        elif circle_one.getCenter() == circle_two.getCenter():
            dx, dy = -dx, -dy


    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()