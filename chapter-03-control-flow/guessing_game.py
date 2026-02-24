# Number Guessing Game - Chapter 3 Project

import random

print("=" * 40)
print("  NUMBER GUESSING GAME")
print("=" * 40)
print("I picked a number between 1 and 100.")
print("You have 7 attempts.")
print()

secret = random.randint(1, 100)

for attempt in range(1, 8):
    text = input(f"Attempt {attempt}/7 - Your guess: ")

    if not text.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(text)

    if guess == secret:
        print(f"\nYou got it in {attempt} attempt(s)!")
        if attempt <= 3:
            print("Incredible!")
        elif attempt <= 5:
            print("Well done!")
        else:
            print("Close call!")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")
else:
    print(f"\nGame over! The number was {secret}.")
