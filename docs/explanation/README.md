# Project Explanations and Conceptual Deep Dives

<!-- AI_CONTEXT: This directory contains deep dives into project concepts, protocols, and architectural patterns. Refer to these to understand the underlying logic of the system's components. -->

This directory provides deep dives into the core concepts, communication protocols, and architectural patterns utilized across the Tellurion ecosystem.

---

## 1. Explanation Directory Map

### System Logic
- **[Architecture Evolution](./architecture-evolution.md):** Detailed history and reasoning behind the project's evolution.
- **[Repository Strategy](./repository-strategy.md):** The logic behind our monorepo/polyrepo structure.
- **[Relevant Architecture Patterns](./relevant-architecture-patterns.md):** Guides on Hexagonal, CQRS, and other project-wide patterns.

### Agentic Protocols
- **[Agent Protocols](./agent-protocols.md):** Deep dives into standardized agent communication (REST vs. JSON-RPC).
- **[Gemini CLI Branch](./gemini-cli/README.md):** Specialized documentation for the Gemini CLI and its integrations.
- **[Client-Agent Orchestration](./client-agent-orchestration.md):** Logic for coordinating multiple agent instances.

### Data and Knowledge
- **[Ingestion Pipeline](./ingestion-pipeline.md):** Conceptual overview of the data ingestion and transformation logic.
- **[Knowledge Graphs](./knowledge-graphs.md):** Theory and implementation of graph-based system memory.
- **[Vector Embeddings](./base-embedding.md):** How the system uses numerical arrays for semantic retrieval.
- **[Managing Token Efficiency](./managing-token-efficiency.md):** Strategies for context management and cost reduction.

---

## 2. Learning Principles
- **Concept First:** Before implementing a new feature, ensure its conceptual logic is documented here.
- **Standardized Communication:** Refer to the protocols documentation to maintain system interoperability.
