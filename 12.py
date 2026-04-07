# Number Guessing Game

import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number (1-100): "))

    if guess == number:
        print("Correct! You guessed it 🎉")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")