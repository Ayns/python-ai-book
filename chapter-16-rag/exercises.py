# Chapter 16 - Exercise Solutions
# See doc_chat.py for the main RAG project

# 1. Different chunk sizes experiment
def experiment_chunk_sizes(text, query):
    """Test different chunk sizes and compare results."""
    sizes = [200, 500, 1000]
    for size in sizes:
        chunks = [text[i:i+size] for i in range(0, len(text), size)]
        print(f"\nChunk size {size}: {len(chunks)} chunks")
        # In a real implementation, you'd embed and search each set

# 2. Multi-file indexer
import os
def index_folder(folder_path):
    """Index all .txt files in a folder."""
    all_chunks = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r") as f:
                text = f.read()
            chunks = [text[i:i+500] for i in range(0, len(text), 500)]
            for chunk in chunks:
                all_chunks.append({"text": chunk, "source": filename})
    print(f"Indexed {len(all_chunks)} chunks from {folder_path}")
    return all_chunks
