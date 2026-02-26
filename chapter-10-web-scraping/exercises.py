# Chapter 10 - Exercise Solutions
import requests
from bs4 import BeautifulSoup
import time

# 1. Scrape quotes with pagination
def scrape_all_quotes():
    all_quotes = []
    page = 1
    while True:
        url = f"https://quotes.toscrape.com/page/{page}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("span", class_="text")
        if not quotes:
            break
        for q in quotes:
            all_quotes.append(q.get_text())
        page += 1
        time.sleep(1)  # Be polite
    return all_quotes

# 2. Extract structured data
def scrape_with_authors():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    results = []
    for div in soup.find_all("div", class_="quote"):
        text = div.find("span", class_="text").get_text()
        author = div.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in div.find_all("a", class_="tag")]
        results.append({"quote": text, "author": author, "tags": tags})
    
    return results

data = scrape_with_authors()
for item in data[:3]:
    print(f"  {item['author']}: {item['quote'][:50]}...")
