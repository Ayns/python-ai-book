# Chapter 5 - Exercise Solutions

# 1. Temperature converter with default
def convert_temp(value, from_unit="C"):
    if from_unit.upper() == "C":
        return value * 9/5 + 32, "F"
    else:
        return (value - 32) * 5/9, "C"

temp, unit = convert_temp(100)
print(f"100°C = {temp}°{unit}")

temp, unit = convert_temp(212, "F")
print(f"212°F = {temp}°{unit}")

# 2. Statistics function using *args
def stats(*numbers):
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }

result = stats(10, 20, 30, 40, 50)
for key, value in result.items():
    print(f"  {key}: {value}")

# 3. Your own module — create helpers.py with reusable functions
# Then: from helpers import convert_temp, stats
