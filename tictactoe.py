import sys

def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

def is_board_full(board):
    return ' ' not in board

def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            if board[move] != ' ':
                print("That spot is already taken!")
                continue
            return move
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Use numbers 1-9 to select positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    board = [' '] * 9
    current_player = 'X'

    while True:
        print_board(board)
        move = get_player_move(board, current_player)
        board[move] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Congratulations! Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame exited.")
        sys.exit(0)