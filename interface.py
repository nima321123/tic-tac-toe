# Python

import tkinter as tk
from tkinter import messagebox
from game_logic import board, players, check_win

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create a list to hold the button objects
buttons = []

# Initialize the current player
current_player_index = 0

# Function to handle button click
def button_click(i):
    global current_player_index

    # Get the current player
    player = players[current_player_index]

    # Update the button text and disable the button
    buttons[i].config(text=player, state='disabled')

    # Update the game board
    board[i] = player

    # Check if the current player has won
    if check_win(board, player):
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        root.quit()

    # Switch to the other player
    current_player_index = (current_player_index + 1) % 2

# Create the buttons
for i in range(9):
    button = tk.Button(root, text=' ', command=lambda i=i: button_click(i), height=3, width=6)
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the main loop
root.mainloop()