import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

score_user = 0
score_computer = 0


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"

    winning_combinations = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }

    if winning_combinations[user_choice] == computer_choice:
        return "You Win!"

    return "Computer Wins!"


def play(user_choice):
    global score_user, score_computer

    computer_choice = random.choice(choices)

    # Display choices
    user_label.config(text=f"You: {user_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")

    # Determine result
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)

    # Update score
    if result == "You Win!":
        score_user += 1
    elif result == "Computer Wins!":
        score_computer += 1

    score_label.config(
        text=f"Score: {score_user} - {score_computer}"
    )


def reset_game():
    global score_user, score_computer

    score_user = 0
    score_computer = 0

    user_label.config(text="You: —")
    computer_label.config(text="Computer: —")
    result_label.config(text="Choose your move!")
    score_label.config(text="Score: 0 - 0")


# Main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("500x500")
window.configure(bg="#1e1e2e")


# Title
title_label = tk.Label(
    window,
    text="ROCK • PAPER • SCISSORS",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#1e1e2e"
)
title_label.pack(pady=30)


# Choices
choices_frame = tk.Frame(window, bg="#1e1e2e")
choices_frame.pack(pady=20)

user_label = tk.Label(
    choices_frame,
    text="You: —",
    font=("Arial", 18),
    fg="white",
    bg="#1e1e2e"
)
user_label.grid(row=0, column=0, padx=30)

computer_label = tk.Label(
    choices_frame,
    text="Computer: —",
    font=("Arial", 18),
    fg="white",
    bg="#1e1e2e"
)
computer_label.grid(row=0, column=1, padx=30)


# Result
result_label = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 22, "bold"),
    fg="#f9e2af",
    bg="#1e1e2e"
)
result_label.pack(pady=30)


# Buttons
button_frame = tk.Frame(window, bg="#1e1e2e")
button_frame.pack()

rock_button = tk.Button(
    button_frame,
    text="🪨 Rock",
    font=("Arial", 14, "bold"),
    width=10,
    command=lambda: play("Rock")
)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(
    button_frame,
    text="📄 Paper",
    font=("Arial", 14, "bold"),
    width=10,
    command=lambda: play("Paper")
)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(
    button_frame,
    text="✂️ Scissors",
    font=("Arial", 14, "bold"),
    width=10,
    command=lambda: play("Scissors")
)
scissors_button.grid(row=0, column=2, padx=5)


# Score
score_label = tk.Label(
    window,
    text="Score: 0 - 0",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#1e1e2e"
)
score_label.pack(pady=30)


# Reset button
reset_button = tk.Button(
    window,
    text="Play Again",
    font=("Arial", 13),
    command=reset_game
)
reset_button.pack()


window.mainloop()
