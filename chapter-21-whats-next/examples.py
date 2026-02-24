# What's Next: Your AI + Python Journey - Chapter 21
# This file contains the code examples from the final chapter.

# ─── Local Models with Ollama ───
# Install: https://ollama.com
# Then: ollama pull llama3
# Then: ollama run llama3

# Use from Python (same pattern as OpenAI!):
from openai import OpenAI

# Ollama's API is OpenAI-compatible — one-line URL change!
client = OpenAI(base_url="http://localhost:11434/v1", api_key="unused")

response = client.chat.completions.create(
    model="llama3",
    messages=[{"role": "user", "content": "Hello! Tell me a fun fact."}]
)
print(response.choices[0].message.content)


# ─── Portfolio Project Ideas ───
# 1. AI-Powered Resume Analyzer
#    - Upload PDF → extract text → AI rates it → gives improvement suggestions
#    - Skills: file handling, AI APIs, prompt engineering
#
# 2. Smart Study Assistant
#    - Upload notes → RAG pipeline → quiz generation → spaced repetition
#    - Skills: RAG, embeddings, ChromaDB, prompt engineering
#
# 3. Automated Report Generator
#    - Read data from CSV → Pandas analysis → AI narrative → PDF report
#    - Skills: Pandas, AI APIs, file handling, automation
#
# 4. Multi-Language Chatbot
#    - Detect language → respond in same language → translate on demand
#    - Skills: AI APIs, prompt engineering, Streamlit
#
# 5. AI Code Reviewer Bot
#    - Paste code → analyze → get feedback with severity ratings
#    - Skills: prompt engineering, JSON output, Streamlit
