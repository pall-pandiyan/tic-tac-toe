"""
    creating a simple tic tac toe game (terminal based).
"""
import os
from random import randint

player = 'X'
computer = 'O'
xwins = 0
owins = 0

rows = 3
cols = 3
# row1 = ['' for _ in range(rows)]
# board = [row1.copy() for _ in range(cols)]

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# board = [
#     ['1', '2', '3'],
#     ['4', '5', '6'],
#     ['7', '8', '9']
# ]


def clear():
    """
        clear the terminal screen using os module.
    """
    os.system('clear') # cls for windows


def draw_board():
    """
        we are simply drawing the current status of the board.
        it will be called at start and after every turn.
    """
    clear()
    
    print("---------------")
    for row in range(rows): # r => 0, 1, 2
        for col in range(cols): # c => 0, 1, 2
            print("| ", board[row][col], end=" ")
        print("| ")
        print("---------------")


def check_for_empty():
    """
        check and see if there is a empty coordinate (return true) to continue with the game.
        if no empty coordinate (return false) found and no winner the game will be draw.
    """
    for row in range(rows): # r => 0, 1, 2
        for col in range(cols): # c => 0, 1, 2
            # print('inside the loop')
            if board[row][col] == " ":
                return True
    return False


def check_winner():
    """
        there are 8 possible ways to win this game (in 3x3)
        we are checker wheather any player won.
        if any player won, we will return the player's character
        else return false.
    """
    # check the winner in vertical
    for col in range(cols): # 0, 1, 2
        if board[0][col] != ' ' and board[0][col] == board[1][col] and board[0][col] == board[2][col]:
            return board[0][col]

    # check the winner in horizondal
    for row in range(rows):
        if  board[row][0] != ' ' and board[row][0] == board[row][1] and board[row][0] == board[row][2]:
            return board[row][0]
    
    # check the winner in the cross sections.
    if board[0][0] != ' ' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]

    # if none of the above triggered, return false
    return False


def player_turn():
    """
        we get 2 numbers (row, col) from user and if that position is already taken we will ask over and over again until we get a one of the empty position.
    """
    while True:
        try:
            x = int(input("Enter the row number (1-3): ")) - 1
            if x < 0 or x >= rows:
                print("Error! please enter a number with range!")
                continue # start the next interation
            y = int(input("Enter the col number (1-3): ")) - 1
            if y < 0 or y >= cols:
                print("Error! please enter a number with range!")
                continue
            if  board[x][y] != " ":
                print("Error! position already taken, please select another!")
                continue
            break # break out of the current loop
        except ValueError:
            print("Error! please only give number input!")

    board[x][y] = player


def computer_turn():
    """
        we get 2 numbers (row, col) randomly in the range of 0 to 2 and if that position is already taken we do this over and over again until we get a one of the empty position.
    """
    x = randint(0, rows-1)
    y = randint(0, cols-1)

    # print("x:", x)
    # print("y:", y)
    # print("board[x][y]:", board[x][y])

    while board[x][y] != " ":
        # print("board[x][y]:", board[x][y])
        x = randint(0, rows-1)
        y = randint(0, cols-1)
    
    board[x][y] = computer


def is_game_over():
    """
        check if the game is over
        if the check_winner() returns a value other than False,
            we have a winner and the function returns True.
        if check_winner() return false and there is no empty space.
            the game is draw, return true
        otherwise, the game is going on, return false
    """
    winner = check_winner()
    if winner:
        print("The game is over!")
        print(winner, "wins the game!")
        return True

    if not check_for_empty() and winner is False:
        print("The game is draw!")
        return True
    
    return False


def run_once():
    """
        play a simple tic tac toe game once.
        once a winner or draw detected break out of the function.
    """
    draw_board()
    while True:
        print(player, "'s turn!", sep='')
        player_turn()
        draw_board()
        if is_game_over():
            break
        
        print(computer, "'s turn!", sep='')
        computer_turn()
        draw_board()
        if is_game_over():
            break


def main():
    """
        run the game if the user chioce is y/Y again and again.
    """
    while True:
        run_once()
        choice = input("Do you want to continue the game? (y): ")
        if choice.lower() != "y":
            break


if __name__ == '__main__':
    main()
