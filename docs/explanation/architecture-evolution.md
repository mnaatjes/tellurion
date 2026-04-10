# Explanation: Monorepo-to-Polyrepo Evolution

## 1. The Strategy: "The Strangler Fig" Evolution
In the early phase of project growth, we utilize the **Modular Monorepo** approach. This allows for high developer velocity while maintaining clean architectural boundaries.

### The Stages of Extraction
1.  **Componentization:** Strictly enforce folder boundaries. Treat internal folders as if they were external libraries, preventing "spaghetti" imports.
2.  **Workspace Implementation:** Introduce a workspace manager (like **uv** or **Poetry**) to manage these folders as independent packages while they still live in one repo.
3.  **The Extraction:** One by one, the most stable or independent components (e.g., the `Ingestion-Pipeline`) are moved to their own dedicated Git repositories.
4.  **Dependency Linking:** The original project pulls the extracted component as a remote dependency (via Git URL or private PyPI) rather than a local path.

---

## 2. Python Workspaces
Python Workspaces allow us to manage a collection of related packages within a single environment. This is the core engine of our modular development strategy.

### Technical Mechanics
*   **Shared Virtual Environment:** Instead of each sub-project having its own `venv`, the workspace creates one "mega-environment" that contains all dependencies for all sub-packages.
*   **Local Cross-Pollination:** If the `Skill-Manager` depends on the `Skill-Factory`, the workspace tool marks the Factory as an **editable install**. Editing code in the Factory folder instantly updates the Manager’s behavior without requiring a re-install.
*   **Dependency Resolution:** The workspace tool calculates a single "solve" for all packages. This ensures all components use compatible versions of shared libraries (e.g., `pydantic`, `requests`), preventing runtime conflicts.

### Recommended Tooling
*   **uv:** Currently the fastest and most modern choice for Linux/Python workspaces.
*   **Poetry:** Uses "Multiproject" plugins or native workspace features to handle local path dependencies.

## 4. The 2026 Professional Workflow: Advanced Agentic Systems

Beyond the RAG stack, a professional AI/LLM-assisted workflow is built on Agentic Orchestration, Observability, and Infrastructure. Detailed breakdowns of these components can be found in **[The Operational Stack](operational-stack.md)**.

### A. Agentic Orchestration (The "Staff")
As you move from simple chat to "Agents," the system gains **Agency**—the ability to reason, plan, and execute multi-step tasks independently.
*   **Planning & Reasoning:** Breaking complex goals (e.g., "Implement a new API endpoint") into a sequence of bite-sized tasks.
*   **Tool-Use (Function Calling):** The LLM decides when to use external tools (Linux terminal, Python interpreter, MCP Server).
*   **Reflection & Loops:** The agent runs a test, reads the error, and self-corrects the code before presenting it to the user.

### B. LLM Observability & Evaluation (The "Analytics")
*   **Tracing:** Every tool call and vector search is logged to debug where a "hallucination" started.
*   **Evaluation (LLM-as-a-Judge):** A high-reasoning model (e.g., Gemini 1.5 Pro) grades primary model outputs for **Faithfulness** (RAG adherence) and **Relevance**.
*   **Cost Tracking:** Monitoring real-time spend across providers to prevent runaway recursive loops.

### C. AI Gateways & Guardrails (The "Security")
*   **Input Guardrails:** Scans queries for PII (Personally Identifiable Information) or "jailbreak" attempts.
*   **Output Guardrails:** Validates that responses match expected formats (e.g., valid JSON or schema-compliant code).
*   **Semantic Caching:** Serving repeated questions from a local cache to reduce latency by 90% and costs by 30%.

---

## 5. Benefits Comparison
| Feature | Standard Polyrepo | Monorepo w/ Workspaces |
| :--- | :--- | :--- |
| **Isolation** | High | High |
| **Refactoring** | Hard (requires versioning/re-installs) | Easy (local linking) |
| **Dev Velocity** | Slow (due to dependency overhead) | Fast (optimized linking) |
| **Deployment** | Independent | Independent |

---
**Next Steps:**
*   Review [Contract and Testing Standards](../reference/contract-and-testing-standards.md) for rules on inter-package communication.
