# Glossary of Agent-CLI Concepts

This document defines core concepts related to the operation and management of agent-based command-line interfaces.

---

## Agent-CLI "Windows"
### How "The Window" Works
When you send a prompt to an LLM, you aren't just sending your latest message. To "remember" what happened previously, the CLI client bundles everything together and sends it as one giant block of text every single time you hit enter.
- **Reference:** [Monitoring and Managing the Context Window](../how-to/gemini-cli/monitor-context-window.md)

### The Hard Limit
Every model has a maximum capacity (e.g., 128k tokens for GPT-4o, or 1M+ for Gemini 1.5 Pro). This defines the maximum amount of context (history + current prompt + instructions) that can be processed at once.

### The "Anchor" Strategy
By saying the `GEMINI.md` or System Instruction "stays in the window," it means that as the conversation gets longer and older messages are eventually "pushed out" (deleted) to make room for new ones, the Anchor is programmatically kept at the very top of every request.
- **Reference:** [System Design Considerations](../design/outline.system-design-considerations.md)

### Why "The Window" is a Budget
For developers working in a Linux environment and focusing on ETL, it’s helpful to view the window as a resource buffer:
- **Fixed Cost (The Anchor):** Your core rules and project outline. This might take up 500–1,000 tokens. You pay this "tax" on every turn to ensure the agent doesn't forget its persona.
- **Variable Cost (The Retrieval):** The specific documentation chunks or code snippets you pull in via RAG.
- **The Remainder:** What’s left for the actual conversation and the model's "reasoning" space.

---

## Agent Protocol
### The "HTTP for Agents"
The Agent Protocol is a platform-agnostic API specification that standardizes how a user (or a CLI) sends a goal to an agent and how that agent reports back its progress.
- **Key Function:** Standardizes communication between different agent backends (AutoGPT, custom Python agents) and CLI clients.
- **Standard Endpoints:** Includes `/ap/v1/agent/tasks` and `/ap/v1/agent/tasks/{id}/steps`.
- **Reference:** [Understanding Agent Protocols](../explanation/agent-protocols.md), [Gemini CLI Agent Protocol](../../docs/explanation/gemini-cli/gemini-agent-protocol.md)

---

## CAO: CLI Agent Orchestrator
### The "Team Manager"
CAO is a multi-agent orchestration framework that manages multiple Gemini CLI instances as independent, parallel processes.
- **Parallel Execution:** Uses **tmux** or **screen** to spin up separate terminal instances for each expert.
- **Isolated Context:** Each expert runs in its own process, ensuring its context window remains 100% focused on its specific domain.
- **Reference:** [Integrated Workflow: Single Instance vs. CAO Orchestration](gemini-cli/integrated-workflow.md), [Prototype: Client Agent Orchestrator](../design/prototype.client-agent-orchestrator.md)

---

## The Catalog (The "Public View")
The Catalog is a frontend "View" or "Projection" of the Registry. It is what the user interacts with to discover what is possible.
- **Definition:** A curated, read-only representation of the available items in the Registry, often enriched with human-friendly metadata (descriptions, tiers, versions).
- **Intent:** Discovery and Selection. It is built for the human to answer the question: "What can I use right now?"
- **Analogy:** The Library Card Catalog. It provides a summary, a title, and a location so you can find what you need without walking through 10 miles of shelves.
- **Contract:** `list_all()`, `filter_by_type()`, or `search(query)`.
- **Architecture:** Acts as the **Query (Read)** side of the CQRS pattern. It is a "Managed View" rather than a self-managing entity; because it is read-only at runtime, it has no state of its own to manage. It simply projects the current state of the Registry.

---

## Context Window
The maximum amount of information (tokens) the LLM can "hold in its head" at a single moment. It is the sum of System Instructions (Anchor), the Working Set (Files), Chat History, and Tool Outputs.
- **Reference:** [Monitoring and Managing the Context Window](../how-to/gemini-cli/monitor-context-window.md), [Context Window Monitoring Tools](tooling/context-window-monitors.md)

---

## Evaluation (LLM-as-a-Judge)
The process of using a high-reasoning model (like Gemini 1.5 Pro) to audit the performance of a specialized agent.
- **Pattern:** The "Triangle of Truth" (Source vs. Expert vs. Judge).
- **Reference:** [System Design Considerations](../design/outline.system-design-considerations.md)

---

## Gemini CLI Instance
A standalone execution of the `gemini` command. In a single instance, only one **Skill** is truly active in the context window at a time.
- **Reference:** [Integrated Workflow: Single Instance vs. CAO Orchestration](gemini-cli/integrated-workflow.md), [Instance-Based Manager Prototype](../design/prototype.instance-based-manager.md)

