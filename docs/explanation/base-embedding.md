# Understanding BaseEmbedding in LlamaIndex (v0.10+)

In the LlamaIndex framework (v0.10+), the `embed_model` is the core component responsible for transforming human-readable text into numerical vectors (embeddings). This document outlines the formal hierarchy, practical implementation, and 2026-era recommendations for Google/Gemini integrations.

## 1. Formal Types and Hierarchy

The `embed_model` type depends on whether you are interacting with the formal class hierarchy or the flexible inputs accepted by global settings.

### BaseEmbedding (The Formal Type)
At its core, `embed_model` is an instance of the `BaseEmbedding` class.
- **Namespace:** `llama_index.core.base.embeddings.base.BaseEmbedding`
- **Purpose:** An Abstract Base Class (ABC) that acts as a standard interface. Any model (Google, OpenAI, HuggingFace) must inherit from this class to support methods like `.get_text_embedding()` or `.get_query_embedding()`.

### GoogleGenAIEmbedding (The Concrete Type)
For the Google stack, the concrete implementation is `GoogleGenAIEmbedding`.
```python
from llama_index.embeddings.google import GoogleGenAIEmbedding

# Inherits from BaseEmbedding
embed_model = GoogleGenAIEmbedding(model_name="models/gemini-embedding-2-preview")
```

### EmbedType (The "Setter" Type)
When assigning values to `Settings.embed_model`, LlamaIndex uses the `EmbedType` alias:
- **Type:** `Union[BaseEmbedding, str]`
- **Logic:** If a string "slug" is passed (e.g., `"local"`), LlamaIndex resolves it automatically via `resolve_embed_model`. For Google models, it is best practice to pass the object itself to ensure API keys and parameters are correctly configured.

---

## 2. Representations: Practical vs. Abstract

### The Practical "Translator"
In code, the model represents the software engine.
- **The Contract:** By passing `embed_model`, you instruct LlamaIndex to use a specific engine whenever it encounters text.
- **The Requirement:** Without it, "Semantic Search" is impossible; the system cannot categorize or find documents based on meaning.

### The Abstract "Semantic Map"
Mathematically, the model projects language into a geometric coordinate system.
- **Dimensionality Reduction:** Compresses infinite language combinations into a fixed-width vector (e.g., 768 or 3,072 numbers).
- **Geometric Proximity:** The distance between points represents semantic similarity. "Dog" will be physically closer to "Puppy" than to "Space Station" in this vector space.

---

## 3. 2026 Google/Gemini Recommendations

For the most advanced performance in early 2026, **Gemini Embedding 2** is the recommended choice.

| Context | Recommended Model ID | Why? |
| :--- | :--- | :--- |
| **Advanced/Multimodal** | `models/gemini-embedding-2-preview` | Best for 2026; natively handles text, images, and PDFs. |
| **Standard Text** | `models/text-embedding-005` | High-performance, stable, and cost-effective. |
| **Legacy/Lightweight** | `models/text-embedding-004` | Faster, but lower "semantic resolution." |

**Note on Defaults:** LlamaIndex defaults to OpenAI models. If `Settings.embed_model` is not explicitly defined and an OpenAI API key is missing, the system will fail during the indexing phase.

---

## 4. Critical Rules for ETL Pipelines

### The "Golden Rule" of RAG Architecture
While you can mix different providers for the Embedding and the LLM (e.g., OpenAI embedder with a Google LLM), you **must** use the exact same embedding model for both indexing and querying.

*   **Indexing:** Turning your documents into vectors to store in the database.
*   **Querying:** Turning the user’s question into a vector to search that database.

If you index your data with Google’s `text-embedding-004` but try to search it using a vector created by OpenAI’s `text-embedding-3-small`, the math will not align. It would be like trying to find a street address in Paris using a map of Kalamazoo—the coordinates mean completely different things.

### The Proprietary "Black Box"
Embedding models are often proprietary "Black Boxes." For example, the internal "math" of how Google translates a word into a vector is completely different from OpenAI's math.
*   **Architect's Perspective:** You treat the embedding model as a Black Box Translator. You feed it Text; it spits out Numbers. You save those Numbers in a database next to the Text.
*   **Intercompatibility:** You cannot mix vectors from different models (a "handshake" between raw numbers fails). However, because the final retrieval stage converts the vector back into plain text before it reaches the LLM, the LLM itself (the "Brain") can read text found by *any* embedding model.

| Scenario | Possible? | Why? |
| :--- | :--- | :--- |
| **Search:** Google Vector vs. Google Vector | **YES** | They speak the same "mathematical language." |
| **Search:** Google Vector vs. OpenAI Vector | **NO** | Different coordinate systems; raw numbers don't match. |
| **Processing:** Google-found Text → OpenAI LLM | **YES** | Both models speak "Human Language" (English, Python, etc.). |

---

## 5. Implementation in Global Settings

Always explicitly set your `embed_model` in the global `Settings` at the start of your script.

```python
from llama_index.embeddings.google import GoogleGenAIEmbedding
from llama_index.core import Settings

# 1. Instantiate the model
embed_model = GoogleGenAIEmbedding(
    model_name="models/gemini-embedding-2-preview",
    embed_batch_size=100
)

# 2. Set it globally
Settings.embed_model = embed_model
```

---

## 6. Advanced Usage: Semantic Splitting

The `embed_model` shifts the logic of document parsing from syntactic (character counts) to semantic (meaning).

### SemanticSplitterNodeParser
Instead of splitting at a fixed character limit (e.g., 1024), the `SemanticSplitterNodeParser` uses the embedding model to identify "meaning shifts."

- **Adaptive Breakpoints:** If Sentence A and B have high cosine similarity, they stay in the same node. If the meaning shifts significantly, a new node is created.
- **Contextual Integrity:** Nodes contain complete thoughts, improving RAG accuracy.
- **Trade-off:** Slower and potentially more expensive, as every sentence requires a model call during the parsing phase.

### Contract Prototype
```python
from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.core.node_parser import SemanticSplitterNodeParser

class SemanticParserContract:
    embed_model: BaseEmbedding 
    buffer_size: int = 1
    breakpoint_percentile_threshold: int = 95

    def get_parser(self):
        return SemanticSplitterNodeParser(
            embed_model=self.embed_model,
            buffer_size=self.buffer_size,
            breakpoint_percentile_threshold=self.breakpoint_percentile_threshold
        )
```
