# Chapter 1 - Exercise Solutions

# Challenge 1: Ask for favorite food
name = input("What is your name? ")
food = input("What is your favorite food? ")
print(f"Hello, {name}! I hear you love {food}!")

# Challenge 2: Calculate months alive
birth_year = input("What year were you born? ")
age = 2026 - int(birth_year)
months = age * 12
print(f"You have lived approximately {months:,} months!")

# Challenge 3: Try entering "abc" as birth year
# This will crash with: ValueError: invalid literal for int()
# Chapter 6 teaches how to handle this with try/except
