# Tooling Reference Summary

This document provides a categorized overview of the tools and frameworks available for building, managing, and optimizing agents within the Gemini CLI ecosystem.

## 1. Agent Configuration & Scaffolding
Tools for defining personas, configuring hyperparameters, and initializing skill structures.

| Tool | Description | Reference File |
| :--- | :--- | :--- |
| **Interactive Scaffolder** | CLI wizard (`gemini skill create`) for initializing new expert skills. | [agent-configuration-tools.md](tooling/agent-configuration-tools.md) |
| **Skill Editor** | Specialized UI-lite editor (`gemini skill edit`) for tuning agent configurations. | [agent-configuration-tools.md](tooling/agent-configuration-tools.md) |
| **JSON Schema** | IDE-level validation for `config.json` to ensure parameter accuracy. | [agent-configuration-tools.md](tooling/agent-configuration-tools.md) |
| **Fabric Patterns** | A library of proven expert personas for diverse technical tasks. | [agent-configuration-tools.md](tooling/agent-configuration-tools.md) |
| **LangChain Hub** | Repository of prompt blueprints and complex chain-of-thought patterns. | [agent-configuration-tools.md](tooling/agent-configuration-tools.md) |

## 2. Reference Material Optimization (Data Digestion)
Tools for transforming large, messy documentation into high-signal context for agents.

| Tool | Description | Reference File |
| :--- | :--- | :--- |
| **Fabric** | Synthesis engine using the `extract_wisdom` pattern to condense long texts. | [agent-reference-optimizers.md](tooling/agent-reference-optimizers.md) |
| **LlamaIndex** | Framework for knowledge structuring and creating searchable vector indices. | [agent-reference-optimizers.md](tooling/agent-reference-optimizers.md) |
| **Unstructured.io** | Python library for cleaning and transforming PDFs/HTML into clean Markdown. | [agent-reference-optimizers.md](tooling/agent-reference-optimizers.md) |
| **GPT-Index** | Tool for creating high-level summaries of vast documentation sets. | [data-ingestion-utilities.md](tooling/data-ingestion-utilities.md) |

## 3. Script & Execution Management
Tools for managing the "hands" of the agent and securing the execution environment.

| Tool | Description | Reference File |
| :--- | :--- | :--- |
| **MCP SDK** | Structured framework for defining tools that agents can discover and call. | [agent-script-managers.md](tooling/agent-script-managers.md) |
| **MCP Gallery** | Collection of pre-built servers for connecting to external APIs and services. | [agent-script-managers.md](tooling/agent-script-managers.md) |
| **`direnv`** | Linux utility for managing per-directory environment variables and secrets. | [agent-script-managers.md](tooling/agent-script-managers.md) |
| **`chmod`** | Standard Linux permissions for controlling script execution security. | [agent-script-managers.md](tooling/agent-script-managers.md) |

## 4. Context Window & Observability
Tools for monitoring token usage, tracing thought processes, and managing cost.

| Tool | Description | Reference File |
| :--- | :--- | :--- |
| **LangSmith** | The industry standard for tracing LLM turns and identifying context bloat. | [context-window-monitors.md](tooling/context-window-monitors.md) |
| **Arize Phoenix** | Open-source, local observability platform for tracing thinking processes. | [context-window-monitors.md](tooling/context-window-monitors.md) |
| **LiteLLM** | Universal proxy for tracking costs and token counts across different providers. | [context-window-monitors.md](tooling/context-window-monitors.md) |
| **Tiktoken** | Low-level library for precise token counting before prompt submission. | [context-window-monitors.md](tooling/context-window-monitors.md) |

## 5. Knowledge Graph Tooling
Tools for managing structured relationships and hierarchical system memory.

| Tool | Description | Reference File |
| :--- | :--- | :--- |
| **Neo4j Suite** | Comprehensive set of MCP servers for modeling, querying, and monitoring graphs. | [knowledge-graph-tools.md](tooling/knowledge-graph-tools.md) |
| **Graphiti** | Temporal knowledge graph tool for tracking system changes over time. | [knowledge-graph-tools.md](tooling/knowledge-graph-tools.md) |
| **TrustGraph** | Ontology management tool for enforcing the logical rules of a knowledge graph. | [knowledge-graph-tools.md](tooling/knowledge-graph-tools.md) |

## 6. Multi-Agent Orchestration
Frameworks for coordinating multiple specialized experts to achieve complex goals.

| Tool | Description | Reference File |
| :--- | :--- | :--- |
| **CAO (Kay-Oh)** | Open-source orchestrator for managing multiple Gemini CLI instances in tmux. | [client-agent-orchestrators.md](tooling/client-agent-orchestrators.md) |
| **Supervisor Skill** | Built-in orchestration skill for managing sub-processes within Gemini CLI. | [client-agent-orchestrators.md](tooling/client-agent-orchestrators.md) |
| **LangGraph** | Tool for building stateful, multi-actor applications with cyclical logic. | [client-agent-orchestrators.md](tooling/client-agent-orchestrators.md) |
| **CrewAI** | Role-playing orchestrator for autonomous, specialized AI agents. | [client-agent-orchestrators.md](tooling/client-agent-orchestrators.md) |
| **Microsoft AutoGen** | Framework for conversational task-solving between multiple agents. | [multi-agent-orchestrators.md](tooling/multi-agent-orchestrators.md) |
| **Google Generative AI SDK** | Native Python SDK for direct Gemini model interaction. | [google-specific-developer-tools.md](tooling/google-specific-developer-tools.md) |
| **Vertex AI Agent Builder** | Enterprise-grade platform for deploying managed AI agents. | [google-specific-developer-tools.md](tooling/google-specific-developer-tools.md) |

## 7. Interfaces, Protocols & Routing
Standardized communication and routing layers for agents.

| Tool | Description | Reference File |
| :--- | :--- | :--- |
| **Agent Protocol** | Open API specification for interoperability between agent backends. | [specialized-agent-interfaces.md](tooling/specialized-agent-interfaces.md) |
| **RouteLLM** | Framework for optimized model routing to minimize token expense. | [client-agent-orchestrators.md](tooling/client-agent-orchestrators.md) |
| **OpenDevin / Devin** | Advanced autonomous engineering agents for complex terminal tasks. | [specialized-agent-interfaces.md](tooling/specialized-agent-interfaces.md) |
| **llm (Simon Willison)** | Extensible CLI utility for persona-based LLM interaction. | [cli-native-utilities.md](tooling/cli-native-utilities.md) |
| **Aider** | Terminal-based pair programming assistant with deep file-system awareness. | [cli-native-utilities.md](tooling/cli-native-utilities.md) |
