# Context Engineering: Making Projects "Legible" to AI Agents

In professional AI-native workflows, making a codebase "legible" to an Agent CLI while staying token-efficient is an emerging discipline called **Context Engineering**.

Instead of feeding the agent your entire source tree (which is often "noisy" and expensive), you provide a **Layered Context Map**. This ensures the agent is grounded in the project's architecture and current state without overwhelming its context window.

---

## 1. The Components of a "Legible" Project
To keep the agent updated on the "what," "where," and "how" of your framework, a legible project structure includes the following major components:

### Architectural Guardrails (`ARCHITECTURE.md` or `AI.md`)
This is the **blueprint**. It defines the "why" and "global rules" of the project.
- **Example Rules:** "All dataclasses must be immutable," or "Use Pydantic for validation."
- **Function:** Prevents architectural drift and ensures the agent follows established patterns.

### The Session State (`PROGRESS.md` or `GEMINI.md`)
This is the **short-term memory**. It tracks exactly what is working, what is in "testing," and what is a "partial" implementation.
- **Function:** Bridges the gap between sessions so the agent knows exactly where it left off.

### Interface Definitions (`__init__.py` or Types)
In languages like Python, clean type hinting and `__all__` definitions in `__init__.py` files act as a **table of contents** for the agent.
- **Function:** Allows the agent to understand the available API surface without reading every line of implementation logic.

---

## 2. Professional Implementation: How to Blueprint
Developers use **Compaction** and **Explicit Artifacts** to fit critical project information into the agent's context window efficiently.

### A. The "Progress.md" Pattern (Token Efficient)
Instead of asking the agent to "guess" the project's state, you maintain a high-density file that acts as the single source of truth for completion status.

**Example `PROGRESS.md` Structure:**
- `[WORKING]` `core/extractor.py` - Fully tested, handles JSON/CSV.
- `[PARTIAL]` `core/transformer.py` - Logic exists but lacks error handling for nulls.
- `[TESTING]` `core/loader.py` - Awaiting database connection strings.

### B. Instructional Metadata (`.cursorrules` or `agent.md`)
Many professional tools look for specific files in the root directory containing rules for the agent. This prevents the agent from "forgetting" naming conventions or preferred libraries.
- **Contents:** Naming conventions, preferred libraries, and specific "Don't do X" instructions.

---

## 3. Summary: How State is Observed

| Component | Industry Term | How the Agent "Observes" |
| :--- | :--- | :--- |
| **Blueprints** | Grounding Rules | Reads your `AI.md` or specific "rules" file at startup. |
| **Project State** | Session Artifacts | Reads a `progress.md` or `todo.md` created by you or its previous run. |
| **Code Structure** | Workspace Map | Runs `tree -L 2` or `git ls-files` to see the skeleton without the "meat." |
| **Logic/API** | Stubbing | Reads just the signatures (docstrings/method names) without the full function body. |

---

## The "Pro" Move: The Model Context Protocol (MCP)
The most modern way professionals manage context in 2026 is via the **Model Context Protocol (MCP)**.

- **How it works:** You run an MCP server (a small local daemon) that "serves" context to your Agent CLI.
- **The Benefit:** Instead of you manually providing code, the Agent "queries" the MCP server (e.g., "What are all the dataclasses in the `/models` directory?"). The server returns only the relevant definitions, saving thousands of tokens and ensuring high-precision context delivery.
