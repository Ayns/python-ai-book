# AI + Automation Pipeline - Chapter 17 Project
# Requirements: pip install openai python-dotenv schedule

import os
import json
import csv
import time
import logging
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ─── Configuration ───
LOG_FILE = "automation.log"
RESULTS_FILE = "processed_results.csv"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def classify_text(text):
    """Use AI to classify text into a category"""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Classify the following text into exactly one category: urgent, follow-up, informational, spam. Return ONLY the category word."},
                {"role": "user", "content": text}
            ],
            temperature=0
        )
        category = response.choices[0].message.content.strip().lower()
        logging.info(f"Classified: '{text[:50]}...' -> {category}")
        return category
    except openai.APIError as err:
        logging.error(f"API error: {err}")
        return "error"


def summarize_text(text, max_sentences=2):
    """Use AI to summarize text"""
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": f"Summarize in {max_sentences} sentences. Be concise."},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except openai.APIError as err:
        logging.error(f"API error: {err}")
        return "Error generating summary"


def process_batch(items):
    """Process a batch of text items: classify + summarize each"""
    results = []

    for i, item in enumerate(items):
        print(f"  Processing {i+1}/{len(items)}...")
        category = classify_text(item)
        summary = summarize_text(item)

        result = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "category": category,
            "summary": summary,
            "original_length": len(item)
        }
        results.append(result)

        # Save incrementally (production tip: don't lose progress on failure)
        save_result(result)

        time.sleep(0.5)  # respect rate limits

    return results


def save_result(result):
    """Append a single result to CSV"""
    file_exists = os.path.exists(RESULTS_FILE)
    with open(RESULTS_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "category", "summary", "original_length"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(result)


def watch_folder(folder="inbox"):
    """Watch a folder for new .txt files and process them"""
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created '{folder}/' directory. Drop .txt files there.")
        return

    files = [f for f in os.listdir(folder) if f.endswith(".txt")]
    if not files:
        print(f"No .txt files found in '{folder}/'")
        return

    print(f"Found {len(files)} file(s) to process:")
    items = []
    for filename in files:
        filepath = os.path.join(folder, filename)
        with open(filepath, "r") as f:
            text = f.read()
        items.append(text)
        print(f"  - {filename} ({len(text)} chars)")

    results = process_batch(items)

    print(f"\nResults:")
    for i, result in enumerate(results):
        print(f"  {files[i]}: [{result['category']}] {result['summary'][:60]}...")

    print(f"\nSaved to {RESULTS_FILE}")
    logging.info(f"Batch complete: {len(results)} items processed")


# ─── Main Program ───
print("=" * 40)
print("  AI AUTOMATION PIPELINE")
print("=" * 40)

while True:
    print("\n1. Process batch of text")
    print("2. Watch 'inbox' folder")
    print("3. Classify single text")
    print("4. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        print("Enter texts (one per line, blank line to finish):")
        items = []
        while True:
            line = input()
            if not line:
                break
            items.append(line)
        if items:
            process_batch(items)
            print(f"Results saved to {RESULTS_FILE}")

    elif choice == "2":
        watch_folder()

    elif choice == "3":
        text = input("Text to classify: ")
        category = classify_text(text)
        print(f"Category: {category}")

    elif choice == "4":
        print("Goodbye!")
        break
