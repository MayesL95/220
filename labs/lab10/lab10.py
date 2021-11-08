"""
Name: Lindy Mayes
TicTacToe.py
"""

def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def display_board(board):
    print("-" * 10)
    counter = 0
    for i in range(1, 3):
        print("1", end = "")
        for j in range(1, 3):
            print (board(counter), end = "1")
            counter += 1
    print ("-" * 10)

def place_spot(board, spot, marker):
    board[spot] = marker

def legal_spot(board, spot):
    if (((board[spot] == "x") or if (board[spot] == "o")) or (spot < 1 or spot > 9)):
        return False
    else:
        return True

def game_won(board):
    winCondition = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8,], [3, 6, 9],
                    [1, 5, 9], [7, 5, 3]]
    for condition in winCondition:
        counter = 0
        for spot in condition:
            if board[spot] == "X":
                counter += 1
        if counter == 3:
            return "X Wins"
    for condition in winCondition:
        counter = 0
        for spot in condition:
            if board[spot] == "O":
                counter += 1
        if counter == 3:
            return "O Wins"

def game_over(board, turnCount):
    if ((game_won(board) == "X Wins" or if game_won(board) == "O wins")
            or (turnCount > 9)):
        return True
    else:
        return False

def play_Game():
    raw_board = build_board()
    board_created = display_board(raw_board)
    while not game_over(board_created, 9):
        turnCount = 0
        if legal_spot(board_created, spot) == True:
            spot = input("pick a spot")
            place_spot(board_created, spot, marker)
            marker = input("Enter X or O")
            turnCount += 1
        if game_won(board_created):
            print(game_won(board_created))
        if game_over(board_created, 9) == True:
            print("game over")

def main():
    play_Game()
    #pass


main()
