# We are importing ranom module to generate random numbers:
import random

# Take a top range number from the users, and take input in form of string:
top_of_range = input("Type a number: ")

# Here .isdigit() used to check if the string is a number or not.
# If the string is a number then we are converting it into integer using int() function.
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    # Check if the number is less than or equal to 0, if true print a msg, and quit 
    if top_of_range <= 0:
        print("Please type a number greater then 0 next time.")
        quit()
            
else: 
    print("Plase type a number next time.")
    quit()

# Here we are generating a random number between 0 and the top of range number using randint() function of random module.
random_number = random.randint(0, top_of_range)

# We have make a variable to count no. of guesses, user taken to guess the number.
guesses=0

# This while loop will always work:
while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    # same logic, explained before:
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    # now check the user input number is correct or wrong:
    if user_guess == random_number:
        print("You got it!")
        break
    # Check if the number guess by user is greater than the random number.
    elif user_guess > random_number:
        print("you were above the number!")
    else:
        print("you were below the number!")

print("You got it in", guesses, "guesses")

