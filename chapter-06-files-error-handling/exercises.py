# Chapter 6 - Exercise Solutions
import json
import csv

# 1. Journal app (text file)
def add_entry():
    entry = input("Today's entry: ")
    with open("journal.txt", "a") as f:
        from datetime import datetime
        f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}]\n{entry}\n")
    print("Saved!")

def read_journal():
    try:
        with open("journal.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No entries yet.")

# 2. Safe number input with error handling
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# 3. Config file manager (JSON)
def load_config(filename="config.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"theme": "light", "language": "en", "font_size": 14}

def save_config(config, filename="config.json"):
    with open(filename, "w") as f:
        json.dump(config, f, indent=4)

config = load_config()
print(f"Current config: {config}")
