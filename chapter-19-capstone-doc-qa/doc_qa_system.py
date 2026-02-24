# Intelligent Document Q&A System - Chapter 19 Capstone
# Requirements: pip install openai chromadb python-dotenv

import os
import glob
from dotenv import load_dotenv
from openai import OpenAI
import openai
import chromadb

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ─── Configuration ───
DOCS_FOLDER = "documents"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Split text into overlapping chunks"""
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks


def load_documents(folder):
    """Load all .txt files from a folder"""
    documents = []
    txt_files = glob.glob(os.path.join(folder, "*.txt"))

    if not txt_files:
        print(f"No .txt files found in '{folder}/'")
        return documents

    for filepath in txt_files:
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        chunks = chunk_text(text)
        for i, chunk in enumerate(chunks):
            documents.append({
                "text": chunk,
                "source": filename,
                "chunk_id": f"{filename}_chunk_{i}"
            })
        print(f"  Loaded: {filename} ({len(chunks)} chunks)")

    return documents


def build_index(documents):
    """Index documents in ChromaDB"""
    chroma = chromadb.Client()

    # Delete existing collection if it exists
    try:
        chroma.delete_collection("doc_qa")
    except:
        pass

    collection = chroma.create_collection("doc_qa")

    texts = [doc["text"] for doc in documents]
    ids = [doc["chunk_id"] for doc in documents]
    metadatas = [{"source": doc["source"]} for doc in documents]

    collection.add(documents=texts, ids=ids, metadatas=metadatas)
    print(f"Indexed {len(documents)} chunks.")
    return collection


def ask_question(collection, question, n_results=3):
    """Search for relevant chunks and generate an answer"""
    results = collection.query(query_texts=[question], n_results=n_results)

    if not results["documents"][0]:
        return "No relevant information found.", []

    # Build context with source tracking
    context_parts = []
    sources = set()
    for i, doc in enumerate(results["documents"][0]):
        source = results["metadatas"][0][i]["source"]
        context_parts.append(f"[From {source}]:\n{doc}")
        sources.add(source)

    context = "\n\n".join(context_parts)

    prompt = f"""Answer the question based ONLY on the context provided below.
If the answer is not in the context, say "I could not find that in the documents."
Cite which document(s) the answer comes from.

Context:
{context}

Question: {question}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a document analyst. Answer questions accurately based only on provided context. Always cite your sources."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        answer = response.choices[0].message.content
        return answer, list(sources)
    except openai.APIError as err:
        return f"Error: {err}", []


# ─── Main Program ───
print("=" * 40)
print("  DOCUMENT Q&A SYSTEM")
print("=" * 40)

# Setup documents folder
if not os.path.exists(DOCS_FOLDER):
    os.makedirs(DOCS_FOLDER)
    print(f"\nCreated '{DOCS_FOLDER}/' folder.")
    print("Add .txt files there and restart.")
    exit()

# Load and index documents
print(f"\nLoading documents from '{DOCS_FOLDER}/'...")
documents = load_documents(DOCS_FOLDER)

if not documents:
    print(f"Add .txt files to '{DOCS_FOLDER}/' and restart.")
    exit()

collection = build_index(documents)

# Chat loop
print("\nReady! Ask questions about your documents.")
print("Type 'quit' to exit.\n")

conversation = []

while True:
    question = input("You: ").strip()

    if not question:
        continue
    if question.lower() == "quit":
        print("Goodbye!")
        break

    answer, sources = ask_question(collection, question)

    print(f"\nAI: {answer}")
    if sources:
        print(f"Sources: {', '.join(sources)}")
    print()

    conversation.append({"question": question, "answer": answer})
