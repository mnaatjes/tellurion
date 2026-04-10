# Context Optimization Techniques

To maximize the signal density within a model's limited context window, professional developers employ a series of optimization strategies designed to prioritize high-value tokens.

---

## 1. Context Selection (Precision over Volume)
Don't provide everything; provide only what matters.
- **Dynamic Context:** Use RAG paired with a **Reranking layer** to surface only the most relevant facts.
- **Segmented Reasoning:** Have the model break its reasoning into logical segments so only the necessary pieces flow to the next step.
- **Semantic Tool Search:** Instead of binding every tool to the model on every call, use semantic search to load only the tools relevant to the current query.

## 2. Context Compression and Compaction
Managing "Context Rot" by stripping out redundant information.
- **Summary:** Condense older conversation turns (e.g., turns 1–10) into a few concise lines, while keeping only the most recent turns (turns 11–15) in full detail.
- **Semantic Extraction:** Extract specific facts (e.g., a user's stated budget) and store them in long-term episodic memory, then discard the raw messages.
- **Context Folding:** For complex tasks, an agent can branch off to handle a sub-task and then "fold" it upon completion, collapsing the intermediate steps while retaining a summary of the outcome.

## 3. Context Ordering (Leveraging Attention Bias)
Where information is placed matters as much as what is included.
- **The "Lost in the Middle" Solution:** Place critical instructions at the very top (Anchor) and the most recent, task-relevant data at the very bottom (Frontier).
- **Reranking:** Sort information within the middle of the context window by relevance or recency to ensure essential details don't fade into the "blind spot."

## 4. Format Optimization (Reducing Token Overhead)
The format of your data directly impacts your token "budget."
- **Structured Markup:** Use explicit tags (e.g., XML `<instructions>...</instructions>`) to provide the model with unambiguous signals about the role of each text block.
- **YAML vs. JSON:** When providing structured data, prefer **YAML** over JSON. YAML can carry roughly **66% less token overhead** for the same amount of information.

## 5. Summary: Optimization Strategy

| Strategy | Technical Mechanism | Goal |
| :--- | :--- | :--- |
| **Selection** | Reranking / Semantic Tool Search | Increase signal-to-noise ratio. |
| **Compression** | Summarization / Fact Extraction | Reclaim context window space. |
| **Ordering** | Temporal and Relevance Sorting | Maximize model attention on key details. |
| **Formatting** | XML Tagging / YAML usage | Reduce token overhead and improve parsing. |
| **Isolation** | Sub-agent delegating | Prevent cross-task contamination. |
