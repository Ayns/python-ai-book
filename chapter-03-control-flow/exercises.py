# Chapter 3 - Exercise Solutions
import random

# Challenge 1: Difficulty levels
print("Difficulty: 1=Easy (10 attempts), 2=Medium (7), 3=Hard (4)")
diff = input("Choose: ")
attempts = {"1": 10, "2": 7, "3": 4}.get(diff, 7)

secret = random.randint(1, 100)
for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}/{attempts}: "))
    if guess == secret:
        print(f"You got it in {attempt}!")
        break
    print("Too low." if guess < secret else "Too high.")
else:
    print(f"Game over! It was {secret}.")

# Challenge 2: Score tracker across rounds
total_score = 0
rounds = 3
for round_num in range(1, rounds + 1):
    print(f"\n--- Round {round_num} ---")
    secret = random.randint(1, 50)
    for attempt in range(1, 6):
        guess = int(input(f"Guess ({attempt}/5): "))
        if guess == secret:
            points = 6 - attempt  # fewer attempts = more points
            total_score += points
            print(f"Correct! +{points} points")
            break
        print("Too low." if guess < secret else "Too high.")
    else:
        print(f"It was {secret}. No points.")
print(f"\nFinal score: {total_score}/{rounds * 5}")
