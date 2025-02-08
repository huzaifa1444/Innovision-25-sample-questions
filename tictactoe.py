# Mapping position codes to board indices
position_map = [
    ["ul", "um", "ur"],
    ["ml", "mm", "mr"],
    ["dl", "dm", "dr"]
]

def check_winner(board):
    """Checks if a player has won the game."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_draw(board):
    """Checks if the board is full, leading to a draw."""
    return all(cell != " " for row in board for cell in row)

def get_position_coordinates(move):
    """Returns the row and column index for a given position code."""
    for i in range(3):
        for j in range(3):
            if position_map[i][j] == move:
                return [i,j]
    return None

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe without printing the board."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        move = input(f"Player {player}, enter your move (ul, um, ur, ml, mm, mr, dl, dm, dr): ")

        # Get board coordinates
        position = get_position_coordinates(move)
        if position is None:
            print("Invalid input! Use the correct format.")
            continue

        row=position[0]
        col=position[1]
        if board[row][col] != " ":
            print("Cell is already occupied! Try again.")
            continue

        # Make the move
        board[row][col] = player
        winner = check_winner(board)

        # Check for winner or draw
        if winner:
            print(f"Player {winner} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()
