# How-To: Assigning and Managing Vector Embeddings

Vector embeddings allow your Expert Agents to handle massive documentation sets (like a 500-page BigQuery manual) without overwhelming the context window. By pre-processing text into numerical vectors, the Gemini CLI can perform "Similarity Searches" to retrieve only the most relevant chunks for any given query.

---

## 1. Global Configuration: The Embedding Engine

The global configuration defines the "mathematical language" used by all skills. This ensures consistency across your workspace and allows multiple experts to potentially reference the same vector space.

- **File Location:** `~/.gemini/settings.json`
- **Key Property:** `embeddingModel`
- **Default:** `models/text-embedding-004` (Google's latest high-performance embedding model).

### Why it's Global
Setting the model at the user level ensures that if you have a "BigQuery Architect" and a "Data Modeler" both looking at the same documentation, they generate and interpret vectors identically.

---

## 2. Skill-Specific Configuration: Ingestion Strategy

While the engine is global, the **Ingestion Strategy** is defined at the skill level. This allows you to tune how data is "digested" based on the content type (e.g., code-heavy SQL docs vs. narrative tutorials).

- **File Location:** `./.gemini/skills/<name>/config.json`

### Key Properties
- **`vectorDimensions`**: Defines the size of the vector array (e.g., `768` or `1536`). This must match the output dimensions of your selected `embeddingModel`.
- **`chunkConfig`**: Explicitly defines how documents are sliced.
  - **`chunkSize`**: For code-heavy documentation, a larger chunk size (e.g., `800` to `1000` tokens) is recommended to keep SQL blocks and function definitions intact.
  - **`overlap`**: The number of tokens shared between adjacent chunks (typically `10-20%`) to ensure context isn't lost at the "seams" of a cut.
- **`searchMetric`**: The distance metric used for retrieval, usually set to `cosine` (Cosine Similarity).

---

## 3. Physical Storage and Local Caching

To avoid the "Token Tax" of re-embedding the same files repeatedly, the Gemini CLI maintains a local cache on your machine.

- **Directory:** `.gemini/cache/embeddings/`
- **Mechanism:** When you run the `/ingest` command, the CLI creates a local SQLite or Flat-File database here.
- **Metadata:** This cache stores the mapping between **Vector IDs** and the **Original File Paths** (e.g., `docs/reference/bigquery_manual.md`).
- **Scope:** This is a persistent local cache. It survives terminal restarts and system reboots, ensuring rapid retrieval in future sessions.

---

## 4. The Retrieval "Handshake" Workflow

When you interact with an expert agent, the Gemini CLI performs these steps in order to provide contextually aware answers:

1.  **Read Config:** Checks the skill's `config.json` for specific chunking and dimension rules.
2.  **Verify Cache:** Looks in `.gemini/cache/embeddings/` to see if the required documentation has already been processed.
3.  **Embed Query:** Uses the global model defined in `settings.json` to turn your current question into a numerical vector.
4.  **Retrieve:** Performs a "Similarity Search" against the local cache.
5.  **Inject:** Pulls the top matching chunks into **Layer 2 (The Working Set)** of your context window, allowing the LLM to "see" the relevant documentation before answering.

---

## Summary Reference

| Property | Configuration File | CLI Command to View/Set |
| :--- | :--- | :--- |
| **Model ID** | `~/.gemini/settings.json` | `/settings embedding_model` |
| **Chunk Size** | `.gemini/skills/<name>/config.json` | `gemini skill edit <name>` |
| **Overlap** | `.gemini/skills/<name>/config.json` | `gemini skill edit <name>` |
| **Local Cache** | `.gemini/cache/embeddings/` | `/ingest status` |
