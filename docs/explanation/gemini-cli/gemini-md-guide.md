# The Purpose of GEMINI.md: A Hybrid Context Artifact

The **`GEMINI.md`** (or `AI.md`) document is a specialized context artifact designed to solve the "Amnesia Problem" of Large Language Models (LLMs). It acts as both the **Project Constitution** and the **Session Bridge**, aligning the agent's reasoning with the project's actual structure and goals.

By combining governance rules and operational state into a single, token-efficient file, you ensure that the agent understands **who to be** and **where it left off** every time it is initialized.

---

## 1. The Persona & Governance Layer (The "Law")
This section defines the rules of engagement. It prevents the agent from falling into "lazy coder" patterns and establishes non-negotiable architectural standards.

- **The Mandate:** Clearly defines the agent's role (e.g., Senior Architectural Mentor, DevOps Lead).
- **The Constraints:** Establishes which patterns are mandatory (e.g., Hexagonal Architecture, strict Pydantic validation).
- **The Hierarchy:** Dictates which files or documentation sources take precedence during a conflict.

## 2. The Operational State Layer (The "Memory")
Because project roots can be vast, this section provides a "Map" of the project's current progress. It allows the agent to observe its own momentum without rescanning every file.

- **The Frontier:** Specifies the precise task or sub-task currently being addressed.
- **The Status Map:** Lists which modules are "Contract-Complete," "Implementation-Partial," or "Awaiting Tests."
- **The Hand-off:** Critical notes for the next initialization of the CLI.

---

## 3. Professional Synthesis: The Unified Agent File
Combining these layers into one file creates a **Force Multiplier**. In a professional workflow, the Mandate is placed at the top and the Current State at the bottom. This ensures that the first few thousand tokens the agent reads ground its identity before it observes its current task.

### Major Components Observed
When an Agent CLI reads `GEMINI.md`, it is observing four things:

| Component | Industry Term | How it's Used |
| :--- | :--- | :--- |
| **Identity** | Persona | "Am I an architect or a debugger?" |
| **Authorities** | Governance | "What laws (e.g., `.tellurion/rules.yml`) must I check before acting?" |
| **Boundary** | Scope | "What is the specific scope of the Source Tree I am allowed to touch?" |
| **Momentum** | Progress | "What is the very next step in the pipeline?" |
