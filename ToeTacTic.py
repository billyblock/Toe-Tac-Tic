#Toe Tac Tic game with a bot that chooses the best possible move each turn
#Billy Block

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = "X"

#Print the entire board
def print_board():
    print("\nCurrent Board:")
    print(board[0][0], board[0][1], board[0][2], sep="|")
    print("-+-+-")
    print(board[1][0], board[1][1], board[1][2], sep="|")
    print("-+-+-")
    print(board[2][0], board[2][1], board[2][2], sep="|")

#Compares each box in a given row. Returns the loser or "running"
def check_rows(a_board):
    for i in range(3):
        # if the row is the same string and not empty
        if len(set(a_board[i])) == 1 and a_board[i][0] != " ":
            return a_board[i][0]
    return "running"

#Checks the entire board for any spaces, if there is one, there is no tie, otherwise theres a tie
#under the assumtion that a win would be found before this function is called.
def check_tie():
    for row in board:
        if " " in row:
            return False
    return True

# Returns the loser, winner, tie, or running
def game_state():
    # check rows for win
    state = check_rows(board)
    if state != "running":
        return state

    # Columns get converted to rows for an easier check
    vertical_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] 
    for i in range(3): 
        for j in range(3): 
            vertical_board[j][i] = board[i][j]
    # check the columns (as rows) for a loss.
    state = check_rows(vertical_board)
    if state != "running":
        return state

    # manually check diagnals for a loss
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    if len(set(diag1)) == 1 and diag1[0] != " ":
        return diag1[0]
    if len(set(diag2)) == 1 and diag2[0] != " ":
        return diag2[0]

    # check tie
    if check_tie():
        return "tie"
    # if you get to this point, the game has no conclusion yet
    return "running"

# define the goals for the toe tac tic bot
def evaluate_board():
    state = game_state()
    if state == "O":
        return -1
    if state == "X":
        return 1
    if state == "tie":
        return 0
    return None

def minimax(is_computer, depth):
    # get the goal of the current board
    score = evaluate_board()
    # if theres a result
    if score != None:
        return score * (10 - depth)
    #Bot wants positive scores
    if is_computer:
        best_score = -100
        current = "O"
    else:
        best_score = 100
        current = "X"
    #Test every move to see which is best
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = current
                temp_score = minimax(not is_computer, depth + 1)
                board[i][j] = " "
                if is_computer:
                    best_score = max(best_score, temp_score)
                else:
                    best_score = min(best_score, temp_score)
    return best_score

# makes the best move from the current state.
def computer_move():
    best_score = -100
    best_move = None

    # Enumerate each possibility and make the best move.
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(False, 0)
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = "O"
    
# X is Player, O is computer. if loser is X, that means they lost and computer won
def display_winner(loser):
    if loser == "X":
        return "Computer Wins."
    if loser == "O":
        return "You win!"
    return "tie"

#Entry point to the program
while game_state() == "running":
    print_board()
    row = int(input("Select a Row (1-3): "))
    col = int(input("Select a Column (1-3): "))
    #If their input box has already been chosen
    if board[row - 1][col - 1] != " ":
        print("Invalid move, try again.")
        continue

    board[row - 1][col - 1] = player
    # If the game has finished, the computer shouldnt play
    if game_state() != "running":
        break
    computer_move()

print_board()
print("Game result:", display_winner(game_state()))
