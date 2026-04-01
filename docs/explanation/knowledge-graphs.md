# Knowledge Graphs & GraphRAG

While Vector RAG focuses on **"What is similar?"**, a Knowledge Graph focuses on **"How is this related?"**.

If Vector RAG is a high-speed library search for similar book covers, a Knowledge Graph is the detailed index at the back of the book that tells you exactly which characters met in which chapters.

---

## 1. Vector RAG vs. Knowledge Graphs

### Vector RAG: The Map of Meaning
Vector RAG uses mathematical similarity by turning text into coordinates.
*   **The Logic:** "This paragraph about engines is near this paragraph about pistons because they share a semantic space."
*   **The Weakness:** It sees data in isolated "chunks" and struggles with **multi-hop** questions.
    *   *Example:* "Who is the CEO of the company that supplied the parts for the XJ-900 engine?" Vector RAG might find engine docs and CEO docs, but it doesn't "know" there is a direct physical link between them.

### Knowledge Graph: The Web of Relationships
A Knowledge Graph (KG) stores data as **Nodes** (entities) and **Edges** (relationships) in a triple format: `Subject -> Predicate -> Object`.
*   **The Logic:** `Company A -> SUPPLIES -> Part B`, `Part B -> COMPONENT_OF -> XJ-900`.
*   **The Strength:** It traverses these links factually. It doesn't guess based on similarity; it follows a path.
*   **The Weakness:** It is "brittle." If a relationship isn't explicitly defined in the ETL pipeline, the graph doesn't know it exists.

### Key Technical Differences
| Feature | Vector RAG | Knowledge Graph (GraphRAG) |
| :--- | :--- | :--- |
| **Data Format** | Unstructured (Text Chunks) | Structured (Entities & Relations) |
| **Search Method** | Similarity Search (Cosine) | Graph Traversal (Cypher/SPARQL) |
| **Reasoning** | "This looks like that." | "A is connected to B through C." |
| **Multi-hop** | Poor (Gets "lost" after 1-2 hops) | Excellent (Can follow long chains) |
| **Setup Cost** | Low (Automatic Embedding) | High (Requires Entity Extraction) |

---

## 2. GraphRAG: The Hybrid Approach

GraphRAG combines the two worlds to provide both local context and global awareness.
*   **Summarization:** Uses an LLM to read docs and automatically extract "Entities" and relationships.
*   **Global Search:** Answers high-level questions like "What are the three biggest themes in these 500 documents?" by querying automated community summaries.

### Automated "Bottom-Up" Pipeline
Modern GraphRAG automates construction in the "Transform" stage of ETL:
1.  **Extraction:** LLM identifies Entities (People, Places, Concepts) and Triples (Subject → Relation → Object).
2.  **Resolution:** Deduplicates entities (e.g., merging "Kalamazoo" and "K-Zoo") using semantic models.
3.  **Community Detection:** Algorithms (Leiden/Louvain) group related nodes into thematic clusters automatically.
4.  **Summarization:** LLM writes summaries for each cluster, providing the Agent with "Global Awareness."

---

## 3. Connecting Knowledge Graphs to Gemini-CLI

### The Communication Bridge: MCP
The **Model Context Protocol (MCP)** is the primary way to connect a KG to Gemini-CLI.
*   **Existing Tools:** Use official Neo4j MCP servers to allow Gemini to query the graph as "Long-term Memory."
*   **Custom Tools:** Register your Python "Librarian" script as an MCP server or a tool in `config.json`.

### Configuration (`config.json`)
```json
{
  "name": "Knowledge Architect",
  "mcpServers": {
    "my_graph_store": {
      "command": "python",
      "args": ["path/to/graph_query_tool.py"],
      "env": {
        "GRAPH_DB_URL": "bolt://localhost:7687"
      }
    }
  }
}
```

### Teaching the Agent Strategy
In the skill's `prompt.md` or `instructions` field, explicitly define when to use the graph:
> "Use Vector Search for simple 'What is X?' questions. Use the Knowledge Graph for complex questions involving relationships (e.g., 'Who is connected to Project Hermes?'). If a vector search returns a specific entity, use the Graph Tool to explore its neighbors."

