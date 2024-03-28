# Python

import tkinter as tk
from tkinter import messagebox
from game_logic import board, players, check_win, get_move

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create a list to hold the button objects
buttons = []

# Function to handle button click
def button_click(i):
    # Get the current player
    player = players[len(buttons[i].cget('text')) % 2]
    
    # Update the button text and disable the button
    buttons[i].config(text=player, state='disabled')
    
    # Update the game board
    board[i] = player
    
    # Check if the current player has won
    if check_win(board, player):
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        root.quit()

# Create the buttons
for i in range(9):
    button = tk.Button(root, text=' ', command=lambda i=i: button_click(i), height=3, width=6)
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the main loop
root.mainloop()