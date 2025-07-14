# Rock Paper Scissors – Python Game

This is a beginner-friendly terminal game built using Python.  
You will play Rock, Paper, Scissors against the computer!

---

## 🕹️ How to Play

- You will be asked to choose: **rock**, **paper**, or **scissors**.
- The computer randomly picks one of the three.
- The winner is determined using the classic rules:
  - Rock beats Scissors
  - Paper beats Rock
  - Scissors beats Paper
- Type `quit` anytime to exit the game.

---




## 🧠 How the Code Works (Line-by-Line Table)

| Line(s) | Code | Explanation |
|--------|------|-------------|
| 1 | `import random` | Imports the `random` module to allow the computer to make a random choice. |
| 3 | `choices = ["rock", "paper", "scissors"]` | A list of valid options the player and computer can choose from. |
| 5-7 | `print(...)` | Prints a welcome message and instructions for the player. |
| 9 | `while True:` | Starts an infinite loop so the game continues until the player quits. |
| 11 | `user_choice = input(...).lower()` | Takes the user's input and converts it to lowercase. |
| 13 | `if user_choice == "quit"` | If user types "quit", the game ends. |
| 14 | `print("Thanks for playing!")` | Displays a thank-you message before exiting. |
| 15 | `break` | Exits the loop (and the game). |
| 16 | `if user_choice not in choices:` | Checks if the input is not one of the valid choices. |
| 17 | `print("Invalid input! Try again.")` | Informs the player about invalid input. |
| 18 | `continue` | Restarts the loop so the user can try again. |
| 21 | `computer_choice = random.choice(choices)` | Computer randomly picks rock, paper, or scissors. |
| 22 | `print("Computer chose:", computer_choice)` | Displays the computer's choice. |
| 25 | `if user_choice == computer_choice:` | Checks for a tie. |
| 26 | `print("It's a tie!")` | Informs the user of a tie result. |
| 27-31 | `elif (...)` | Checks all win conditions for the player. |
| 32 | `print("You win!")` | Displays win message if player beats computer. |
| 33 | `else:` | If none of the win or tie conditions match, player loses. |
| 34 | `print("You lose!")` | Displays loss message. |
| 35 | `print("-" * 30)` | Prints a line separator for neatness between rounds. |
