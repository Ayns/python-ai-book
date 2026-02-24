# Expense Tracker - Chapter 6

import csv
import os
from datetime import datetime

FILE = "expenses.csv"
CURRENCY = "$"
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Other"]

def save_expense(date, category, description, amount):
    file_exists = os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])
        writer.writerow([date, category, description, amount])

def load_expenses():
    if not os.path.exists(FILE):
        return []
    expenses = []
    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["Amount"] = float(row["Amount"])
            expenses.append(row)
    return expenses

def show_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    totals = {}
    for expense in expenses:
        cat = expense["Category"]
        if cat in totals:
            totals[cat] = totals[cat] + expense["Amount"]
        else:
            totals[cat] = expense["Amount"]
    grand_total = sum(totals.values())
    print(f"\n{'Category':<15} {'Amount':>12}")
    print("-" * 28)
    for cat in totals:
        amount = totals[cat]
        percentage = (amount / grand_total) * 100
        print(f"{cat:<15} {CURRENCY}{amount:>8,.2f} ({percentage:.0f}%)")
    print("-" * 28)
    print(f"{'TOTAL':<15} {CURRENCY}{grand_total:>8,.2f}")

print("=" * 35)
print("   EXPENSE TRACKER")
print("=" * 35)

while True:
    print("\n1. Add Expense")
    print("2. View All")
    print("3. Summary")
    print("4. Exit")
    choice = input("\nChoice: ")
    if choice == "1":
        print("\nCategories:")
        for i in range(len(CATEGORIES)):
            print(f"  {i + 1}. {CATEGORIES[i]}")
        try:
            cat_num = int(input("Category number: "))
            if cat_num < 1 or cat_num > len(CATEGORIES):
                print("Invalid category number.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue
        category = CATEGORIES[cat_num - 1]
        description = input("Description: ")
        try:
            amount = float(input(f"Amount ({CURRENCY}): "))
        except ValueError:
            print("Invalid amount.")
            continue
        date = datetime.now().strftime("%Y-%m-%d")
        save_expense(date, category, description, amount)
        print(f"\nSaved: {category} - {description} - {CURRENCY}{amount:,.2f}")
    elif choice == "2":
        expenses = load_expenses()
        if expenses:
            for exp in expenses:
                print(f"{exp['Date']} {exp['Category']:<12} {exp['Description']:<18} {CURRENCY}{exp['Amount']:>8,.2f}")
        else:
            print("No expenses yet.")
    elif choice == "3":
        show_summary()
    elif choice == "4":
        print("\nExpenses saved to file. Goodbye!")
        break
