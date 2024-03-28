# Python

from constants import PLAYER_X, PLAYER_O, WINNING_COMBINATIONS

# Define the game board
board = [' ' for _ in range(9)]

# Define the players
players = [PLAYER_X, PLAYER_O]

# Function to print the game board
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])

# Function to check if a player has won
def check_win(board, player):
    for combination in WINNING_COMBINATIONS:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False
"""For each combination, the function checks if the board cells at those indices all contain 
the current player's symbol. This is done using the equality comparison operator (==). 
If all three cells contain the current player's symbol, this means the player has a winning line, 
so the function returns True."""

# Function to get a player's move
def get_move(player):
    move = int(input(f"Player {player}, enter your move (0-8): "))
    while board[move] != ' ':
        move = int(input("Invalid move. Enter your move (0-8): "))
        #If the cell is not empty, this means that a move has already been made in that cell,
        #so the move is invalid. In this case, the function asks the player to enter a new move."""
    return move