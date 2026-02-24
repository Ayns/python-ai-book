# AI-Powered Personal Finance Tracker - Chapter 18 Capstone
# Requirements: pip install openai pandas python-dotenv

import os
import csv
import json
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ─── Configuration ───
FILE = "expenses.csv"
CURRENCY = "$"
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Other"]


def auto_categorize(description):
    """Use AI to auto-categorize an expense"""
    categories_str = ", ".join(CATEGORIES)
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": f"Categorize expenses into exactly one of: {categories_str}. Return ONLY the category name, nothing else."},
                {"role": "user", "content": description}
            ],
            temperature=0
        )
        category = response.choices[0].message.content.strip()
        if category in CATEGORIES:
            return category
        return "Other"
    except openai.APIError:
        return "Other"


def save_expense(date, category, description, amount):
    """Save an expense to CSV"""
    file_exists = os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])
        writer.writerow([date, category, description, amount])


def load_expenses():
    """Load all expenses from CSV"""
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
    """Display expense summary with category breakdown"""
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return

    totals = {}
    for exp in expenses:
        cat = exp["Category"]
        totals[cat] = totals.get(cat, 0) + exp["Amount"]

    grand_total = sum(totals.values())
    print(f"\n{'Category':<15} {'Amount':>12} {'Share':>8}")
    print("-" * 37)
    for cat, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        pct = (amount / grand_total) * 100
        print(f"{cat:<15} {CURRENCY}{amount:>10,.2f} {pct:>6.1f}%")
    print("-" * 37)
    print(f"{'TOTAL':<15} {CURRENCY}{grand_total:>10,.2f}")


def generate_insights():
    """Use AI to analyze spending patterns and give advice"""
    expenses = load_expenses()
    if len(expenses) < 3:
        print("Need at least 3 expenses for insights.")
        return

    # Build summary for AI
    totals = {}
    for exp in expenses:
        cat = exp["Category"]
        totals[cat] = totals.get(cat, 0) + exp["Amount"]

    grand_total = sum(totals.values())
    summary = f"Monthly spending: {CURRENCY}{grand_total:,.2f}\n"
    for cat, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        pct = (amount / grand_total) * 100
        summary += f"  {cat}: {CURRENCY}{amount:,.2f} ({pct:.0f}%)\n"

    recent = expenses[-5:]
    summary += "\nRecent expenses:\n"
    for exp in recent:
        summary += f"  {exp['Date']}: {exp['Description']} - {CURRENCY}{exp['Amount']:,.2f}\n"

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a personal finance advisor. Give specific, actionable advice based on spending data. Keep response under 200 words."},
                {"role": "user", "content": f"Analyze my spending and give 3 specific tips:\n\n{summary}"}
            ],
            temperature=0.5
        )
        print(f"\n{'=' * 40}")
        print("  AI SPENDING INSIGHTS")
        print(f"{'=' * 40}")
        print(response.choices[0].message.content)
    except openai.APIError as err:
        print(f"Error: {err}")


# ─── Main Program ───
print("=" * 40)
print("  AI FINANCE TRACKER")
print("=" * 40)

while True:
    print("\n1. Add Expense (AI auto-categorize)")
    print("2. Add Expense (manual category)")
    print("3. View All Expenses")
    print("4. Spending Summary")
    print("5. AI Insights")
    print("6. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        description = input("Description: ").strip()
        try:
            amount = float(input(f"Amount ({CURRENCY}): "))
        except ValueError:
            print("Invalid amount.")
            continue
        category = auto_categorize(description)
        print(f"Auto-categorized as: {category}")
        confirm = input("Accept? (y/n): ").strip().lower()
        if confirm != "y":
            print("Categories:", ", ".join(f"{i+1}.{c}" for i, c in enumerate(CATEGORIES)))
            try:
                idx = int(input("Category number: ")) - 1
                category = CATEGORIES[idx]
            except (ValueError, IndexError):
                category = "Other"
        date = datetime.now().strftime("%Y-%m-%d")
        save_expense(date, category, description, amount)
        print(f"Saved: {category} - {description} - {CURRENCY}{amount:,.2f}")

    elif choice == "2":
        print("Categories:")
        for i, cat in enumerate(CATEGORIES):
            print(f"  {i+1}. {cat}")
        try:
            idx = int(input("Category number: ")) - 1
            category = CATEGORIES[idx]
        except (ValueError, IndexError):
            print("Invalid selection.")
            continue
        description = input("Description: ").strip()
        try:
            amount = float(input(f"Amount ({CURRENCY}): "))
        except ValueError:
            print("Invalid amount.")
            continue
        date = datetime.now().strftime("%Y-%m-%d")
        save_expense(date, category, description, amount)
        print(f"Saved: {category} - {description} - {CURRENCY}{amount:,.2f}")

    elif choice == "3":
        expenses = load_expenses()
        if expenses:
            print(f"\n{'Date':<12} {'Category':<15} {'Description':<20} {'Amount':>10}")
            print("-" * 60)
            for exp in expenses:
                print(f"{exp['Date']:<12} {exp['Category']:<15} {exp['Description']:<20} {CURRENCY}{exp['Amount']:>9,.2f}")
        else:
            print("No expenses yet.")

    elif choice == "4":
        show_summary()

    elif choice == "5":
        generate_insights()

    elif choice == "6":
        print("Expenses saved. Goodbye!")
        break
