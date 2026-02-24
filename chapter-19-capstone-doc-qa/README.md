# Chapter 19: Capstone — Intelligent Document Q&A System
Combines: RAG (Ch16), APIs (Ch13), File Handling (Ch6), OOP (Ch7)

## Run
```
python doc_qa_system.py
```

## Requirements
```
pip install openai chromadb python-dotenv
```

## Setup
1. Create a `.env` file with your API key
2. Add `.txt` files to the `documents/` folder
3. Run the script

## Features
- Multi-document support
- Source citations in answers
- Chunking with overlap for accuracy
- Conversation-style Q&A
