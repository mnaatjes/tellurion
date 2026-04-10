# Advanced Cognitive Architectures for Context Engineering

When tasks exceed the limits of single-model reasoning, developers utilize advanced architectural patterns to ensure high-fidelity context management.

---

## 1. Sub-Agent Isolation (Context Segregation)
The most powerful defense against "context suicide" is the use of specialized sub-agents with their own isolated context windows.
- **The Pattern:** Instead of a single model juggling everything, an **Orchestrator** delegates risky operations (e.g., searching a large codebase) to a **Sub-Agent**.
- **The Benefit:** 50,000 tokens of exploration by the sub-agent can be "folded" into a 2,000-token summary for the orchestrator. If a sub-agent fails due to context overflow, it doesn't kill the orchestrator's session.

## 2. Code Mode (Filtering Before Context)
Instead of receiving a raw tool response (e.g., 100,000 tokens of data) directly into its context, the agent writes code to fetch, process, and filter the data in a secure execution environment.
- **Mechanism:** The agent is "programming its own data pipeline." It can filter 10,000 rows to the 5 relevant ones before any tokens are sent to the model's context.
- **Result:** Drastic token savings and reduced tool confusion.

## 3. Recursive Language Model (RLM)
For processing data beyond any single context limit (e.g., an entire corporate wiki or a complex monorepo), RLM stores context in a Python REPL environment.
- **Mechanism:** Data lives in REPL memory, not the context window. The model writes Python code to "peek" at subsets, partition the data into chunks, and recursively process them.
- **Scale:** Can theoretically process inputs far beyond any context limit by decomposing the problem into isolated, manageable sub-contexts.

## 4. Memory Pointers (Context Offloading)
Large tool outputs or documents are stored in external memory and referenced via lightweight IDs (Pointers).
- **Mechanism:** The agent sees `[memory:doc_12345]` (20 tokens) instead of the full 10,000-token document.
- **Benefit:** Allows an agent to track hundreds of documents simultaneously without saturating the context window.

---

## 5. Summary: Advanced Patterns

| Architecture | Strategy | Best For |
| :--- | :--- | :--- |
| **Sub-Agents** | Isolation and Folding | High-risk, multi-step explorations. |
| **Code Mode** | Server-Side Filtering | Massive data ingestion and chaining. |
| **RLM** | Recursive Decomposition | Inputs exceeding all context limits. |
| **Memory Pointers** | Out-of-band Storage | Long-term tracking of many documents. |
| **Agent Harness** | Deterministic Shelling | Standardizing state recovery and persistence. |
