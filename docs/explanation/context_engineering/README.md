# Context Engineering: The Art of Context Management

<!-- AI_CONTEXT: This directory contains deep dives into Context Engineering—the discipline of optimizing what information, tools, and formats are provided to an AI agent. Reference these files to understand how to build token-efficient and accurate AI workflows. -->

In professional AI-native workflows, the effectiveness of an agent is rarely determined by the model's capacity alone. Instead, it depends on **Context Engineering**: the strategic curation of the model's limited context window with the right information, at the right time, in the right format.

---

## 1. Context Engineering Map

### Foundational Concepts
- **[Core Concepts](./core-concepts.md):** What is context engineering, why it absorbs prompt engineering, and the components of a context payload.
- **[Context Hydration](./context-hydration.md):** The discipline of managing project state, layers of hydration, and the "Map" vs. "Guts" approach.
- **[Evolution and History](./evolution-and-history.md):** The origin of the term, thematic blocks, and its role in the SDLC.
- **[Implementation Patterns](./implementation-patterns.md):** How to make projects "legible" via Architectural Guardrails, Session State (GEMINI.md), and the **PRP Workflow**.
- **[Challenges and Bottlenecks](./challenges.md):** Understanding Context Rot, "Lost in the Middle," Context Drift, and Tool Confusion.

### Optimization and Architecture
- **[Optimization Techniques](./optimization-techniques.md):** Selecting context, compression (summary vs. semantic), ordering (attention bias), and format optimization (XML vs. YAML).
- **[Advanced Cognitive Architectures](./advanced-architectures.md):** Multi-agent isolation, Code Mode (filtering before context), Memory Pointers, and Recursive Language Models (RLM).

### Artifacts and Governance
- **[The Hybrid Context Artifact (GEMINI.md)](../gemini-cli/gemini-md-guide.md):** A detailed guide on the "Unified Agent File" as a project constitution.

---

## 2. Professional Strategy
To build production-ready AI agents, developers must move beyond simple prompts and design the entire **Information Environment** around the model. The goal is precision and signal density—ensuring the agent only sees what is relevant to the task right in front of it.

---

## 3. External Resources & Community References

### Research & Foundations
- **[Context Engineering (Boni Garcia)](https://github.com/bonigarcia/context-engineering.git):** A comprehensive companion to the book "Context Engineering," covering the art and science of shaping context-aware AI systems.
- **[Context Engineering Intro (Cole Medin)](https://github.com/coleam00/context-engineering-intro.git):** A starter template and guide emphasizing that context engineering is "10x better than prompt engineering."

### Specialized Tools & Harnesses
- **[Letta Code (Letta AI)](https://github.com/letta-ai/letta-code.git):** A memory-first coding harness built on the Letta API, focusing on persisted agents that learn over time across sessions.
- **[Context-aware Prompt Builder](https://bonigarcia.dev/context-engineering/context-aware-prompt-builder.html):** An interactive tool for designing and comparing structured prompts across frameworks (COSTAR, CRISPE, etc.).
- **[SDLC Prompt Library](https://bonigarcia.dev/context-engineering/sdlc_prompt_library.html):** A curated library of prompts organized around the software development lifecycle roles.
