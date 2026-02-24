# Password Generator & Strength Checker - Chapter 5 Project

import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%&"
    password = ""
    for i in range(length):
        one_char = random.choice(characters)
        password = password + one_char
    return password


def check_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score = score + 1
    if len(password) >= 12:
        score = score + 1

    # Check for character types
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in "!@#$%&":
            has_special = True

    if has_upper: score = score + 1
    if has_lower: score = score + 1
    if has_digit: score = score + 1
    if has_special: score = score + 1

    # Determine strength label
    if score >= 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"


# Main program
print("=" * 40)
print("  PASSWORD TOOL")
print("=" * 40)

while True:
    print("\n1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        length = int(input("Password length (8-32): "))
        password = generate_password(length)
        strength = check_strength(password)
        print(f"\nPassword: {password}")
        print(f"Strength: {strength}")

    elif choice == "2":
        password = input("Enter password to check: ")
        strength = check_strength(password)
        print(f"Strength: {strength}")

    elif choice == "3":
        print("Stay secure!")
        break
