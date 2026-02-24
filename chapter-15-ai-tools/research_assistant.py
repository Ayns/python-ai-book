# AI Research Assistant - Chapter 15 Project
# Requirements: pip install openai python-dotenv

import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import openai

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_ai(prompt, system="You are a research assistant.", temperature=0.3):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content
    except openai.APIError as err:
        return f"Error: {err}"


def analyze_text(text):
    """Analyze text and return structured data"""
    prompt = f"""Analyze this text and return ONLY valid JSON:
{{"summary": "2-sentence summary",
  "key_points": ["point 1", "point 2"],
  "sentiment": "positive/negative/neutral",
  "topics": ["topic1", "topic2"]}}

Text: {text}"""
    result = ask_ai(prompt, temperature=0)
    try:
        data = json.loads(result)
        print(f"\nSummary: {data['summary']}")
        print(f"Sentiment: {data['sentiment']}")
        print(f"Topics: {', '.join(data['topics'])}")
        for point in data.get("key_points", []):
            print(f"  - {point}")
    except json.JSONDecodeError:
        print(f"\nRaw response:\n{result}")


def compare_texts(text1, text2):
    """Compare two texts"""
    prompt = f"""Compare these two texts. Identify similarities, differences,
and which is stronger. Keep response under 200 words.

Text 1: {text1}

Text 2: {text2}"""
    print(f"\nComparison:\n{ask_ai(prompt, temperature=0.3)}")


def generate_report(topic):
    """Generate a research report"""
    prompt = f"""Write a concise research brief about: {topic}

Include:
- Summary (2-3 sentences)
- 3-5 key facts
- Current trends
- One surprising finding

Keep it under 300 words. Be specific and data-driven."""
    print(f"\nReport:\n{ask_ai(prompt, temperature=0.5)}")


# Main program
print("=" * 40)
print("   AI RESEARCH ASSISTANT")
print("=" * 40)

while True:
    print("\n1. Analyze  2. Compare  3. Report  4. Exit")
    choice = input("Choice: ")

    if choice == "1":
        text = input("Paste text:\n")
        analyze_text(text)
    elif choice == "2":
        text1 = input("First text:\n")
        text2 = input("Second text:\n")
        compare_texts(text1, text2)
    elif choice == "3":
        topic = input("Research topic: ")
        generate_report(topic)
    elif choice == "4":
        print("Goodbye!")
        break
