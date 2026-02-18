LEVEL 1 - BASIC
🔹 Task 1: Simple Calculator
I built a Python calculator that performs:
➕ Addition
➖ Subtraction
✖️ Multiplication
➗ Division
I also handled edge cases like division by zero using proper error messages. This task helped me understand functions, user input, and error handling.

🔹 Task 2: Number Guessing Game
I developed a fun game where the system generates a random number (1–100), and the user guesses it.
The program gives feedback like “Too High” or “Too Low” until the correct answer is guessed.
This improved my understanding of loops, conditional statements, and the random module.


import random

chosen_number = random.randint(1,100)

max_attempts = 6
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print(f"Try to guess the number.You have {max_attempts} attempts to guess it.\n")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > chosen_number:
        print("Too high! Try again.")
    elif guess < chosen_number:
        print("Too low! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
        break
else:
    print(f"Sorry! You used all the attempts. The number was {chosen_number}.")
