# importing the random module to generate random numbers for the computer's choice
import random

# Initializing the user's and computer's win counts to zero
user_wins=0
computer_wins=0

# Defining the possible options for the game
options=["rock","paper","scissors"]

# Starting an infinite loop to continuously prompt the user for input until they choose to quit
while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    # If the user input is not one of the valid options, the loop continues and prompts the user again
    if user_input not in ["rock","paper","scissors"]:
        continue
    
    random_number=random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2
     
    # The computer's choice is determined by the random number generated, which corresponds to one of the options in the list
    computer_pick=options[random_number]
    print("Compute picked", computer_pick + ".")

    # The following condition tell the user if they won, lost, or tied based on their input and the computer's choice.
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("You tie with computer!")

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "paper":
        print("You tie with computer!")

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("You tie with computer!")

    else:
        print("You lost!")
        computer_wins += 1

# After the user decides to quit the game, the program prints out the total number of wins for both the user and computer.
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")