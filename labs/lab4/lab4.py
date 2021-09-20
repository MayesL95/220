"""
Name: Lindy Mayes
Graphics ad Accumulation practice.py
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Drawing Squares", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)



    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        user_click = win.getMouse()
        # builds a circle
        shape = Rectangle(Point(user_click.x - 10, user_click.y - 10), Point(user_click.x + 10, user_click.y + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)


    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("Draw a Rectangle", 400, 400)
    message = Text(Point(200, 350), "click twice to get opposite corners")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    rectangle = Rectangle(p1, p2)
    rectangle.setFill("blue")
    rectangle.setOutline("red")
    rectangle.draw(win)

    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()

    length = abs(x2 - x1)
    width = abs(y2 - y1)

    area = length * width
    perimeter = 2 * length * width

    txt1 = Text(Point(100, 50), "The area is:" + str(area))
    txt2 = Text(Point(100, 70), "The perimeter is:" + str(perimeter))

    txt1.draw(win)
    txt2.draw(win)


    message.setText("click anywhere to close")
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Draw a Circle", 400, 400)
    message = Text(Point(200, 350), "click twice for center and a circumference point")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    r = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    circleA = Circle(p1, r)
    circleA.setFill("blue")
    circleA.setOutline("red")
    circleA.draw(win)

    txt1 = Text(Point(100, 50), "The radius is:" + str(r))
    txt1.draw(win)

    message.setText("click anywhere to close")
    win.getMouse()
    win.close()

def pi2():
    n = eval(input("Enter the number of terms in the series"))
    acc = 1
    i = (-1)
    for x in range(n):
        num = 4
        den = 1 + 2 * x
        frac = (num / den) * ((-1) ** i)
        acc = acc + frac
    print(acc)
    print(math.pi - acc)




    pass


#def main():
    #squares()
    # rectangle()
    # circle()
    # pi2()


#main()
