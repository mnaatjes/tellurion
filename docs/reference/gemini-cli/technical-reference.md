# Gemini CLI v0.35.3 Technical Reference

This document provides a technical specification summary and identity information for Gemini CLI v0.35.3.

## 1. Technical Specification Summary

Gemini CLI is the official command-line interface for Google's Gemini models, designed for high-performance tool-enabled development and workflow automation.

| Component | Description |
| :--- | :--- |
| **Architecture** | **`packages/cli`**: A flicker-free TUI with sticky headers and mouse support.<br>**`packages/core`**: Orchestration layer for API communication (Gemini 3), tool management, and session state. |
| **Model Routing** | **Intelligent Steering**: Automatically delegates tasks between Gemini Flash and Gemini Pro to optimize speed and cost. |
| **Core Workflows** | **Plan Mode (`/plan`)**: Structured task decomposition with persistent progress tracking.<br>**Agent Skills**: Modular automation for specialized tasks. |
| **Connectivity** | **MCP Support**: Full integration with the Model Context Protocol (stdio/HTTP).<br>**A2A**: Secure Agent-to-Agent communication via HTTP/OAuth2. |
| **Security** | **Sandboxing**: Execution of shell commands via **gVisor (runsc)** or **LXC**.<br>**Policy Engine**: TOML-based fine-grained control over tool execution. |
| **Context** | **Hierarchical Context**: Automated discovery of `GEMINI.md` files; context compression for history management. |

### Schema Highlights
- **Runtime:** Node.js (`@google/gemini-cli`)
- **Security:** "Folder Trust" mechanism and environment sanitization.
- **Telemetry:** OpenTelemetry-compliant metrics for token usage and performance tracking.

---

## 2. Identity and Discovery

### API Layer: `GET /v1/models`
Gemini CLI does **not** expose a local HTTP API or an OpenAI-compatible `/v1/models` endpoint. It is primarily a terminal-based interface and programmatic CLI. Model routing logic is internal and not exposed as a discoverable service for other clients.

### Agent Layer: Model Context Protocol (MCP)
Gemini CLI operates as an **MCP Client**, not a server. It can connect to external MCP servers (via stdio or HTTP) to discover and use their tools, but it does not currently have a "handshake" mode where another agent can query it for capabilities.

### CLI Layer: Configuration Metadata
The CLI uses a hierarchical discovery system for **`GEMINI.md`** files, which act as project-level metadata. These files can contain:
- **Tech stack and style guides** for the project.
- **Custom instructions** for CLI behavior in a specific repository.
- **Skill or Hook definitions** that extend core functionality.

---

## 3. Probing the CLI

To programmatically identify the CLI and its capabilities:
- **Version Check:** Run `gemini --version` (currently `0.35.3`).
- **Machine-Readable Output:** Use `gemini --prompt "identify yourself" --output-format json` for structured responses.
- **Help Documentation:** Use `gemini --help` to list available commands and options.
