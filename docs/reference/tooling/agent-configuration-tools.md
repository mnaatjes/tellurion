# Agent Configuration and Definition Tools

These tools are designed to streamline the creation, tuning, and management of "Expert Agents" (Skills) within the Gemini CLI environment. They ensure metadata consistency and prevent common configuration errors.

## 1. Built-in CLI Scaffolding

Using the built-in scaffolding tools is the recommended way to initialize and manage skills, as it enforces the required directory structure and schema.

| Tool | Command | Purpose |
| :--- | :--- | :--- |
| **Interactive Scaffolder** | `gemini skill create <name>` | Launches a wizard to define the agent's persona, temperature, and required tools. Generates the `./.gemini/skills/<name>/` directory automatically. |
| **Skill Editor** | `gemini skill edit <name>` | Opens a specialized UI-lite editor to tune configuration parameters (e.g., `config.json`) without risk of syntax errors. |

## 2. IDE Integration and Validation

For developers working directly with configuration files, leveraging IDE features can significantly improve the accuracy of agent definitions.

- **JSON Schema Validation:** By associating a JSON schema with your skill's configuration files (like `config.json`), editors like **VS Code** or **Cursor** provide:
  - **Autocomplete:** Suggestions for properties like `temperature`, `topP`, and `maxOutputTokens`.
  - **Type Checking:** Instant warnings for invalid data types or out-of-range values.
  - **Documentation:** Inline descriptions of what each parameter controls.

## 3. Proven Pattern Libraries

Instead of defining personas from scratch, you can adapt blueprints from established prompt engineering communities:

- **Fabric Patterns:** A library of proven "Expert Personas" for coding, summarizing, and complex logic extraction.
- **LangChain Hub:** A repository of "Prompt Blueprints" and complex "Chains of Thought" that can be adapted into the `SKILL.md` instructions.
## 4. Context Management Tools

To implement the **Context Engineering** strategies described in `docs/explanation/context_engineering/`, developers utilize specialized infrastructure and utilities.

| Tool | Category | Key Use Case |
| :--- | :--- | :--- |
| **AWS Bedrock AgentCore** | Managed Context Infrastructure | Provides built-in session context management, source attribution, and long-term memory. |
| **AWS Bedrock Knowledge Base** | Managed RAG Pipeline | Handles ingestion, chunking, and retrieval logic, exposing it to the agent via a single endpoint. |
| **mem0** | Memory Layer | A tool for extracting facts and preferences from conversations and committing them to long-term episodic memory. |
| **MinHash** | Context Deduplication | An algorithm used to identify and strip out redundant information before it enters the context window. |
| **AgentCore Gateway** | Tool Management Proxy | Acts as a centralized proxy for tool ecosystems, supporting semantic search to load only relevant tools. |
