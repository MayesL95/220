"""
Name: Lindy Mayes

File Name: greeting.py

Problem: display a heart with an animation for a greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


import time
from graphics import GraphWin, Circle, Polygon, Point, Line, Text

def main():
    win = GraphWin("Greeting Card", 500, 500)
    win.setCoords(0, 0, 10, 10)

    point1_upsidedwon = Point(5, 3)
    point2_upsidedown = Point(2.2, 5.5)
    point3_upsidedown = Point(7.8, 5.5)
    upsidedown_triangle = Polygon(point1_upsidedwon, point2_upsidedown, point3_upsidedown)
    upsidedown_triangle.setFill("red")
    upsidedown_triangle.setOutline("red")
    upsidedown_triangle.draw(win)

    point1_triangle = Point(5, 8)
    point2_triangle = Point(3.4, 5)
    point3_triangle = Point(6.6, 5)
    triangle = Polygon(point1_triangle, point2_triangle, point3_triangle)
    triangle.setFill("red")
    triangle.setOutline("red")
    triangle.draw(win)

    left_cirlce_point = Point(3.5, 6.9)
    left_cirlce = Circle(left_cirlce_point, 1.9)
    left_cirlce.setFill("red")
    left_cirlce.setOutline("red")
    left_cirlce.draw(win)

    right_circle_point = Point(6.5, 6.9)
    right_circle = Circle(right_circle_point, 1.9)
    right_circle.setFill("red")
    right_circle.setOutline("red")
    right_circle.draw(win)

    message = Text(Point(5, 2.5), "Happy Valentine's Day!")
    message.draw(win)

    point1_arrow = Point(3, 4)
    point2_arrow = Point(2.1, 3.8)
    point3_arrow = Point(2.9, 3.1)
    arrow_head = Polygon(point1_arrow, point2_arrow, point3_arrow)
    arrow_head.setFill("yellow")
    arrow_head.setOutline("blue")
    arrow_head.draw(win)
    arrow = Line(Point(1, 2), Point(2.5, 3.5))
    arrow.setWidth(2)
    arrow.setFill("blue")
    arrow.draw(win)
    for i in range(10):
        arrow_head.move(1, 1)
        arrow.move(1, 1)
        time.sleep(0.5)

    message.setText("Click anywhere to close.")
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()



