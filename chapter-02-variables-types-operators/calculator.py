# Calculator - Chapter 2 Project

print("=" * 40)
print("  CALCULATOR")
print("=" * 40)

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print()
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")

if num2 != 0:
    division = num1 / num2
    print(f"{num1} / {num2} = {division:.2f}")
else:
    print("Cannot divide by zero!")
