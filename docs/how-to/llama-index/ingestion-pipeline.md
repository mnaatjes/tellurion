# Building an Ingestion Pipeline with LlamaIndex

This documentation is designed to help you build an Ingestion Pipeline for your separate project, specifically focusing on how to get your data into a Vector Database that your Agent-Expert can then use via the Gemini-CLI.

## 1. Project Setup

LlamaIndex in 2026 is highly modular. You should install the core library plus the specific integrations for your database (e.g., Chroma) and your embedding model.

```bash
# Core and common integrations
pip install llama-index-core
pip install llama-index-readers-file
pip install llama-index-embeddings-google
pip install llama-index-vector-stores-chroma
```

---

## 2. The Ingestion Pipeline (The "Librarian")

This script represents the "E" and "T" of your ETL. It reads your raw documentation, chunks it, and creates the vector embeddings.

### Step 1: Load Raw Documents
Use the `SimpleDirectoryReader` for local folders. It supports `.md`, `.pdf`, `.txt`, and more.

```python
from llama_index.core import SimpleDirectoryReader

# Load everything in your documentation folder
documents = SimpleDirectoryReader("./my_private_docs").load_data()
```

### Step 2: Intelligent Chunking (Transformation)
To avoid the "Context Window" wall, use a `SentenceSplitter`. This ensures your Agent gets precise snippets rather than whole files.

```python
from llama_index.core.node_parser import SentenceSplitter

# 512 tokens with a 10% overlap is the 2026 standard for high accuracy
parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
nodes = parser.get_nodes_from_documents(documents)
```

### Step 3: Embed and Store (The Vector DB)
Connect to your local database (like ChromaDB) so your embeddings persist on your machine.

```python
import chromadb
from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore

# Initialize ChromaDB client (local storage)
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("agent_knowledge")

# Set up the Storage Context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create the Index (this generates the embeddings)
index = VectorStoreIndex(nodes, storage_context=storage_context)
```

---

## 3. The Query Bridge (For Gemini-CLI)

Once your data is ingested, you need the "Query Script" that your Agent-Expert will call. This script performs the Similarity Search.

```python
# query_agent_db.py
import sys
import chromadb
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.vector_stores.chroma import ChromaVectorStore

def search_knowledge(user_query):
    # Initialize ChromaDB client (local storage)
    db = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = db.get_or_create_collection("agent_knowledge")
    
    # Set up the vector store
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    
    # Load the index
    index = VectorStoreIndex.from_vector_store(vector_store)
    
    # Create a query engine
    query_engine = index.as_query_engine(similarity_top_k=3)
    
    # Execute the search
    response = query_engine.query(user_query)
    
    # Print for Gemini-CLI to capture
    print(f"SOURCE DATA:\n{response}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_knowledge(sys.argv[1])
```

---

## 4. Best Practices for 2026

*   **Persistent Storage:** Always use `PersistentClient` in Chroma or persist your index to disk. Re-embedding 100 documents every time you run the CLI is expensive and slow.
*   **Metadata is King:** When loading documents, use the metadata argument to attach the filename and version. This allows your Agent to say, "According to Version 2.1 of the manual..."
*   **Similarity Thresholds:** In your `query_engine`, set a `similarity_cutoff` (e.g., 0.7). This prevents the Agent from hallucinating based on "weak" matches that aren't actually relevant.

---

## Summary Checklist

*   [ ] **Ingest:** Use `SimpleDirectoryReader` for your raw docs.
*   [ ] **Transform:** Use `SentenceSplitter` for optimal chunking.
*   [ ] **Store:** Use a local `ChromaVectorStore`.
*   [ ] **Retrieve:** Use a Python script as an MCP bridge to connect this logic to your Gemini-CLI skill.
