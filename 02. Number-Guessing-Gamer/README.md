# 🎯 Number Guessing Game

A fun, interactive **command-line guessing game** built in Python — the computer picks a secret number and you have to find it, with hints to guide you every step of the way.

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🧠 About

This project is a beginner-friendly Python game that demonstrates core programming concepts like loops, conditionals, input validation, and random number generation — all wrapped in a fun, replayable guessing challenge. It runs entirely in the terminal with no external dependencies.

---

## ✨ Features

- ✅ Custom number range — you set the upper limit before each game
- ✅ Truly random secret number generated using Python's `random` module
- ✅ Helpful hints — tells you if your guess is too high or too low
- ✅ Robust input validation — handles non-numeric and invalid inputs gracefully
- ✅ Guess counter — tracks and displays how many attempts it took you
- ✅ Clean, readable code — great for beginners to study

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine
- No external libraries required

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aaron-Garvin/20-Days-20-Basic-Problems-on-Python.git
   cd "20-Days-20-Basic-Problems-on-Python/02. Number-Guessing-Game"
   ```

2. **Run the game:**
   ```bash
   python number_guessing_game.py
   ```

---

## 🎮 How to Play

1. Run the script in your terminal.
2. Enter a **positive integer** as the upper boundary of the number range (e.g. `100`).
3. Keep guessing until you find the secret number — you'll get a hint after every wrong answer.
4. Your total number of guesses is displayed when you win.

**Example session:**

```
Type a number: 100
Make a guess: 50
you were below the number!
Make a guess: 75
you were above the number!
Make a guess: 62
You got it!
You got it in 3 guesses
```

> **Pro tip:** Use a binary search strategy — always guess the midpoint of the remaining range — to find the number in the fewest guesses possible!

---

## 📁 Project Structure

```
02. Number-Guessing-Game/
│
├── number_guessing_game.py   # Main game script
└── README.md                 # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add new features like a replay option, a difficulty selector, or a leaderboard:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](../../LICENSE).

---

> Made with ❤️ and Python — happy guessing!