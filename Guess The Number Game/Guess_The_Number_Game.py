import random  # Importing random module to generate random numbers

def guess_the_number():
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0  # To count the number of guesses

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))  # Take user input
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop when guessed correctly
        except ValueError:
            print("Please enter a valid number.")

# Start the game
if __name__ == "__main__":
    guess_the_number()
