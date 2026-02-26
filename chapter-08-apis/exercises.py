# Chapter 8 - Exercise Solutions
import requests

# 1. Multi-city weather comparison
def compare_weather(cities):
    for city in cities:
        url = f"https://wttr.in/{city}?format=%t+%C"
        try:
            r = requests.get(url, timeout=5)
            print(f"  {city}: {r.text.strip()}")
        except requests.RequestException as e:
            print(f"  {city}: Error - {e}")

compare_weather(["London", "Tokyo", "Chennai"])

# 2. API with error handling and retries
import time

def fetch_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"  Attempt {attempt+1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
    return None
