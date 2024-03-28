# Python

# Import necessary modules
from interface import root
from game_logic import print_board, get_move, check_win, board, players

def main():
    # Print the initial game board
    print_board(board)

    # Game loop
    current_player_index = 0
    while True:
        # Get the current player
        player = players[current_player_index]

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

        # Switch to the other player
        current_player_index = (current_player_index + 1) % 2

if __name__ == "__main__":
    main()
    root.mainloop()