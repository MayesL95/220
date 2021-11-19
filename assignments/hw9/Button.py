"""
Name: Lindy Mayes

File Name: bumper.py

Problem: create a button class

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import *

class Button:
    def __init__(self, rectangle_shape, string_label):
        self.shape = rectangle_shape
        self.text = Text(rectangle_shape.getCenter(), string_label)

    def get_label(self):
        return self.text

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self, win):
        self.shape.undraw(win)
        self.text.undraw(win)

    def is_clicked(self, point):
        if point in self.shape:
            shape.color_button("green")

    def color_button(self, color):
        self.shape.setFill(color)


    def set_label(self, label):
        self.text = label