---

## Human-in-the-Loop (HITL)
The recognition that the human developer remains the ultimate orchestrator. Includes "Veto" interfaces and "Deep-Dive" modes for manual steering.
- **Reference:** [Skill Factory Prototype](../design/prototype.skill-factory.md)

---

## Knowledge Graphs
A mapping of logical relationships between entities (e.g., Salesforce_Lead -> BigQuery_Table). Unlike Vector RAG, it enables multi-hop reasoning and logic enforcement.
- **Reference:** [Configuring Knowledge Graphs](../how-to/gemini-cli/configure-knowledge-graphs.md), [Knowledge Graph Tooling](tooling/knowledge-graph-tools.md)

---

## MCP Server
A lightweight program that exposes specific functionalities (filesystem access, DB querying) to an MCP client.
- **Key Functions:** Tool provisioning, resource access, and standardized communication (JSON-RPC).
- **Reference:** [MCP Configuration Reference](gemini-cli/mcp-configuration.md), [Understanding MCP Integration](../../docs/explanation/gemini-cli/mcp-integration.md), [Setting Up MCP Servers](../how-to/gemini-cli/setup-mcp.md)

---

## Memory Persistence
The physical storage infrastructure (JSON, SQLite, Vector Store) that holds data outside the LLM's temporary context window to track long-term progress.
- **Key Fields:** Struggles, Preferences, and Mastered Topics.
- **Reference:** [System Design Considerations](../design/outline.system-design-considerations.md)

---

## The Registry (The "Private Record")
The Registry is a backend data structure (usually a Dictionary or Database) that holds the "Truth" of your system. It is managed by the Registrar.
- **Definition:** A centralized mapping of unique identifiers (Keys) to their implementation details (Values/Blueprints).
- **Intent:** Storage and Retrieval. It is built for the machine to find a specific tool when it needs to run a task.
- **Analogy:** The Library Stacks. It is where the actual books are sorted by call number. It’s dense, strictly organized, and not meant for "browsing."
- **Contract:** `get(key)` and `set(key, value)`.
- **Architecture:** The "Source of Truth" and backend storage for Blueprints. In Hexagonal Architecture, this follows the **CQRS (Command Query Responsibility Segregation)** pattern:

| Action Type | Hexagonal Component | Role | Logic Type |
| :--- | :--- | :--- | :--- |
| **Command (Write)** | **Registrar** | The "Input" | Validation & Storage |
| **Query (Read)** | **Catalog** | The "Output" | Filtering & Formatting |

---

### The Registry/Catalog Relationship
In a strictly Hexagonal or Clean Architecture, the relationship is asymmetrical because their "jobs" are different.
- **The Registrar:** The "Writer." It has the keys to the vault and can add/modify Blueprints (the Input Port).
- **The Registry:** The "Database." The actual dictionary sitting on your system's RAM.
- **The Catalog:** The "Reader." It simply looks at the Registry and formats it for the human (the Output Port).

**Rule:** You only have one Registry (the data), but you can have one Registrar and one Catalog sitting on top of it. This ensures **Data Integrity**: the Catalog never shows a model that hasn't been put into the Registry.

---

## Runbook
A structured instruction set used to restrict an agent's focus and define specific procedural workflows.
- **Roles:** Context scoping, workflow orchestration, and standardization.
- **Reference:** [Setting Up Runbooks](../how-to/gemini-cli/setup-runbook.md)

---

## Session Commands
The specific "Slash Commands" (e.g., `/clear`, `/compress`) used to interact with the CLI's internal state without sending text as a prompt to the LLM.
- **Reference:** [Monitoring and Managing the Context Window](../how-to/gemini-cli/monitor-context-window.md)

---

## Temperature
A hyperparameter controlling the predictability (low temp) versus creativity (high temp) of model output. Used primarily for hallucination management in technical tasks.
- **Reference:** [Defining Expert Agents](../how-to/gemini-cli/define-skills.md)

---

## Top-P (Nucleus Sampling)
A hyperparameter that cuts off the "long tail" of low-probability tokens. Combined with Low Temperature, it creates a "Double Lock" for factual accuracy.
- **Reference:** [Defining Expert Agents](../how-to/gemini-cli/define-skills.md)

---

## Vector Embeddings
The conversion of text into numerical arrays to enable efficient semantic search (RAG) without overwhelming the context window.
- **Mechanism:** Similarity search against a local cache (e.g., `.gemini/cache/embeddings/`).
- **Reference:** [Assigning and Managing Vector Embeddings](../how-to/gemini-cli/assign-vector-embeddings.md)
