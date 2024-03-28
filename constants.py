# Python

# Define the symbols for the players
PLAYER_X = 'X'
PLAYER_O = 'O'

# Define the winning conditions
WINNING_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]              # diagonals
]