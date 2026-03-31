# Agent Scripting and Execution Managers

Scripts represent the "hands" of your agent. Managing them requires a robust bridge between the LLM's intent and your local Linux execution environment, ensuring both security and structured communication.

## 1. Structured Tool Definition

Instead of using standalone or "naked" scripts, use the **Model Context Protocol (MCP) SDK** to define tools that the Gemini CLI can discover and execute reliably.

| Tool | Focus | Use Case |
| :--- | :--- | :--- |
| **MCP SDK (Python/Node)** | Tool Implementation | Provides a structured way to define functions (Tools) with schemas that the LLM can understand and invoke. |
| **MCP Gallery** | Community Servers | A collection of pre-built, official, and community-contributed MCP servers for connecting to services like Google Drive, Slack, GitHub, or Postgres. |

### Diagnostic Command (MCP)
```bash
# Verify that your expert can actually "see" the scripts in its directory and understands the arguments they require.
gemini mcp inspect
```

## 2. Secure Environment Management

Managing agent scripts in a Linux environment requires a strategy for handling sensitive configuration and API credentials without hardcoding them.

- **`chmod`:** Use standard Linux file permissions to control which scripts the agent process can execute.
- **`direnv`:** A highly recommended tool for managing environment variables (like `GITHUB_TOKEN` or `DB_PASSWORD`) on a per-directory basis. This allows agent scripts to access necessary secrets safely as they are loaded into the workspace.

## 3. Execution Best Practices

- **LLM-Friendly Output:** Ensure scripts output clear, concise, and structured success/failure messages. Avoid verbose stack traces that might bloat the context window.
- **Pagination and Truncation:** For tools that produce large outputs, implement pagination or truncation (e.g., "Success: First 50 lines of processed file...") to maintain context window health.
- **Input Validation:** Always validate arguments passed from the LLM within the script itself to prevent command injection or malformed data processing.
