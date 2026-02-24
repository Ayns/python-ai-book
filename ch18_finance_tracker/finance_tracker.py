# AI-Powered Finance Tracker - Chapter 18
# See book for full code and walkthrough
# This is the complete runnable version

import os
import json
import csv
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

FILE = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Shopping", "Bills",
              "Entertainment", "Health", "Education", "Other"]


def ask_ai(prompt, temperature=0):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a financial assistant. Be precise and practical."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content
    except openai.APIError as err:
        return f"Error: {err}"


def auto_categorize(description, amount):
    prompt = f"""Categorize this expense into exactly one category.
Return ONLY valid JSON: {{"category": "", "confidence": "high/medium/low"}}

Categories: {', '.join(CATEGORIES)}

Expense: "{description}" - ${amount:.2f}"""
    result = ask_ai(prompt)
    try:
        data = json.loads(result)
        if data["category"] in CATEGORIES:
            return data["category"], data.get("confidence", "medium")
    except (json.JSONDecodeError, KeyError):
        pass
    return "Other", "low"


def add_expense():
    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return
    try:
        amount = float(input("Amount ($): "))
    except ValueError:
        print("Invalid amount.")
        return

    category, confidence = auto_categorize(description, amount)
    print(f"  AI categorized as: {category} (confidence: {confidence})")

    confirm = input(f"  Accept? (Enter=yes, or type new category): ").strip()
    if confirm:
        if confirm.title() in CATEGORIES:
            category = confirm.title()
        else:
            print(f"  Unknown category. Keeping: {category}")

    date = datetime.now().strftime("%Y-%m-%d")
    file_exists = os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])
        writer.writerow([date, category, description, f"{amount:.2f}"])
    print(f"  Saved: {category} - {description} - ${amount:.2f}")


def load_expenses():
    if not os.path.exists(FILE):
        return pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])
    df = pd.read_csv(FILE)
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df.dropna()


def view_expenses():
    df = load_expenses()
    if df.empty:
        print("No expenses yet.")
        return
    print(f"\n{'Date':<12} {'Category':<14} {'Description':<22} {'Amount':>8}")
    print("-" * 58)
    for _, row in df.iterrows():
        print(f"{str(row['Date'].date()):<12} {row['Category']:<14} "
              f"{row['Description']:<22} ${row['Amount']:>7,.2f}")
    print("-" * 58)
    print(f"{'TOTAL':<48} ${df['Amount'].sum():>7,.2f}")


def ai_analysis():
    df = load_expenses()
    if df.empty:
        print("No expenses to analyze.")
        return
    summary = df.groupby("Category")["Amount"].agg(["sum", "count"])
    summary_text = summary.to_string()
    total = df["Amount"].sum()

    prompt = f"""Analyze these spending patterns and provide practical insights.

Spending summary:\n{summary_text}
Total spent: ${total:.2f}
Number of transactions: {len(df)}

Provide:
1. Top spending category observation
2. One specific saving tip
3. One spending pattern you notice

Keep it under 150 words. Be specific to THIS data, not generic advice."""
    print(f"\n--- AI Spending Analysis ---\n{ask_ai(prompt, temperature=0.3)}")


# Main program
print("=" * 40)
print("   AI FINANCE TRACKER")
print("=" * 40)

while True:
    print("\n1. Add Expense (AI auto-categorize)")
    print("2. View All Expenses")
    print("3. AI Spending Analysis")
    print("4. Exit")
    choice = input("\nChoice: ")

    if choice == "1": add_expense()
    elif choice == "2": view_expenses()
    elif choice == "3": ai_analysis()
    elif choice == "4":
        print("\nExpenses saved. Goodbye!")
        break
