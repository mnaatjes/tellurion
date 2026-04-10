# Reference: Project Roles

This document defines the specialized roles involved in the design, development, and governance of the Tellurion project.

## 1. AI Solutions Architect

The AI Solutions Architect is the bridge between high-level business problems and technical implementation. Unlike a Data Scientist who focuses on training models, the Architect focuses on the entire ecosystem.

### Core Responsibilities
*   **System Design:** Deciding when to use RAG (Retrieval-Augmented Generation), fine-tuning, or prompt engineering.
*   **Tool Selection:** Evaluating which LLMs (OpenAI, Claude, Gemini) and Vector Databases (Pinecone, Chroma, SQLite) fit specific use cases.
*   **The "Plumbing":** Engineering the ingestion pipelines that connect internal data (APIs, PDFs, DBs) to the AI models.
*   **Governance:** Setting standards for AI safety, data privacy, and hallucination management.

### Key Skills
*   Deep understanding of **RAG Architecture** (Ingestion vs. Retrieval).
*   Expertise in **Modular Pipelines** and avoiding provider lock-in.
*   Ability to justify architectural decisions based on **Cost**, **Freshness**, and **Accuracy**.

---

## 2. Senior Architectural Mentor (AI Role)

*See [GEMINI.md](../../GEMINI.md) for behavioral directives.*

The Senior Architectural Mentor is an autonomous AI agent responsible for guiding the implementation of Tellurion.
*   **Gatekeeping:** Enforcing Hexagonal Architecture and the monorepo "Code of Laws."
*   **Validation:** Ensuring all changes are documented via ADRs and aligned with the system roadmap.
*   **Instruction:** Prioritizing teaching the developer "how" to build rather than performing all tasks in silence.
