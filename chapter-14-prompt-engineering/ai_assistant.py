# Multi-Purpose AI Assistant - Chapter 14 Project
# Requirements: pip install openai python-dotenv

import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_ai(prompt, temperature=0.7):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Follow instructions precisely."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content
    except openai.APIError as err:
        return f"Error: {err}"


def summarize():
    text = input("Paste text to summarize:\n")
    length = input("Number of sentences (default 3): ").strip() or "3"
    prompt = f"Summarize in {length} sentences. Be clear and concise:\n\n{text}"
    print(f"\nSummary:\n{ask_ai(prompt, temperature=0.3)}")


def translate():
    text = input("Text to translate:\n")
    target = input("Target language: ")
    prompt = f"Translate to {target}. Return only the translation:\n\n{text}"
    print(f"\nTranslation:\n{ask_ai(prompt, temperature=0.3)}")


def extract_data():
    text = input("Paste text to extract data from:\n")
    prompt = f"""Extract all people, organizations, and locations from this text.
Return ONLY valid JSON: {{"people": [], "organizations": [], "locations": []}}
Text: {text}"""
    result = ask_ai(prompt, temperature=0)
    try:
        data = json.loads(result)
        print("\nExtracted data:")
        for key, values in data.items():
            print(f"  {key}: {', '.join(values)}")
    except json.JSONDecodeError:
        print(f"\nRaw response:\n{result}")


def code_review():
    code_text = input("Paste code to review:\n")
    prompt = f"""Review this code. For each issue:
1. What the problem is
2. Why it matters
3. How to fix it
Keep feedback constructive.\nCode:\n{code_text}"""
    print(f"\nReview:\n{ask_ai(prompt, temperature=0.3)}")


print("=" * 40)
print("   AI ASSISTANT")
print("=" * 40)
while True:
    print("\n1. Summarize  2. Translate  3. Extract Data  4. Code Review  5. Exit")
    choice = input("Choice: ")
    if choice == "1": summarize()
    elif choice == "2": translate()
    elif choice == "3": extract_data()
    elif choice == "4": code_review()
    elif choice == "5":
        print("Goodbye!")
        break
