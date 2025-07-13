import random

def roll_dice():
    return random.randint(1, 6)

print("Welcome to the Dice Roller Game :")

while True:
    input("Press Enter to roll the dice...")
    number = roll_dice()
    print(f"You rolled a {number} CONGRATS !!!")

    play_again = input("Do you want to roll again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
