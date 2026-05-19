import sys

def print_board(board):
    """Displays the current board state."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    """Checks if the specified player has won the game."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

def is_board_full(board):
    """Returns True if the board contains no empty spaces."""
    return ' ' not in board

def get_valid_move(board):
    """Prompts the user for a move and validates input."""
    while True:
        try:
            move_input = input("Enter your move (1-9): ")
            move_index = int(move_input) - 1
            if 0 <= move_index <= 8 and board[move_index] == ' ':
                return move_index
            elif board[move_index] != ' ':
                print("Error: That space is already occupied.")
            else:
                print("Error: Invalid position. Enter a number between 1 and 9.")
        except ValueError:
            print("Error: Please enter a valid number (1-9).")

def play_game():
    """Initializes and runs the Tic Tac Toe game loop."""
    board = [' '] * 9
    current_player = 'X'
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1-9 starting from top-left.")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        move_idx = get_valid_move(board)
        board[move_idx] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("The game is a draw.")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
