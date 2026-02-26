# Chapter 14 - Exercise Solutions
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Few-shot sentiment classifier
def classify_sentiment(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": """Classify text sentiment as positive, negative, or neutral.

Examples:
"This product is amazing!" → positive
"Worst experience ever." → negative
"The meeting is at 3pm." → neutral

Respond with ONLY the classification."""},
            {"role": "user", "content": text}
        ],
        max_tokens=10
    )
    return response.choices[0].message.content.strip()

# 2. Chain-of-thought math solver
def solve_math(problem):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Solve math problems step by step. Show your work clearly, then give the final answer on the last line as 'Answer: X'"},
            {"role": "user", "content": problem}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content

# 3. JSON output enforcer
def extract_info(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": 'Extract name, age, and city from text. Return ONLY valid JSON: {"name": "...", "age": ..., "city": "..."}'},
            {"role": "user", "content": text}
        ],
        max_tokens=100
    )
    import json
    return json.loads(response.choices[0].message.content)

# Uncomment to test:
# print(classify_sentiment("I love this book!"))
# print(solve_math("If a train travels 120km in 2 hours, what is its speed?"))
# print(extract_info("My name is Ayyanar, I'm 30 and I live in Chennai."))
