# MCP Configuration Reference

This document provides a technical reference for configuring Model Context Protocol (MCP) servers within Gemini CLI.

## 1. Configuration File Locations

Gemini CLI searches for MCP configuration in two hierarchical locations:

- **Global (User-level):** `~/.gemini/settings.json`
  - Applied across all projects on the system.
- **Local (Project-level):** `./.gemini/settings.json`
  - Applied only to the current project workspace. Settings here override global settings if conflicts occur.

## 2. JSON Configuration Schema

The `mcpServers` object in `settings.json` defines the connected servers. Each server is keyed by a unique name.

### Schema Fields
- **`command`**: The executable to run (e.g., `npx`, `python3`, `node`).
- **`args`**: An array of string arguments passed to the command.
- **`env`**: (Optional) An object containing environment variables required by the server (e.g., API tokens).
- **`disabled`**: (Optional) A boolean to temporarily deactivate the server without removing it.

### Example Configuration
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/my-docs-project"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

## 3. CLI Command Reference

Gemini CLI provides built-in commands to manage MCP servers without manual JSON editing.

| Command | Description |
| :--- | :--- |
| `gemini mcp add <name> <commandOrUrl> [args...]` | Adds a new MCP server configuration. |
| `gemini mcp remove <name>` | Removes an existing MCP server. |
| `gemini mcp list` | Lists all configured and discovered MCP servers. |
| `gemini mcp enable <name>` | Enables a previously disabled MCP server. |
| `gemini mcp disable <name>` | Disables an MCP server. |
| `gemini mcp help` | Displays full command help for MCP management. |
