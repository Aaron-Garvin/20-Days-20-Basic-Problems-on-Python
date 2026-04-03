print("Welcome to my computer quiz!")

# Ask the user if they want to play or not:
playing = input("Want to test your computer Knowledge? ")

# Check if user not wants to play, if not then quit the game:
if playing.lower() != "yes":
    print("Maybe next time!")
    quit()

print("Okay! Let's play :) ")
score = 0

# Question 1:
answer = input("Q1. What does CPU stand for? ")
if answer.lower() != "central processing unit":
    print("Wrong!")
    print("The correct answer is Central Processing Unit")
else:
    print("Correct!")
    score += 1

# Question 2:
answer = input("Q2. How many bits are in a byte? ")
if answer.lower() != "8":
    print("Wrong!")
    print("The correct answer is 8")
else:
    print("Correct!")
    score += 1

# Question 3:
answer = input("Q3. How does the computer know what to do? ")
if answer.lower() not in ["programs", "software", "instructions"]:
    print("Wrong!")
    print("The correct answer is programs")
else:
    print("Correct!")
    score += 1

# Question 4:
answer = input("Q4. What is known as the brain of the computer? ")
if answer.lower() not in ["central processing unit", "cpu"]:
    print("Wrong!")
    print("The correct answer is Central Processing Unit")
else:
    print("Correct!")
    score += 1

# Question 5:
answer = input("Q5. When was the first computer invented? ")
if answer.lower() != "1940":
    print("Wrong!")
    print("The correct answer is 1940")
else:
    print("Correct!")
    score += 1

# Question 6:
answer = input("Q6. What does RAM stand for? ")
if answer.lower() != "random access memory":
    print("Wrong!")
    print("The correct answer is random access memory")
else:
    print("Correct!")
    score += 1

print(f"\nQuiz over! You scored {score}/6")