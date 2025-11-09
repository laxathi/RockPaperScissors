import tkinter as tk
import random

# Global variables to store scores
wins = 0
losses = 0
ties = 0

# Function to get the computer's choice
def computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to get the score
def decide_winner(player, computer):
    global wins, losses, ties
    
    if player == computer:
        ties += 1
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper"):
        wins += 1
        return "You win!"
    else:
        losses += 1
        return "You lose!"

# Function to handle player's choice
def play(choice, result_label, score_label):
    comp_choice = computer_choice()
    result = decide_winner(choice, comp_choice)
    result_label.config(text=f"Computer chose: {comp_choice}\n{result}")
    score_label.config(text=f"Wins: {wins}  Losses: {losses}  Ties: {ties}")

# Function to quit the game
def quit_game(window):
    window.quit()

def main():
    global wins, losses, ties
    
    # Creating the main window
    window = tk.Tk()
    window.title("Rock Paper Scissors Game")

    # Increase the window size for better layout
    window.geometry("500x400")

    # Adding a label to display the result
    result_label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
    result_label.pack(pady=20)

    # Adding a label to display the score
    score_label = tk.Label(window, text=f"Wins: {wins}  Losses: {losses}  Ties: {ties}", font=("Arial", 12))
    score_label.pack(pady=10)

    # Adding buttons for each choice
    rock_button = tk.Button(window, text="Rock", width=10, height=2, font=("Arial", 12), command=lambda: play("Rock", result_label, score_label))
    rock_button.pack(side="left", padx=20)

    paper_button = tk.Button(window, text="Paper", width=10, height=2, font=("Arial", 12), command=lambda: play("Paper", result_label, score_label))
    paper_button.pack(side="left", padx=10)

    scissors_button = tk.Button(window, text="Scissors", width=10, height=2, font=("Arial", 12), command=lambda: play("Scissors", result_label, score_label))
    scissors_button.pack(side="left", padx=10)

    # Adding a quit button to exit the game
    quit_button = tk.Button(window, text="Quit Game", width=20, height=2, font=("Arial", 12), command=lambda: quit_game(window))
    quit_button.pack(side="left", padx=10)  # Add more padding to ensure it's at the bottom

    # Running the application
    window.mainloop()

# Ensure this block only runs when the script is executed directly
if __name__ == "__main__":
    main()
