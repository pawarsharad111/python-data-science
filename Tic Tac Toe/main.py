#-----Global Variable----------

board=["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-"]

# game is still going
game_still_going=True

# who is won? or tie?
winner=None

# whos turn is
current_player="X"

#-----Functions-------
# Play game of tic tac toe
def play_game():
    # Display  initial board
    display_board()

    # while the game still going
    while game_still_going:

        #handle the single turn of an arbitrary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #flip the player
        flip_player()

    # The game has ended
    if winner == 'X' or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("tie.")

# Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(player +"'s turn.")
    position=input("Choose Position from 1-9: ")

    valid=False

    while not valid:

        while position not  in ["1","2","3","4","5","6","7","8","9"]:
            position=input(" Choose a position between 1-9: ")

        position=int(position)-1

        if board[position] == "-":
            valid=True
        else:
            print("You cant go there. Go again.")

    board[position] = player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    # Set up global variables
    global winner

    row_winner=check_rows()
    column_winner=check_columns()
    diagonal_winner=check_diagonals()

    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None


def check_rows():
    global game_still_going
    # if any row have same value the row and not empty the row win
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any rows does have match, flage that there is win
    if row_1 or row_2 or row_3:
        #then game stop
        game_still_going = False
    #  Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3 :
        return  board[6]
    else:
        return None

def check_columns():
    global game_still_going
    # if any row have same value the row and not empty the row win
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # if any columns does have match, flage that there is win
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None

def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # if any digonal does have match, flage that there is win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    global current_player
    # if current player was, then change to O
    if current_player=='X':
        current_player='O'

    # if current player was O, then change to X
    elif current_player=="O":
        current_player="X"


play_game()

#bord
#Display board
#play game
#check win
    #check columns
    #check rows
    #check Digonals
#check tie
#flip player