---

## 4. Designing the Graph Query Script (`graph_tool.py`)

The script must act as a **Deterministic Searcher** or a **Cypher Executor**.

### Input Styles
*   **Natural Language:** The Agent passes a string; the script translates it into a graph query using a small local model.
*   **Entity/Node:** The Agent identifies a specific node and asks for its neighbors (e.g., `entity: "Hermes"`, `relation: "OWNED_BY"`).

### Efficient Output Formats
*   **Triple Format:** `(User) - [ADOPTED] -> (Hermes)`. This allows the Agent to reconstruct logic perfectly.
*   **Schema Flag:** Implement a `--schema` flag so the Agent can learn available Node and Relationship types before querying.

---

## 5. Data Sourcing: The Same Source, Different Lens

Knowledge Graphs are often generated from the same raw content (.md, .pdf) as Vector RAG.
*   **Vector Branch:** Chunking + Embedding → Vectors (Mathematical "vibe").
*   **Graph Branch:** Entity & Relation Extraction → Nodes & Edges (Logical "facts").

### Recommended Tools
*   **Microsoft GraphRAG:** Robust automated pipeline from raw text to hierarchical graphs.
*   **LlamaIndex PropertyGraphIndex:** Simultaneously creates vectors and extracts entities, ensuring the Agent has both the "vibe" and the "facts" from the same files.
*   **Neo4j / FalkorDB:** Databases for storing and querying the resulting graph structure.

---

## 6. LlamaIndex: The Unified Property Graph Index

LlamaIndex has become the industry standard for advanced RAG due to its unified approach, often referred to as a **Property Graph Index**.

Instead of managing two separate databases and two separate pipelines, you can build a single "hybrid" index where every piece of data is both a Vector (for similarity) and a Node (for relationships).

### How LlamaIndex Unifies the Two
When you run a LlamaIndex ingestion pipeline, you can configure a "Property Graph" that performs both actions simultaneously:
*   **The Vector Part:** Chunks text and creates embeddings (e.g., `models/embedding-001`), stored in a vector store like ChromaDB.
*   **The Graph Part:** Uses an LLM to extract entities and relationships, stored in a graph store like Neo4j or a local FalkorDB.

### The "Property Graph Index" Workflow
In a Python ETL script, the code to build a hybrid index looks like this:

```python
from llama_index.core import PropertyGraphIndex
from llama_index.embeddings.google import GooglePaLMEmbedding
from llama_index.llms.google import Gemini
from llama_index.core.indices.property_graph import ImplicitPathExtractor, SimpleLLMPathExtractor

# Build the Index
index = PropertyGraphIndex.from_documents(
    documents,
    embed_model=GooglePaLMEmbedding(),
    llm=Gemini(model="models/gemini-1.5-flash"),
    kg_extractors=[
        ImplicitPathExtractor(), # Finds folder/file structure links
        SimpleLLMPathExtractor() # Uses LLM to find entities/relations
    ]
)
```

### Why this is "Expert Level" for Your CLI Agent
By using LlamaIndex to manage both, your Agent-Expert gets a specialized query engine called a **Router** or **Sub-Question Query Engine**.

When you ask your Gemini-CLI a question:
1.  **The Router:** Evaluates the question intent.
2.  **Vector Store:** Pulls for semantic/descriptive questions (e.g., "What did the vet say about Hermes?").
3.  **Knowledge Graph:** Pulls for relationship/stakeholder questions (e.g., "Who are all the stakeholders in Project Hermes?").
4.  **The Result:** The Agent combines both into a single, highly accurate response.

### Hardware/Lab Considerations
*   **Storage:** A hybrid index with thousands of relationships can take several gigabytes.
*   **Processing:** Graph extraction is "expensive" in terms of API credits, but the final index lives entirely on your local NVMe drive.

**Next Steps:** Install `llama-index-indices-managed-llama-cloud` or `llama-index-graph-stores-neo4j`.
