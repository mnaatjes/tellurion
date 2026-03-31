# Glossary of Agent-CLI Concepts

This document defines core concepts related to the operation and management of agent-based command-line interfaces.

## Agent-CLI "Windows"

### How "The Window" Works
When you send a prompt to an LLM, you aren't just sending your latest message. To "remember" what happened previously, the CLI client bundles everything together and sends it as one giant block of text every single time you hit enter.

### The Hard Limit
Every model has a maximum capacity (e.g., 128k tokens for GPT-4o, or 1M+ for Gemini 1.5 Pro). This defines the maximum amount of context (history + current prompt + instructions) that can be processed at once.

### The "Anchor" Strategy
By saying the `GEMINI.md` or System Instruction "stays in the window," it means that as the conversation gets longer and older messages are eventually "pushed out" (deleted) to make room for new ones, the Anchor is programmatically kept at the very top of every request.

### Why "The Window" is a Budget
For developers working in a Linux environment and focusing on ETL, it’s helpful to view the window as a resource buffer:

- **Fixed Cost (The Anchor):** Your core rules and project outline. This might take up 500–1,000 tokens. You pay this "tax" on every turn to ensure the agent doesn't forget its persona.
- **Variable Cost (The Retrieval):** The specific documentation chunks or code snippets you pull in via RAG (Retrieval-Augmented Generation).
- **The Remainder:** What’s left for the actual conversation and the model's "reasoning" space.

## Context Window

Definition: The Context Window is the maximum amount of information (tokens) the LLM can "hold in its head" at a single moment.

In your Gemini CLI, the window is not just your last message; it is the sum of:

System Instructions (Layer 1: The Anchor).

Files you've added (Layer 2: The Working Set).

The current conversation history (Layer 3: Ephemeral).

The outputs of tools (Search results, bash command outputs).

If you exceed this limit, the model "forgets" the earliest parts of the window (usually your initial instructions or project goals) to make room for new text.

## Session Commands

Definition: Session commands are the specific "Slash Commands" (starting with /) or symbols (like ! or @) used to interact with the CLI's internal state without sending that text as a prompt to the LLM.

They are your steering wheel. While a prompt asks the AI to think, a session command tells the CLI to act—like adding a file, checking memory, or wiping the history.

## MCP Server

### Core Definition
An MCP Server is a lightweight program that exposes specific functionalities—such as local file system access, database querying, or API integrations—to an MCP client (in this case, your Gemini CLI). Instead of writing custom "glue code" for every tool, the CLI uses the MCP standard to "ask" the server what it can do and then execute those commands.

### Key Functions
- **Tool Provisioning:** The server tells Gemini which "tools" (functions) are available, such as `list_directory`, `read_file`, or `fetch_url`.
- **Resource Access:** It provides a secure way for the AI to read specific data files or documentation without needing the entire dataset uploaded to the model.
- **Standardized Communication:** It uses JSON-RPC to communicate, meaning you can swap servers or use servers built by the community (e.g., a GitHub MCP server or a Postgres MCP server) regardless of the specific CLI implementation.

### Implementation in Linux
For a developer in a Linux environment, an MCP server usually runs as a persistent background process or is invoked on-demand. Common ways to manage them include:
- **Node.js/npx:** Many servers are distributed via npm and run using npx.
- **Python:** Servers can be built using the MCP Python SDK.
- **Stdio/WebSockets:** The CLI typically communicates with the server through standard input/output (stdio) or via HTTP/WebSockets.

### Why it Matters
Without an MCP server, a CLI is limited to the knowledge contained within the Gemini model's training data. With an MCP server, the CLI can interact with your local environment, query your private databases, and perform actions on your system in real-time.

## Runbook

### Roles of a Runbook
Context Scoping: Its primary role is to define the "active boundary" of the Working Set. By limiting the agent's focus to specific directories (e.g., src/transformers/), it prevents token waste and reduces "hallucinations" caused by irrelevant code.

Workflow Orchestration: It breaks down complex, multi-stage tasks (like an ETL pipeline) into manageable phases. It tells the agent what to prioritize during specific operations like "Synthesis" or "Extraction."

Standardization: It provides a repeatable "recipe" for the agent. This ensures that every time you run a specific pipeline, the agent follows the same logic and utilizes the same reference materials.

### Key Properties
Localization: Runbooks are stored within the .gemini/ directory. This makes them project-specific and allows them to be version-controlled via Git alongside your source code.

Format Versatility: They are typically authored in Markdown (for human-readable instructions) or JSON (for strict, programmatic configuration).

Phase-Specific Constraints: Unlike a general config file, a Runbook is dynamic. It allows for "If-Then" logic regarding file access based on the current phase of development.

Declarative Nature: You don't tell the agent how to code; you tell it what environment to inhabit and which constraints to respect for a specific task.