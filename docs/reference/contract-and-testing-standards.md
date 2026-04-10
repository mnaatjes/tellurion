# Reference: Contract and Testing Standards

This document outlines the architectural standards for integration, state tracking, and context management in the Tellurion project.

## 1. Context Management & State Tracking

Professional integration of an LLM CLI into a project directory is built on three pillars: **Explicit Context Injection**, **State Persistence**, and **Architectural Guardrails**.

### A. State Persistence (Tracking Project Status)
The LLM does not inherently "remember" project history. State must be managed via physical files:
*   **The Manifest:** Maintain a `STATUS.md` or `PROGRESS.log` in the project root.
*   **Automation:** Pipe task completions to the CLI to update this file: `gemini "Finished user-auth" --update-status`.
*   **Grounding:** Include the manifest in future prompts (`gemini @STATUS.md "Next task?"`) to provide "long-term memory."

### B. Architectural Guardrails (Business Logic)
Never rely on the LLM to guess business rules or coding standards.
*   **Rules Files:** Define "Unbreakable Rules" in `.gemini-instructions` or `PROJECT_RULES.md`.
    *   *Example:* "All DB queries must use the Repository Pattern in /src/repo."
*   **Implementation:** Configure the CLI to automatically prepend these instructions to every request (System Prompt Engineering).

### C. Token & Context Management
Optimize the "Context Budget" to prevent the model from getting slower or less accurate ("Lost in the Middle").
*   **`.geminiignore`:** Similar to `.gitignore`, use this to exclude `node_modules`, `.venv`, and build artifacts from the index.
*   **Explicit Referencing:** Instead of sending the whole repo, use `@file` references for surgical context: `gemini @src/auth.py @docs/api.md "Fix timeout bug"`.

## 2. Testing Standards

(Add specific testing protocols for agentic workflows, RAG faithfulness, and tool-use here.)
