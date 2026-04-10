# Architecture and Design Patterns

The Pipeline and Provider patterns found in sophisticated ETL systems are ideal for this architecture. By treating documentation as a "source" and the LLM as a "sink," the system remains modular and scalable.

**The Provider Pattern:** One "Provider" can handle the ingestion of local project files, while another fetches external documentation (e.g., Salesforce API docs or BigQuery manuals).
Use a "Source Provider" to handle different types of documentation (Salesforce REST docs vs. GCP BigQuery manuals) and a "Synthesis Provider" to handle the summarization logic.

**Middleware Synthesis:** A "Middleware" layer can take these raw inputs and synthesize them into a "Context Packet." This ensures that the logic for gathering information is kept separate from the logic for interacting with the model.

**Hexagonal Architecture:** Using "Ports and Adapters" allows you to swap out the underlying model (e.g., switching between different Gemini versions) without rewriting the core synthesis logic. You can treat the Gemini API as an "Adapter." If a better model or local LLM comes out, you just swap the adapter without changing your "Learning Logic."

**Retrieval-Augmented Generation (RAG):** Instead of feeding the whole document, you use a Python script to break the documentation into "chunks," convert them into "embeddings" (mathematical representations of meaning), and store them in a vector database (like ChromaDB or Pinecone). When you ask a question, the script finds only the relevant 2–3 paragraphs and sends only those to Gemini.

**Multi-Agent Orchestration:** Use a "Router" pattern where a primary agent analyzes your query and decides which expert (Salesforce, SQL, or Architecture) should answer.
---

## Knowledge Middleware: CLI vs. Custom Orchestrator

The choice between using a pre-built CLI and architecting your own "Knowledge Middleware" is a key architectural decision.

### The "Knowledge Middleware" Concept
Middleware acts as a layer between the user and the LLM, managing **Context Control** and **Cost Efficiency**.
- **Standard CLI:** A "Direct Pipe" to the API. It has no internal logic to perform local vector searches or rewrite prompts based on project state.
- **Custom Orchestrator:** Extends the CLI with domain-specific knowledge, automated context retrieval, and agentic tool-use (e.g., running `ls` or indexing new files on the fly).

### Implementation Paths

| Path | Pattern | Benefit |
| :--- | :--- | :--- |
| **A: Wrapper** | The "Hack" | Pipe LlamaIndex context chunks into a standard CLI: `tellurion-query "..." | gemini-cli`. |
| **B: Custom** | The "Pro" | Build the interaction logic yourself using LlamaIndex's chat engine for a unique, project-aware tool. |

### The "Hybrid" Compromise
Professional-grade CLIs can be prototyped using LlamaIndex's built-in **Chat REPL**, which provides history and context with minimal code:

```python
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage

# 1. Load your PERSISTED content
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# 2. Create a professional-grade "CLI" session
chat_engine = index.as_chat_engine(chat_mode="context")
chat_engine.chat_repl()
```

---

## The Repository Pattern in AI
In traditional software engineering, a **Repository** hides the complexity of data access (SQL, APIs, etc.) and returns a clean object. In an AI/LLM architecture, this pattern is used to isolate the **Retrieval Layer** from the rest of the application.

*   **The "Retriever" is the Repository:** It encapsulates the complexity of vector math, chunking strategies, and embedding model interactions.
*   **The Contract:** The input to this repository is a **User Question (String)**, and the output is a **List of Text Chunks (Context)**.

### Separation of Concerns

By viewing the system as three distinct services talking through "Contracts" (Prompts), you maintain architectural integrity:

| Layer | Input | Internal Process | Output |
| :--- | :--- | :--- | :--- |
| **I/O (Data Prep)** | Raw Files (PDF, MD) | Chunking → Embedding | Vector Index (Persist) |
| **Repository (Retrieval)** | User Question | Query Embedding → Similarity Search | Text Snippets (Plain Text) |
| **Generation (LLM)** | Question + Snippets | Prompt Engineering → Reasoning | Human Answer |

---

## The Modular Pipeline

A professional AI ecosystem is built as a **Modular Pipeline** rather than a single-provider silo. This allows you to choose the "best-of-breed" tool for each specific layer.

1.  **Retriever Module:** (Embedder + Vector DB) — These must match each other (the "Golden Rule").
2.  **Generator Module:** (The LLM "Brain") — This can be any model that reads text, regardless of who provided the embeddings.

### The "Polyglot" AI Stack

Architects often "mix and match" providers for strategic reasons:
- **Cost Optimization:** Use cheap, open-source embeddings for indexing millions of docs; use a high-end model (e.g., Gemini 1.5 Pro) for the final response.
- **Data Privacy:** Use a local embedding model for the indexing phase (keeping data on your network); send only small, retrieved text snippets to a cloud LLM for the final generation.
- **Specialization:** Use niche models (e.g., Medical/Legal-BERT) for high-accuracy retrieval but use a general-purpose model for summarization.

| Component | Industry Example | Provider |
| :--- | :--- | :--- |
| **Orchestrator** | LlamaIndex / LangChain | Open Source |
| **Embedding Model** | `text-embedding-3-small` | OpenAI |
| **Vector Database** | Pinecone / Chroma | Managed Service / OSS |
| **The "Brain" (LLM)** | `gemini-1.5-pro` | Google |