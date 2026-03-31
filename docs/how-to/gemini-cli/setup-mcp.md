# How-To: Setting Up MCP Servers in Gemini CLI

Follow this guide to connect Model Context Protocol (MCP) servers to your Gemini CLI.

## Prerequisites

- **Gemini CLI installed:** Version 0.35.3 or higher recommended.
- **Node.js/npx:** For many standard MCP servers.
- **Python 3:** Required if you are running custom Python-based servers.

## Method 1: Adding a Server via CLI (Recommended)

The easiest way to add an MCP server is by using the `gemini mcp add` command. This will automatically update your local or global settings.

### Examples

**Add a local Python-based MCP server:**
```bash
gemini mcp add my-local-server python3 /path/to/your/server.py
```

**Add a Filesystem MCP server (using npx):**
```bash
gemini mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /path/to/your/project/docs
```

## Method 2: Manual Configuration via `settings.json`

To set up an MCP server in the Gemini CLI, you primarily work within the `mcpServers` object in your `settings.json` file. In a Linux environment, the global configuration file is typically located at: `~/.gemini/settings.json`.

### 1. The `mcpServers` Object
Each key inside `mcpServers` is a unique name for a server (e.g., "github", "postgres").

#### Required Properties for Local (Stdio) Servers
- **`command`**: The executable used to start the server (e.g., `node`, `python3`, `npx`, `docker`).
- **`args`**: An array of strings representing the arguments passed to the command.

#### Optional Properties
- **`env`**: An object containing environment variables the server needs (like API keys or tokens). Tip: You can use `$VARIABLE` syntax to reference existing shell variables.
- **`cwd`**: The "Current Working Directory" where the command should execute.
- **`timeout`**: Time in milliseconds (e.g., `30000`) before the CLI gives up on a request.
- **`trust`**: A boolean (`true`/`false`). Setting this to `true` often bypasses manual confirmation prompts for that server's tools.

#### Properties for Remote (HTTP/SSE) Servers
- **`httpUrl`**: The endpoint for servers using HTTP streaming.
- **`url`**: The endpoint for servers using Server-Sent Events (SSE).
- **`headers`**: An object for custom HTTP headers (e.g., `{"Authorization": "Bearer $TOKEN"}`).

### 2. The Global `mcp` Object
You can also define a top-level `mcp` object to control the CLI's behavior across all servers:
- **`allowed`**: An array of server names. If this exists, the CLI will only connect to servers listed here.
- **`excluded`**: An array of server names to ignore, even if they are defined in `mcpServers`.

### 3. Full Configuration Example
Here is a sample `settings.json` for a Linux setup using a local Node.js server and a remote HTTP server:

```json
{
  "mcp": {
    "allowed": ["local-files", "github-api"]
  },
  "mcpServers": {
    "local-files": {
      "command": "node",
      "args": ["/path/to/filesystem-server/index.js", "/home/user/documents"],
      "env": {
        "NODE_ENV": "production"
      },
      "trust": true
    },
    "github-api": {
      "httpUrl": "https://api.github.com/mcp",
      "headers": {
        "Authorization": "Bearer $GITHUB_TOKEN"
      },
      "timeout": 60000
    }
  }
}
```

## Method 3: Discovery and Verification

After saving your configuration, verify the status of your servers within the Gemini CLI.

1.  Start the CLI: `gemini`.
2.  Run the **list command**:
    ```
    /mcp list
    ```
    This command will show the status (🟢 Ready / 🔴 Error) of each defined server and list the tools they provide.
3.  Run the **description command** to see what "skills" the server provides:
    ```
    /mcp desc
    ```

## Troubleshooting

- **Empty List:** If `/mcp list` is empty, check the `command` path in `settings.json` and ensure dependencies (like `npx` or `python3`) are in your system PATH.
- **Permission Errors:** For Filesystem MCP, ensure the provided path is absolute and the user running the CLI has read/write permissions for that directory.
- **Environment Variables:** If a server (like GitHub) fails to start, verify that the `env` block in `settings.json` correctly contains any required API tokens.
