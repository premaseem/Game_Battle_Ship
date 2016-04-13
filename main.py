__author__ = 'Prem Aseem Jain'

from random import randint

board = []
counter = 1
board_size = 4
ship_row = 0
ship_col = 0
continue_game = True
valid_input = True


def __init__():
    global ship_row,ship_col,board
    for x in range(0, board_size):
        board.append(["O"] * board_size)
    print_board()
    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)


def print_board():
    for row in board:
        print " ".join(row)



def valid_input_handler():
    if guess_row in range(board_size) and guess_col in range(board_size):
        pre_gussed()
        board[guess_row][guess_col] = "X"
        return True
    else :
        print "Oops, that's not even in the ocean."
        return False

def pre_gussed():
    if board[guess_row][guess_col] == "X" :
        print board[guess_row][guess_col]
        print "You guessed that one already."

def evaluate():
    if ship_row == guess_row and ship_col == guess_col :
        print "Congratulations! You sank my battleship! in {} attempts ".format(counter)
        return False
    else :
        print "You missed my battleship! Try again"
        return True

__init__()

print ship_row
print ship_col

while continue_game :
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    valid_input = valid_input_handler()
    counter += 1
    continue_game = evaluate()


