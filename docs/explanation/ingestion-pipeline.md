# Ingestion Pipeline: Internal vs. Custom Vector DBs

This document outlines the differences between using the built-in Gemini-CLI managed ingestion and integrating a custom, external Vector Database.

## Custom Vector DB Integration (Separate Project)

If you are building your own Vector DB, you generally bypass the internal `config.json` ingestion properties. Instead, you "attach" your database to a skill as a **Tool** or via the **Model Context Protocol (MCP)**.

### The Workflow
1.  **Your ETL:** Custom extraction, transformation, and loading logic.
2.  **Your Vector DB:** Your choice of storage (Chroma, Pinecone, SQLite, etc.).
3.  **MCP/Tool Bridge:** A script or server that exposes your DB to the CLI.
4.  **Gemini-CLI:** Invokes the tool when relevant.
5.  **Expert Response:** Grounded in your custom data.

### Implementation Strategy
Instead of defining `chunkSize` or `overlap`, you define a `tools` or `mcpServers` entry in your skill configuration. This instructs the Expert: *"Whenever you need to know about [X Topic], don't look in your internal index; call this external script/database instead."*

---

## Key Distinctions

| Feature | CLI-Managed Ingestion | Your Custom Vector DB |
| :--- | :--- | :--- |
| **Logic** | Fixed (Recursive Character Splitting) | Custom (Semantic, Markdown-aware, etc.) |
| **Storage** | Hidden `.gemini` cache | Your choice (Chroma, Pinecone, SQLite) |
| **Control** | Limited to `overlap` / `chunkSize` | Full control over metadata and filtering |
| **Scale** | Best for small-to-medium docs | Best for massive or complex datasets |

---

## Connecting Your Custom Pipeline to Gemini-CLI

To use your own ingestion pipeline and vector database with a Gemini-CLI Agent Expert, you must define your database as an **External Tool** that the Agent can "call" whenever it needs specific information.

### Method 1: The MCP Bridge (The Modern Way)
The Model Context Protocol (MCP) is the native way Gemini-CLI connects to external databases. You create a small "wrapper" script that knows how to query your Vector DB.

1.  **Create a Query Script:** (e.g., `query_my_vectordb.py`) that takes a text query, searches your vector DB, and returns the Top-N results.
2.  **Configure the Skill:** In `.gemini/skills/<skill_name>/config.json`, add an `mcpServers` entry:

```json
{
  "name": "Documentation Expert",
  "mcpServers": {
    "my_docs_tool": {
      "command": "python",
      "args": ["/path/to/your/query_my_vectordb.py"],
      "env": {
        "DB_PATH": "/path/to/your/vector_store"
      }
    }
  }
}
```

### Method 2: Custom Slash Commands (The Direct Way)
Define a Slash Command within your skill directory to create a manual "pipe" between your database and the agent.

1.  **Create a Tool Definition:** At `.gemini/skills/<skill_name>/tools.toml`.
2.  **Define the Command:**

```toml
[commands.search_docs]
description = "Search the local vector database for relevant documentation"
parameters = ["query"]
command = "python /path/to/your/query_script.py {{query}}"
```

The Agent will see `search_docs` as an available skill and use it to gather context when needed.

### Why this is better for your workflow
*   **Custom Logic:** Use advanced "Hybrid Search" (keyword + vector).
*   **Metadata Filtering:** Filter by version, category, or date before handing data to Gemini.
*   **Decoupling:** Update your database via your pipeline at any time without re-triggering a "Gemini Ingest" command.

---

## Designing the "Librarian" (Query Script)

The Python script acts as the "Middleman" between Gemini-CLI and your Vector Database.

### The Librarian's Duties
| Step | Action | Description |
| :--- | :--- | :--- |
| **1. Input** | **Request Handling** | Capture the raw text string from the CLI (e.g., `sys.argv`). |
| **2. Transform** | **Query Embedding** | Pass the query through the same embedding model used during ingestion. |
| **3. Search** | **Similarity Search** | Perform a "Nearest Neighbor" or "Cosine Similarity" search for the Top-N results. |
| **4. Output** | **Context Formatting** | Package text chunks and metadata into a clean string for the LLM. |

### Input (Arguments)
The CLI passes the user's natural language query to your script.
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("query", help="The search string from Gemini-CLI")
parser.add_argument("--limit", type=int, default=3)
args = parser.parse_args()
```

### Output (Return Values)
Print results to `stdout`. Use a structured format for easy parsing:
```text
[SOURCE: api_docs.md | RELEVANCE: 0.92]
To reset the admin password, navigate to /settings...
---
[SOURCE: troubleshooting.txt | RELEVANCE: 0.85]
...
```

**MCP-style Return (JSON):**
```json
{
  "llmContent": "Snippet 1: ... Snippet 2: ...",
  "returnDisplay": "Found 2 relevant matches in your local Vector DB."
}
```

### Summary Checklist for `query_script.py`
*   [ ] **Input:** Capture `{{args}}` from the CLI.
*   [ ] **Processing:** Use your embedding model to vectorize the input.
*   [ ] **Output:** Print text results to `stdout`.
*   [ ] **Context Padding:** Include filenames or confidence scores for prioritization.

---

## Database & Library Recommendations

### Top Recommendations for Local CLI Agents
| Database | Type | Best For | Key Strength |
| :--- | :--- | :--- | :--- |
| **ChromaDB** | Embedded / OSS | Prototyping & Small Docs | Best dev experience; Python-native. |
| **SQLite-vss** | SQL Extension | Local-First Devs | Single-file simplicity; standard SQL. |
| **Milvus Lite** | Library / OSS | Growth & Scalability | Lightweight start; scales to billions later. |
| **Qdrant** | OSS / Managed | High-Speed Filtering | Rust-based; excellent metadata filtering. |

### RAG Frameworks & Chunking Libraries
*   **LlamaIndex:** The "Data Framework" for LLMs. Best for deep ingestion pipelines and structured data.
*   **LangChain:** A modular "Swiss Army Knife" for chaining tools together.
*   **Unstructured:** The industry standard for cleaning and parsing messy PDFs/HTML.
*   **Chonkie:** A lightweight, fast library focused specifically on intelligent text splitting.

---

## GitHub Templates & Blueprints

*   **`run-llama/llama_index` (CLI Package):** Blueprint for standalone RAG CLI logic.
*   **`AhsanAyaz/gemini-rag-llamaindex-example`:** Focused template for Google Gemini integration.
*   **`abhinit21/building-agentic-rag-with-llamaindex`:** Autonomous agent reasoning examples.
*   **`mrdbourke/simple-local-rag`:** Raw Python logic for "from scratch" learning.
*   **`run-llama/llamacloud-mcp`:** Official bridge code for MCP communication.
