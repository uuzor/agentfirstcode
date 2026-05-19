import sys


def display_board(board):
    """Display the current state of the board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_win(board, player):
    """Check if the given player has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def is_draw(board):
    """Check if the game is a draw."""
    return all(cell != ' ' for cell in board)


def get_player_move(board, player):
    """Get and validate the move from the player."""
    while True:
        try:
            move_input = input(f"Enter position (1-9) for Player {player}: ")
            move = int(move_input) - 1
            
            if 0 <= move <= 8:
                if board[move] == ' ':
                    return move
                else:
                    print("That position is occupied. Try again.")
            else:
                print("Invalid number. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    board = [' '] * 9
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print("Use numbers 1-9 to select your position on the keypad layout:")
    print(" 7 | 8 | 9 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 1 | 2 | 3 ")

    while True:
        display_board(board)
        
        move = get_player_move(board, current_player)
        board[move] = current_player
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
        
        if is_draw(board):
            display_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame terminated.")