import random

# List of choices
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'quit' to exit the game.")

while True:
    # Get user input
    user_choice = input("Your choice: ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid input! Try again.")
        continue

    # Get computer choice
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
    else:
        print("You lose!")
    print("-" * 30)
