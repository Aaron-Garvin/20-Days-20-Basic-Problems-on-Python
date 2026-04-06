# 🗺️ Adventure Game

A fun, interactive **command-line text adventure game** built in Python — make choices, explore paths, and find out if you win or lose!

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [Game Map](#game-map)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🧠 About

This project is a beginner-friendly Python game that demonstrates core programming concepts like conditionals, nested if-else statements, and user input handling — all wrapped in a fun story-driven adventure. It runs entirely in the terminal with no external dependencies.

---

## ✨ Features

- ✅ Personalised experience — greets you by your name
- ✅ Multiple branching paths — every choice matters
- ✅ Nested decision making — choices lead to more choices
- ✅ Case-insensitive input — type `LEFT`, `left` or `Left`, all work
- ✅ Win & lose endings — only one path leads to victory!
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
   cd "20-Days-20-Basic-Problems-on-Python/04. Adventure-Game"
   ```

2. **Run the game:**
   ```bash
   python adventure_game.py
   ```

---

## 🎮 How to Play

1. Run the script in your terminal.
2. Enter your name when prompted.
3. Read each scenario carefully and type your choice.
4. Every decision takes you down a different path.
5. Find the one path that leads to victory! 🏆

**Example session:**

```
Enter your user name: Aaron
Welcome to the adventure game, Aaron!

# You are on a dirt road, it has come to an end and you
  can go left or right. Which way would you like to go? : right

# You come to a bridge, it looks wobbly, do you want to
  cross it or head back? Type cross to cross it and back
  to head back: cross

# You crossed the bridge and found a treasure chest full
  of gold. You win! 🏆
```

---

## 🗺️ Game Map

```
                    START
                      │
          ┌───────────┴───────────┐
         LEFT                   RIGHT
          │                       │
          ▼                       ▼
        River                   Bridge
          │                       │
    ┌─────┴─────┐           ┌─────┴─────┐
   SWIM        WALK        BACK       CROSS
    │            │           │           │
    ▼            ▼           ▼           ▼
  LOSE         LOSE        LOSE        WIN 🏆
```

> **Hint:** There is only ONE winning path. Choose wisely! 😉

---

## 📁 Project Structure

```
04. Adventure-Game/
│
├── adventure_game.py    # Main game script
└── README.md            # Project documentation
```

---

## 🧠 Code Overview

| Component | Description |
|-----------|-------------|
| `input()` | Captures the player's name and choices |
| `.lower()` | Makes all input case-insensitive |
| `if / elif / else` | Controls the branching story paths |
| Nested conditionals | Second-level choices after the first decision |

### Key Python Concepts Used

- **`input()`** — for reading player name and choices
- **`.lower()`** — for case-insensitive input handling
- **`if / elif / else`** — for branching game logic
- **Nested conditionals** — for multi-level decision making
- **String concatenation** — for personalised welcome message

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add more paths, new storylines, a scoring system, or even ASCII art:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](../../LICENSE).

---

> Made with ❤️ and Python — choose your path wisely! 🗺️