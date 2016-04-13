__author__ = 'Prem Aseem Jain'


from random import randint
from flask import Flask,jsonify,request,make_response
app = Flask(__name__)

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
    print ship_row
    print ship_col


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


# used for console based gaming
def start_game():
    global continue_game
    while continue_game :
        global guess_row,guess_col,valid_input,counter
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        valid_input = valid_input_handler()
        counter += 1
        continue_game = evaluate()





@app.route("/")
def start():
    print "starting the game"
    __init__()
    return "game started "

@app.route("/input",methods=["POST"])
def user_input():
    global guess_row,guess_col,valid_input,counter
    input = request.json
    guess_row = input["row"]
    guess_col = input["col"]
    valid_input = valid_input_handler()
    if not valid_input :
        return jsonify({"message":"invalid input"})

    counter += 1
    if evaluate():
        return jsonify({"message": "try again"})
    return jsonify({"message": "winner in {} attempts".format(counter)})

print ship_row
print ship_col


if __name__ == "__main__":
    app.run()

#    app.run()




