"""
Name: Lindy Mayes

File Name: vigenere.py

Problem: Encode a message from user

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import GraphWin, Rectangle, Point, Text, Entry


def code(message, keyword):
    acc = " "
    while len(keyword) < len(message):
        keyword += keyword
    for i in range(len(message)):
        c = ord(message[i]) - 65
        key = ord(keyword[i]) - 65
        new_character = c + key + 65
        if new_character > 90:
            new_character = new_character - 26
        acc = acc + chr(new_character)
    return acc


def main():
    win = GraphWin("Vigenere", 500, 500)
    win.setCoords(0, 0, 10, 10)
    message_to_code_text = Text(Point(3, 9), "Message to Code")
    enter_keyword_text = Text(Point(3, 7), "Enter Keyword")
    message_to_code_text.draw(win)
    enter_keyword_text.draw(win)

    user_input_code = Entry(Point(7, 9), 25)
    user_input_keyword = Entry(Point(6, 7), 15)
    user_input_code.draw(win)
    user_input_keyword.draw(win)

    encode_button = Text(Point(5, 5), "Encode")
    button_outline = Rectangle(Point(4.2, 5.4), Point(5.8, 4.4))
    encode_button.draw(win)
    button_outline.draw(win)

    win.getMouse()
    encode_button.undraw()
    button_outline.undraw()

    phrase = user_input_code.getText()
    phrase = phrase.upper()
    phrase = phrase.replace(" ", "")
    key = user_input_keyword.getText()
    key = key.upper()
    key = key.replace(" ", "")

    output_text = Text(Point(5, 5), "Resulting Message")
    output_text.draw(win)
    resulting_message = Text(Point(5, 4), code(phrase, key))
    resulting_message.draw(win)

    closing_statement = Text(Point(5, 1), "Click Anywhere to Close Window")
    closing_statement.draw(win)
    win.getMouse()
    win.close()



if __name__ == '__main__':
    main()
