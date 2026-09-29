import random

print("Welcome to number guessing game!")

number = random.randrange(1, 101)
attempts = 0

while True:
    guess = int(input("guess a number(1-101): "))
    attempts += 1

    if guess < number:
        print("Better luck next time. Go lower.")

    elif guess > number:
        print("Better luck next time. Go higher.")

    else:
        print("Congo! You guessed it right.")
        print("Attempts:", attempts)
        break