# System Design Outline: Agent Management & Orchestration

This document outlines the architectural strategy for managing and orchestrating specialized AI agents within the Gemini CLI environment, focusing on token efficiency, role-based specialization, and long-term memory.

---

## 1.0 Token Efficiency & Context Management

Sending entire documentation manuals to an LLM is cost-prohibitive and leads to "lost in the middle" errors. To maintain accuracy while minimizing costs, we employ a **Layered Context Strategy**.

### 1.1 The Layered Context Strategy
Instead of a monolithic "data dump," the agent's context window is managed through three distinct layers.

#### 1.1.1 Layer 1: The Anchor (Static & Global)
The Anchor defines the core identity, goals, and behavioral rules of the agent. This information remains permanently in the context window.
- **Components:** System Instructions, `GEMINI.md`, and `CONVENTIONS.md`.
- **Function:** Ensures the agent maintains its persona and adheres to project-wide standards across all turns.
- **Constraints:** Limited by the model's total token capacity; must be kept concise.

#### 1.1.2 Layer 2: The Working Set & Runbooks (Dynamic & Context-Sensitive)
This layer contains only the specific files or documentation chapters relevant to the current task.
- **Working Set:** Defined by the `cwd()` and project-level configuration. It maps the "geographical state" of the project scope.
- **Runbooks:** Procedural instruction sets located in `./.gemini/runbooks/`.
  - **`.md`**: Best for complex, "agentic" workflows and narrative instructions.
  - **`.json`**: Ideal for strict, programmatic configurations.
  - **`.yml`**: A middle-ground for structured configuration and metadata.

#### 1.1.3 Layer 3: The Ephemeral (Session-Specific)
This layer consists of transient data that is summarized or discarded once a sub-task is complete.
- **Content:** Search results (`google_web_search`), tool outputs, and raw data downloads.
- **Location:** Typically stored in `/tmp/gemini-cli-cache-[hash]/`.
- **Management:** Automatically pruned or summarized to prevent context window saturation.

### 1.2 Data Synthesis & Compaction Techniques
To further optimize token usage, documentation is "digested" before being presented to the agent.

- **Pre-Processing (Digestion):** Specialized scripts extract key facts, API signatures, and logic flows from raw manuals, reducing 100 pages of text into a high-density 2-page distillation.
- **Vector Embeddings (Semantic RAG):** Documentation is converted into numerical vectors. The CLI retrieves only the top-N most relevant chunks (Similarity Search) rather than the entire document.
- **Adaptive Compaction:** As a session progresses, the CLI automatically summarizes older history to free up reasoning tokens for the current task.

---

## 2.0 Agent Specialization (The "Department of Experts")

Rather than using a general-purpose chatbot, this architecture utilizes a "Department of Experts"—specialized agents with restricted scopes and unique toolsets.

### 2.1 Role-Based Personas
Each expert is defined by a **Skill** that strictly limits its identity and authority.

### 2.2 Skill Directory Structure
Skills are organized within the `./.gemini/skills/` directory:

```text
.gemini/skills/
└── bigquery-architect/          # Unique Expert identifier
    ├── SKILL.md                 # REQUIRED: Frontmatter metadata + Instructions
    ├── scripts/                 # Expert-specific tools (Python/Bash)
    │   └── validate_sql.py      # A tool unique to this Architect
    ├── references/              # Optimized Layer 2 documentation
    │   └── bq_best_practices.md
    └── config.json              # Optional: Model overrides (e.g., Temperature)
```

### 2.3 Skill Components
- **`SKILL.md`**: The primary triggering mechanism. It must clearly describe the expert's capabilities for the model to activate it correctly.
- **`references/`**: The expert's private library.
  - **`.md`**: Checklists and narrative guides.
  - **`.json`**: API schemas and lookup tables (highly token-efficient).
- **`config.json`**: Overrides global settings for the specific agent:
  - **`model`**: Force a high-reasoning model (e.g., `gemini-1.5-pro`) for complex tasks.
  - **`temperature`**: Set to `0.1` for precision roles (Architects) or `0.7` for creative roles (Tutors).
  - **`excludeTools`**: Restrict access to sensitive tools or files.

---

## 3.0 Advanced Cognitive Architectures

### 3.1 Knowledge Graphs (The Logic Layer)
While Vector RAG finds "similar" text, it is often "relationship-blind." A Knowledge Graph (KG) provides the agent with system-wide structural awareness.

- **Nodes (Entities):** The "Nouns" of the system (e.g., Salesforce_Lead, BigQuery_Table).
- **Edges (Relationships):** The "Verbs" (e.g., POPULATES, TRANSFORMS).
- **Function:** Enables **Multi-Hop Reasoning** (e.g., "How does changing this Salesforce Lead object affect the BigQuery partitioning logic?").
- **Authority:** The KG acts as the "Ground Truth" for system architecture and business rules.

### 3.2 Evaluation (LLM-as-a-Judge)
To manage the non-deterministic nature of LLMs, we use a high-reasoning "Judge" model to audit specialized agents.

- **Pattern:** The "Triangle of Truth" (Source vs. Expert vs. Judge).
- **Implementation:** Automated via `evaluation_expert.py` scripts.
- **Metrics:**
  - **Fidelity:** Adherence to the source documentation.
  - **Relevancy:** Correctness of the logic and process followed.
  - **Syntax:** Validity of the generated output (e.g., SQL syntax).

### 3.3 Memory Persistence (The Long-Term Buffer)
To overcome "Session Amnesia," the architecture implements a multi-tiered memory system.

| Tier | Type | Location | Purpose |
| :--- | :--- | :--- | :--- |
| **Short-Term** | Context Window | RAM | Active conversation logic. |
| **Mid-Term** | Working Set | `./.gemini/cache/` | Recent files and search results. |
| **Long-Term** | Persistence Layer | `~/.gemini/memory/` | User struggles, preferences, and mastered topics. |

#### 3.3.1 Lesson Plan Adjustment
At the start of a session, the agent performs a "Pre-Session Handshake" with the Long-Term memory layer. It analyzes the user's progress and automatically adjusts its **Layer 1 Anchor** instructions to focus on current struggles while skipping mastered topics.
