# 🎯 Guess The Number Game (Python)

A simple and fun Python terminal game where the computer randomly chooses a number between 1 and 100, and you try to guess it. It gives you hints like **"Too High"** or **"Too Low"** until you get it right!

---

## 🚀 How to Play

1. Run the game in your terminal or online.
2. Try to guess the number chosen by the computer.
3. It will guide you with hints until you win.
4. It shows how many attempts you took.

---

## 💻 Code Explanation

Here’s a **line-by-line breakdown** of how the code works:

| 🔢 Line | 🧠 Code                          | 💬 Description |
|--------:|----------------------------------|----------------|
| 1       | `import random`                 | Imports the `random` module to generate random numbers. |
| 3       | `def guess_the_number():`       | Defines the main function that holds the game logic. |
| 4       | `number_to_guess = random.randint(1, 100)` | Randomly picks a number between 1 and 100. |
| 5       | `attempts = 0`                  | Initializes a counter to track number of guesses. |
| 7–8     | `print(...)`                    | Displays welcome message and game instructions. |
| 10      | `while True:`                   | Starts an infinite loop for repeated guesses. |
| 11      | `try:`                          | Starts a try block to catch invalid input. |
| 12      | `guess = int(input(...))`       | Takes user's input and converts it to an integer. |
| 13      | `attempts += 1`                 | Increments the attempt counter by 1. |
| 15–17   | `if guess < number_to_guess:`   | If guess is lower, hint "Too low!". |
| 18–20   | `elif guess > number_to_guess:` | If guess is higher, hint "Too high!". |
| 21–23   | `else:`                         | If guess is correct, congratulates and exits loop. |
| 24      | `break`                         | Breaks out of the loop when guessed correctly. |
| 25–26   | `except ValueError:`            | Handles errors if input is not a valid number. |
| 29      | `if __name__ == "__main__":`    | Ensures the function runs when this file is executed. |
| 30      | `guess_the_number()`            | Calls the game function to start the game. |

---

## ▶️ Example Output

