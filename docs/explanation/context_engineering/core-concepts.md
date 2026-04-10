# Core Concepts of Context Engineering

**Context Engineering** is an optimization problem: it is the search for the best combination of functions to assemble a context that maximizes the quality of what an LLM produces for any given task.

---

## 1. Beyond Prompt Engineering
While prompt engineering focuses on *what* you say to a model, **Context Engineering** is about *what the model sees before you say anything*. It doesn't replace prompt engineering—it absorbs it. Clear instructions remain vital, but they are now just one component of a dynamically assembled information environment.

## 2. The Operating System Analogy
As Andrej Karpathy framed it, LLMs can be viewed as a new type of operating system:
- **CPU:** The LLM itself (the reasoner).
- **RAM:** The context window (the working memory).
- **Hard Drive:** External memory systems (vector databases, archives, etc.).

**Context Engineering** is the discipline of carefully managing what is loaded into the model's "RAM" (context window) at any given moment to maximize "attention budget" and precision.

---

## 3. The Components of a Context Payload
A modern AI context is not a fixed block of text; it is a **living payload** dynamically assembled for every interaction using various memory systems:

| System Type | Component | Description | Cognitive Map |
| :--- | :--- | :--- | :--- |
| **Static Rules** | **System Prompt** | Core identity, behavioral rules, persona, and guardrails. | Procedural Memory |
| **Short-Term** | **Message History** | The running thread of conversation, including tool calls and internal reasoning. | Working Memory |
| **Episodic** | **User Preferences** | Stored facts about the user, prior interactions, and behavioral patterns. | Personal Memory |
| **Semantic** | **Retrieved Info** | Domain-specific knowledge pulled from internal wikis, documentation, or databases. | World Knowledge |
| **Capabilities** | **Tool Schemas** | JSON definitions of available tools, actions, and output formats. | Self-Awareness |

## 4. The Cyclical Flow
Context Engineering is a continuous loop:
1.  **Task Trigger:** A user query triggers retrieval across episodic, semantic, and procedural memory.
2.  **Assembly:** Retrieved information merges with the system prompt, history, and tool schemas to form the context payload.
3.  **Inference:** The model processes the payload and produces an output.
4.  **Feedback/Write-back:** New facts, preferences, or decisions are written back to long-term memory, making the system sharper for the next interaction.
