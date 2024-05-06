def print_board(board):
    """
    Print the current state of the Tic-Tac-Toe board.

    Args:
        board (list of lists): Represents the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Use '-' to separate rows


def check_winner(board):
    """
    Check if there's a winner on the Tic-Tac-Toe board.

    Args:
        board (list of lists): Represents the Tic-Tac-Toe board.

    Returns:
        bool: True if there's a winner, False otherwise.
    """
    for row in board:
        if row[0] == row[1] == row[2] != " ":  # Check horizontal rows
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":  # Check vertical columns
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":  # Check diagonal (top-left to bottom-right)
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":  # Check diagonal (top-right to bottom-left)
        return True

    return False  # No winner found


def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize 3x3 board with empty spaces
    player = "X"  # Starting player

    while not check_winner(board) and any(" " in row for row in board):
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":  # Check if the chosen spot is empty
                    board[row][col] = player  # Place player's marker
                    player = "O" if player == "X" else "X"  # Switch player
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid input! Please enter row and column values between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter valid row and column values.")

    print_board(board)

    if check_winner(board):
        winner = "O" if player == "X" else "X"  # Previous player won
        print(f"Player {winner} wins!")
    else:
        print("It's a tie! No winner.")

# Run the game
tic_tac_toe()
