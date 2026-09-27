# Connect Four - Step 1
# State Representation: 6 rows x 7 columns initialized with '.'
def create_board():
    board = []
    for row in range(6):
        new_row = []
        for column in range(7):
            new_row.append('.')
        board.append(new_row)
    return board
# Function to display the board
def print_board(board):
    print("\n  0 1 2 3 4 5 6")  # Column header for user guidance
    # Print each row
    for row in board:
        print(" | " + " ".join(str(cell) for cell in row))
    print("  0 1 2 3 4 5 6")
        


# Function to get a valid column from the player
def get_valid_column(board, player):
    """
    Prompts the current player to select a column (0 to 6).
    Repeatedly prompts until a valid, non-full column is chosen.
    """
    while True:
        user_input = input(f"Player {player}, choose a column (0-6): ")
        
        # Check if input is a digit
        if not user_input.lstrip('-').isdigit():
            print("  Invalid input: please enter a whole number between 0 and 6.")
            continue                     # Jump back to the top of the loop

        # ── Check 2: Is it within bounds? ─────────────────────────────────
        col = int(user_input)
        if col < 0 or col > 6:
            print("  Invalid input: please enter a whole number between 0 and 6.")
            continue

        # Check if the column is already full
        if board[0][col] != '.':
            print(f"Column {user_input} is full! Pick a different column.")
            continue
            
        # If all checks pass, return the valid column index
        return col
# Function to drop a player's piece into a column
def drop_piece(board, col, player_symbol):
    """
    Drops the player's symbol into the lowest available row of the given column.
    Iterates backwards from the bottom row (5) up to the top row (0).
    Modifies the board in place via pass-by-reference.
    """
    # Loop backwards from row 5 (bottom) down to row 0 (top)
    for row in range(5, -1, -1):
        if board[row][col] == '.':
            board[row][col] = player_symbol
            return True  # piece successfully placed
    return False    # No empty cell found → column full


# Function to check if a player has won
def check_win(board, symbol):

    # Check every position on the board
    for r in range(6):
        for c in range(7 - 3):  # Stop at index 3 to prevent index out of bounds
            if (board[r][c] == symbol and 
                board[r][c+1] == symbol and 
                board[r][c+2] == symbol and
                board[r][c+3] == symbol):
                return True

    # ── Vertical Check ────────────────────────────────
    for r in range(6 - 3):  # stop at row 2 to avoid overflow
        for c in range(7):
            if (board[r][c]     == symbol and
                board[r + 1][c] == symbol and
                board[r + 2][c] == symbol and
                board[r+3][c] == symbol):
                return True

    # ── 3. DIAGONAL DOWN-RIGHT CHECK (↘) ─────────────────────────────
    # r increases, c increases
    for r in range(6-3):
        for c in range(7-3):
            if (board[r][c] == symbol and
                board[r+1][c+1] == symbol and
                board[r + 2][c + 2] == symbol and
                board[r + 3][c + 3] == symbol):
                return True

    # 4. Diagonal → up-right
    for r in range(3, 6):
        for c in range(7 - 3):
            if (board[r][c] == symbol and 
                board[r-1][c+1] == symbol and 
                board[r-2][c+2] == symbol and 
                board[r-3][c+3] == symbol):
                return True
    return False  # No win found

# Main game loop
board = create_board()
symbols = ['X', 'O']
turn = 0

while True:
    print_board(board)

    # Modular arithmetic: turn % 2 switches between 0 (Player 'X') and 1 (Player 'O')
    player_symbol = symbols[turn % 2]
    player_name = f"Player {turn % 2 + 1}"
        
    # Get valid column input
    col = get_valid_column(board, player_name)
    # 4. Drop the piece
    drop_piece(board, col, player_symbol)
    

    # 5. Check win
    if check_win(board, player_symbol):
        print_board(board)
        print(f"🎉 {player_name} ({player_symbol}) wins! Congratulations!\n")
        break                   # Exit the while loop → game over
    # Check draw
    if turn == 41:
        print_board(board)
        print("🤝 IT'S A DRAW! The board is completely full.\n")
        game_over = True

    # 5. Switch turn
    else:
        turn += 1   