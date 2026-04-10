# Context Engineering Tools and Methodologies

This document provides a categorized list of specialized tools, frameworks, and workflows designed to optimize context management for AI agents.

---

## 1. Context-Aware Design Tools

| Tool | Category | Key Use Case |
| :--- | :--- | :--- |
| **Context-Aware Prompt Builder** | Structured Prompt Design | Building, comparing, and reusing structured prompts across frameworks (COSTAR, CRISPE, etc.). |
| **SDLC Prompt Library** | Reference Library | Curated prompts organized by SDLC role (Architect, Developer, Debugger, etc.). |
| **Product Requirements Prompt (PRP)** | Methodology | Comprehensive implementation blueprints for AI assistants, generating from `INITIAL.md` feature requests. |

## 2. Memory-First Harnesses and Frameworks

| Tool | Category | Key Use Case |
| :--- | :--- | :--- |
| **Letta Code** | Agent Harness | A memory-first coding harness built on the Letta API for long-lived, learning agents. |
| **Letta API** | Backend Service | Standardizes agent memory persistence and skill learning across model providers. |
| **Claude Code** | Agent Harness | An agentic CLI from Anthropic that utilizes sub-agent isolation and context compaction. |
| **Gemini CLI** | Agent Harness | A tool-using CLI from Google optimized for large-context models (1M+ tokens). |

## 3. Specialized MCP and RAG Extensions

| Tool | Category | Key Use Case |
| :--- | :--- | :--- |
| **AgentCore Gateway** | MCP Integration | Centralized proxy for tool ecosystems, supporting semantic tool search for lean context. |
| **Agentic RAG** | Retrieval Pattern | A paradigm combining RAG with autonomous agents for multi-step reasoning and dynamic data retrieval. |
| **Contextual Retrieval** | Retrieval Pattern | A method by Anthropic that enriches document chunks with context before embedding to improve RAG accuracy. |

---

## 4. Context Management Frameworks (Prompting)

- **COSTAR:** Context, Objective, Style, Tone, Audience, Response.
- **CRISPE:** Capacity, Role, Insight, Statement, Personality, Experiment.
- **RTF:** Role, Task, Format.
- **10-step Framework:** A structured, multi-step process for generating highly precise instructions.
