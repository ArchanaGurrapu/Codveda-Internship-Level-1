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