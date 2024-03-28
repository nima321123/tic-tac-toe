# Tic Tac Toe

This is a simple implementation of the classic game Tic Tac Toe in Python. The game can be played in the console or using a graphical user interface (GUI) created with Tkinter.

## Files

- `main.py`: This is the main file that brings everything together. It starts the game and manages the game loop.
- `game_logic.py`: This file contains the game logic, including the game board, the players, and the functions to print the board, check for a win, and get a player's move.
- `constants.py`: This file defines the constants used in the game, such as the symbols for the players and the winning combinations.
- `interface.py`: This file creates the GUI for the game using Tkinter.

## How to Play

1. Run `main.py` to start the game.
2. The players take turns to enter their moves. In the console, enter the index of the cell where you want to place your symbol (0-8). In the GUI, click on the cell where you want to place your symbol.
3. The game continues until one player has a winning line or all cells are filled. If a player has a winning line, that player wins. If all cells are filled and no player has a winning line, the game is a draw.

## Requirements

- Python 3
- Tkinter (for the GUI)

## Future Improvements

- Add a feature to play against the computer.
- Improve the GUI design.