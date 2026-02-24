# Personal Greeting Generator - Chapter 1

print("=" * 50)
print("   PERSONAL GREETING GENERATOR")
print("=" * 50)
print()

name = input("What is your name? ")
birth_year = input("What year were you born? ")
city = input("Which city do you live in? ")
hobby = input("What is your favorite hobby? ")

age = 2026 - int(birth_year)

print()
print("-" * 50)
print(f"Hello, {name}!")
print(f"You are approximately {age} years old.")
print(f"Living in {city} sounds wonderful!")
print(f"{hobby} is a great way to spend time.")
print()
days = age * 365
print(f"Fun fact: You have lived about {days:,} days!")
print(f"That is {days * 24:,} hours of experience!")
print("-" * 50)
