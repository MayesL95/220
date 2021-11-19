"""
Name: Lindy Mayes

File Name: bumper.py

Problem: create a button class

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import *
from random import randint
from Button import Button

def main():
    win = GraphWin("Three Door Game", 500, 500)
    win.setCoords(0, 0, 10, 10)

    door1 = Button(Rectangle(Point(0.5, 6), Point(3, 4.5)), "Door1")
    door1.draw(win)
    door2 = Button(Rectangle(Point(3.8, 6), Point(6.33, 4.5)), "Door2")
    door2.draw(win)
    door3 = Button(Rectangle(Point(7, 6), Point(9.5, 4.5)), "Door3")
    door3.draw(win)

    top_message = Text(Point(5, 8), "I have a secret door")
    top_message.draw(win)
    bottom_message = Text(Point(5, 1), "click to choose my door")
    bottom_message.draw(win)

    doors = [door1, door2, door3]
    secret_door = randint(0, len(doors))
    choice = win.getMouse()
    while choice == " ":
        if choice == secret_door:
            top_message.setText('You win!')
            secret_door.color_button("green")
            bottom_message.setText("click to close")
        else:
            top_message.setText("You lose!")
            secret_door.color_button("red")
            bottom_message.setText(secret_door, "was my secret door")

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()