import time
import random

# List of sample sentences
sentences = [
    "Python is a powerful programming language.",
    "Typing fast requires practice and focus.",
    "Artificial Intelligence is the future.",
    "Always comment your code for clarity.",
    "Debugging is twice as hard as writing the code."
]

def get_sentence():
    return random.choice(sentences)

def calculate_speed_accuracy(original, typed, start_time, end_time):
    time_taken = end_time - start_time
    time_taken_minutes = time_taken / 60
    words = typed.split()
    wpm = len(words) / time_taken_minutes if time_taken_minutes > 0 else 0

    correct_chars = sum(1 for o, t in zip(original, typed) if o == t)
    accuracy = (correct_chars / len(original)) * 100

    return wpm, accuracy, time_taken

# Main function
def typing_test():
    print("=== Typing Speed Tester ===")
    input("Press Enter when you are ready...")
    
    sentence = get_sentence()
    print("\nType the following sentence:\n")
    print(sentence)
    print()

    start_time = time.time()
    typed = input("Your input: ")
    end_time = time.time()

    wpm, accuracy, time_taken = calculate_speed_accuracy(sentence, typed, start_time, end_time)

    print("\n=== Results ===")
    print(f"Time Taken     : {round(time_taken, 2)} seconds")
    print(f"Speed          : {round(wpm, 2)} WPM")
    print(f"Accuracy       : {round(accuracy, 2)}%")

# Run the game
if __name__ == "__main__":
    typing_test()
