
# 🎮 Typing Speed Tester

A simple Python-based terminal game that tests how fast and accurately you can type a given sentence.

---

## 🧠 What is this Game?

This **Typing Speed Tester** helps you practice your typing skills by giving you random sentences to type.  
It then calculates and displays your:

- ⏱️ Typing speed (WPM - Words Per Minute)
- ✅ Accuracy (Percentage of correct characters)

---

## 🕹️ How to Play

1. Run the game script.
2. A sentence will appear on the screen.
3. Type the sentence as fast and accurately as possible.
4. Press `Enter` when done.
5. Get your **WPM**, **Accuracy**, and **Time Taken** as feedback.

---



## 🧪 Sample Output

```
=== Typing Speed Tester ===
Press Enter when you are ready...

Type the following sentence:

Typing fast requires practice and focus.

Your input: Typing fast requires practice and focus.

=== Results ===
Time Taken     : 10.3 seconds
Speed          : 35.2 WPM
Accuracy       : 100.0%
```

---

## 📘 How the Code Works 

| **Line No.** | **Code** | **Explanation** |
|--------------|----------|------------------|
| 1 | `import time` | Imports the `time` module to measure how long the user takes to type. |
| 2 | `import random` | Imports the `random` module to choose a random sentence. |
| 5–10 | `sentences = [...]` | A list of sample sentences that the program will randomly choose from. |
| 12 | `def get_sentence():` | Defines a function to get a random sentence. |
| 13 | `return random.choice(sentences)` | Picks and returns one random sentence from the list. |
| 15 | `def calculate_speed_accuracy(...):` | Defines a function to calculate WPM and accuracy. |
| 16 | `time_taken = end_time - start_time` | Calculates how many seconds the user took to type. |
| 17 | `time_taken_minutes = time_taken / 60` | Converts time taken into minutes. |
| 18 | `words = typed.split()` | Splits the typed input into words to count them. |
| 19 | `wpm = len(words) / time_taken_minutes ...` | Calculates Words Per Minute (WPM). |
| 21 | `correct_chars = sum(...)` | Counts how many characters match between original and typed input. |
| 22 | `accuracy = (correct_chars / len(original)) * 100` | Calculates percentage of correct characters. |
| 24 | `return wpm, accuracy, time_taken` | Returns all the calculated results. |
| 27 | `def typing_test():` | Defines the main function for the typing test. |
| 28 | `print("=== Typing Speed Tester ===")` | Displays the game title. |
| 29 | `input("Press Enter when you are ready...")` | Waits for the user to start the game. |
| 31 | `sentence = get_sentence()` | Calls function to get a random sentence. |
| 32 | `print("\nType the following sentence:\n")` | Shows instructions. |
| 33 | `print(sentence)` | Displays the sentence to type. |
| 34 | `print()` | Prints an empty line for spacing. |
| 36 | `start_time = time.time()` | Starts the timer. |
| 37 | `typed = input("Your input: ")` | Gets the user’s typed sentence. |
| 38 | `end_time = time.time()` | Stops the timer. |
| 40 | `wpm, accuracy, time_taken = ...` | Calls the calculation function and stores results. |
| 42 | `print("\n=== Results ===")` | Displays the result heading. |
| 43 | `print(f"Time Taken : ...")` | Prints total time taken. |
| 44 | `print(f"Speed : ...")` | Prints the typing speed (WPM). |
| 45 | `print(f"Accuracy : ...")` | Prints the typing accuracy. |
| 48 | `if __name__ == "__main__":` | Ensures this script runs only when executed directly. |
| 49 | `typing_test()` | Starts the game by calling the main function. |

---

