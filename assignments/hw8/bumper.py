"""
Name: Lindy Mayes

File Name: bumper.py

Problem: simulate bumper cars with circles

Certification of Authenticity:
I certify that this assignment is entirely my own work but had a tutor's assistance
"""

from graphics import *
from random import randint
import time
import math


def get_random(move_amount):
    random_move_amount = randint(-move_amount, move_amount)
    return random_move_amount


def did_collide(ball1, ball2):
    point1 = ball1.getCenter()
    x1 = point1.getX()
    y1 = point1.getY()

    point2 = ball2.getCenter()
    x2 = point2.getX()
    y2 = point2.getY()

    if (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= (ball1.getRadius() + ball2.getRadius())):
        return True
    else:
        return False

def hit_vertical(ball, win):
    if (ball.getCenter()).getX() >= 200 or (ball.getCenter()).getX() <= 0:
        return True
    else:
        return False

def hit_horizontal(ball, win):
    if (ball.getCenter()).getY() >= 200 or (ball.getCenter()).getY() <= 0:
        return True
    else:
        return False


def get_random_color():
    random_color = randint(200, 300)
    return random_color


def create_bumpercar_sim():
    win = GraphWin("Bumper Cars Simulation", 200, 200)
    radius = 10

    circle_one_point = Point(20, 20)
    circle_one = Circle(circle_one_point, radius)
    circle_one.setOutline("white")
    circle_one.setFill("red")
    circle_one.draw(win)

    circle_two_point = Point(100, 100)
    circle_two = Circle(circle_two_point, radius)
    circle_two.setOutline("white")
    circle_two.setFill("blue")
    circle_two.draw(win)

    move_speed_x1 = get_random(13)
    move_speed_x2 = get_random(13)
    move_speed_y1 = get_random(13)
    move_speed_y2 = get_random(13)

    while win.checkMouse() == None:
        if did_collide(circle_one, circle_two) == True:
            move_speed_x1 = -move_speed_x1
            move_speed_y1 = -move_speed_y1
            move_speed_x2 = -move_speed_x2
            move_speed_y2 = -move_speed_y2
        if hit_vertical(circle_one, win) == True:
            move_speed_x1 = -move_speed_x1
        if hit_vertical(circle_two, win) == True:
            move_speed_x2 = -move_speed_x2
        if hit_horizontal(circle_one, win) == True:
            move_speed_y1 = -move_speed_y1
        if hit_horizontal(circle_two, win) == True:
            move_speed_y2 = -move_speed_y2
        circle_one.move(move_speed_x1, move_speed_y1)
        circle_two.move(move_speed_x2, move_speed_y2)

        time.sleep(.05)
    win.close()


def main():
    create_bumpercar_sim()


if __name__ == '__main__':
    main()