"""
    creating a simple tic tac toe game (terminal based).
    currently the computer's move is totally random,
    in future we need to improve it.
"""
import os
from random import randint

rows = cols = 5     # change the number if you want a bigger board.
player = 'A'        # change the characters if you want anything else.
computer = 'B'

board = []
player_wins = 0
computer_wins = 0


def clear():
    """
        clear the terminal screen using os module.
    """
    os.system('clear') # or 'cls' on windows


def reset_game():
    """
        reset the board with all spaces dynamically by rows x cols.
    """
    global board
    board = []
    for row in range(rows):
        temp = []
        for col in range(cols):
            temp.append(" ")
        board.append(temp)


def draw_board():
    """
        we are simply drawing the current status of the board.
        it will be called at start and after every turn.
    """
    clear()
    print("-----" * cols)
    print("Score Board: ")
    print(player, ": ", player_wins, sep="", end="     ")
    print(computer, ": ", computer_wins, sep="")
    print("-----" * cols)
    for row in range(rows):
        for col in range(cols):
            print("| ", board[row][col], end=" ")
        print("| ")
        print("-----" * cols)


def check_for_empty():
    """
        check and see if there is a empty coordinate (return true) to continue with the game.
        if no empty coordinate (return false) found and no winner the game will be draw.
    """
    for row in range(rows):
        for col in range(cols):
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
    for col in range(cols):
        first_cell = board[0][col]
        if first_cell == ' ':
            continue
        
        for row in range(1, rows):
            if first_cell != board[row][col]:
                break
        else:
            return first_cell

    # check the winner in horizondal
    for row in range(rows):
        first_cell = board[row][0]
        if first_cell == ' ':
            continue
        
        for col in range(1, cols):
            if first_cell != board[row][col]:
                break
        else:
            return first_cell
    
    # check the winner in the cross sections.
    # check for things like this...
    # X 0 X
    # 0 X 0
    # 0 0 X
    # like x in the above example...
    # comparing 0,0 1,1 2,2 ... row and col are same!
    first_cell = board[0][0]
    if first_cell != ' ':
        for row in range(1, rows):
            if first_cell != board[row][row]:
                break
        else:
            return first_cell

    # check for things like this...
    # X 0 X
    # 0 X 0
    # X 0 0
    # like x in the above example...
    # comparing 0,2 1,1 2,0... row and col are flip sides of the array..
    first_cell = board[rows-1][0]
    if first_cell != ' ':
        for row in range(rows-1, 0, -1):
            if first_cell != board[rows-row-1][row]:
                break
        else:
            return first_cell

    # if none of the above triggered, return false
    return False


def player_turn():
    """
        we get 2 numbers (row, col) from user and if that position is already taken we will ask over and over again until we get a one of the empty position.
    """
    while True:
        try:
            x = int(input("Enter the row number (1-" + str(rows) + "): ")) - 1
            if x < 0 or x >= rows:
                print("Error! Please enter the row number within the range!")
                continue
            y = int(input("Enter the col number (1-" + str(cols) + "): ")) - 1
            if y < 0 or y >= cols:
                print("Error! Please enter the col number within the range!")
                continue
            if board[x][y] != " ":
                print("Error! That position is already taken, please choose another")
                continue
            break
        except ValueError:
            print("Error! Please only enter integers!")

    board[x][y] = player


def computer_turn():
    """
        we get 2 numbers (row, col) randomly in the range of 0 to 2 and if that position is already taken we do this over and over again until we get a one of the empty position.
    """
    x = randint(0, rows-1)
    y = randint(0, cols-1)

    while board[x][y] != " ":
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
    global player_wins, computer_wins
    winner = check_winner()
    if winner:
        print("The game is over!")
        print(winner, "wins the game!")
        if winner == player:
            player_wins = player_wins + 1
        elif winner == computer:
            computer_wins = computer_wins + 1
        return True

    if not check_for_empty() and winner is False:
        print("The game is draw!")
        return True
    
    return False


def run_a_game():
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
    while True:
        reset_game()
        run_a_game()
        print("Do you want to play again?")
        choice = input("Press 'n' to exit, anything else to continue: ")
        if choice.lower() == "n":
            break


if __name__ == '__main__':
    main()
