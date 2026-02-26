# Chapter 2 - Exercise Solutions

# Challenge 1: Power operation
num1 = float(input("Base number: "))
num2 = float(input("Exponent: "))
print(f"{num1} ** {num2} = {num1 ** num2}")

# Challenge 2: BMI Calculator
weight = float(input("Weight in kg: "))
height = float(input("Height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.1f}")

# Challenge 3: Currency converter
usd = float(input("Amount in USD: "))
eur = usd * 0.92
print(f"${usd:.2f} = €{eur:.2f}")
