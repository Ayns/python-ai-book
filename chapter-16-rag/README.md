# Chapter 16: RAG — Teaching AI Your Own Data
Retrieval-Augmented Generation: chunking, embeddings, vector databases, building a complete RAG pipeline.

## Project: Chat with Your Documents
Run: `python doc_chat.py`

## Requirements
```
pip install openai chromadb python-dotenv
```

## Setup
1. Create a `.env` file with your OpenAI API key
2. Prepare a `.txt` file with the document you want to chat with
3. Run the script and provide the file path

## What You'll Learn
- Text chunking with overlap
- ChromaDB for vector storage
- RAG pipeline: retrieve → augment → generate
- Vector database tradeoffs (ChromaDB vs Pinecone vs FAISS)
