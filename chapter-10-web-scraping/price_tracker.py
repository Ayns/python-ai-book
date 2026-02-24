# Price Tracker - Chapter 10 Project
# Note: This is a teaching example. Always respect robots.txt
# and rate limits when scraping websites.

import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime
import time

FILE = "price_history.csv"


def scrape_page(url):
    """Fetch and parse a web page"""
    headers = {"User-Agent": "Mozilla/5.0 (Learning Project)"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as err:
        print(f"Error fetching page: {err}")
        return None


def save_price(product, price, url):
    """Save price data to CSV"""
    file_exists = os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Product", "Price", "URL"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), product, price, url])
    print(f"Saved: {product} - ${price}")


def view_history():
    """Display price history"""
    if not os.path.exists(FILE):
        print("No price history yet.")
        return

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No price history yet.")
        return

    print(f"\n{'Date':<20} {'Product':<25} {'Price':>10}")
    print("-" * 58)
    for row in rows:
        print(f"{row['Date']:<20} {row['Product']:<25} ${float(row['Price']):>9,.2f}")


# Main program
print("=" * 40)
print("  PRICE TRACKER")
print("=" * 40)
print("Note: Requires beautifulsoup4")
print("  pip install beautifulsoup4 requests")

while True:
    print("\n1. Track a Price (manual entry)")
    print("2. View Price History")
    print("3. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        product = input("Product name: ").strip()
        try:
            price = float(input("Current price: $"))
        except ValueError:
            print("Invalid price.")
            continue
        url = input("Product URL (optional): ").strip() or "manual entry"
        save_price(product, price, url)

    elif choice == "2":
        view_history()

    elif choice == "3":
        print("Goodbye!")
        break
