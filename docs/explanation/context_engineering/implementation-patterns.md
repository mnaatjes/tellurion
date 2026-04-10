# Context Implementation Patterns: Making Projects "Legible"

In professional AI-native workflows, making a codebase "legible" to an Agent CLI while staying token-efficient is a primary goal. This is achieved through structured project components and specialized workflows.

---

## 1. The Components of a "Legible" Project
To keep the agent updated on the "what," "where," and "how" of your framework, you structure the following major components:

### Architectural Guardrails (`ARCHITECTURE.md` or `AI.md`)
This is the **blueprint**. It defines the "why" and "global rules" (e.g., "All dataclasses must be immutable," or "Use Pydantic for validation"). It provides the high-level grounding rules that the agent must observe.

### The Session State (`PROGRESS.md` or `GEMINI.md`)
This is the **short-term memory**. It tracks exactly what is working, what is in "testing," and what is a "partial" implementation. This creates a hand-off point for the next session.

### Interface Definitions (`__init__.py` or Types)
In Python, clean type hinting and `__all__` definitions in your init files act as a **table of contents** for the agent, allowing it to understand the API surface area without reading implementation details.

---

## 2. Professional Implementation: The PRP Workflow
Product Requirements Prompts (PRPs) are comprehensive implementation blueprints designed specifically for AI coding assistants.

### The Lifecycle of a PRP
1.  **Initial Request (`INITIAL.md`):** The human developer describes the feature requirements, examples, and relevant documentation links.
2.  **Research & Blueprinting (`/generate-prp`):** The agent researches the codebase, gathers documentation, and creates a step-by-step implementation plan (the PRP).
3.  **Execution & Validation (`/execute-prp`):** The agent implements the feature according to the PRP, running tests and fixing errors until all success criteria are met.

**Key Benefit:** By separating requirements definition from execution, you ensure the agent follows a consistent, validated plan.

---

## 3. Persistent Memory vs. Session-Based Interaction
How an agent "remembers" its environment depends on the underlying architecture:

| Feature | Session-Based Agents (Gemini CLI) | Persisted Agents (Letta Code) |
| :--- | :--- | :--- |
| **Relationship** | Like meeting a new contractor. | Like working with a teammate. |
| **Context** | Current session history + `GEMINI.md`. | Memory persists across sessions and conversations. |
| **Memory Management** | Summarization/PRP hand-off. | Dynamic learning, `/remember`, and `/skill`. |
| **Consistency** | Requires explicit context state files. | Naturally improves over time with use. |

### The "Pro Move": The Unified Agent File
In high-level workflows, you combine the **Mandate** (The Law) at the top of a file like `GEMINI.md` and the **Current State** (The Memory) at the bottom. This ensures every initialization grounded in project rules and recent progress.
