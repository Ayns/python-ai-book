# Chat with Your Documents - Chapter 16 Project
# Requirements: pip install openai chromadb python-dotenv

import os
from dotenv import load_dotenv
from openai import OpenAI
import openai
import chromadb

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks"""
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks


def setup_database(filepath):
    """Load document, chunk it, and store in ChromaDB"""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    print(f"Split into {len(chunks)} chunks.")

    chroma = chromadb.Client()
    collection = chroma.create_collection("documents")

    collection.add(
        documents=chunks,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    print("Indexed in ChromaDB.")
    return collection


def ask_document(collection, question):
    """Search for relevant chunks and ask AI"""
    results = collection.query(query_texts=[question], n_results=3)
    context = "\n\n".join(results["documents"][0])

    prompt = f"""Answer based ONLY on the following context. If the answer
is not in the context, say "I could not find that in the document."

Context:
{context}

Question: {question}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content
    except openai.APIError as err:
        return f"Error: {err}"


# Main program
print("=" * 40)
print("   CHAT WITH YOUR DOCUMENTS")
print("=" * 40)

filepath = input("\nPath to .txt file: ").strip()

try:
    collection = setup_database(filepath)
except FileNotFoundError:
    print(f"File not found: {filepath}")
    exit()

print("\nReady! Ask questions about your document.")
print("Type 'quit' to exit.\n")

while True:
    question = input("You: ").strip()
    if not question:
        continue
    if question.lower() == "quit":
        print("Goodbye!")
        break

    answer = ask_document(collection, question)
    print(f"\nAI: {answer}\n")
