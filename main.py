# Python

# Import necessary modules
from interface import root
from game_logic import print_board, get_move, check_win, board, players

def main():
    # Print the initial game board
    print_board(board)

    # Game loop
    while True:
        for player in players:
            # Get the player's move
            move = get_move(player)

            # Update the game board
            board[move] = player

            # Print the updated game board
            print_board(board)

            # Check if the current player has won
            if check_win(board, player):
                print(f"Player {player} wins!")
                return

if __name__ == "__main__":
    main()
    root.mainloop()