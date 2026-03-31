# How-To: Defining Expert Agents (Skills)

Expert Agents, also known as **Skills**, are modular extensions that provide Gemini CLI with specialized workflows, domain expertise, and tool integrations. This guide covers the two primary ways to define and configure these agents.

## Method 1: The Interactive Scaffold (Recommended)

The easiest way to create an expert agent is using the built-in scaffolding tool. This method ensures that your directory structure and metadata are correctly formatted from the start.

### 1. Initialize the Skill
Run the `create` command with a unique name for your expert (e.g., `bigquery-architect`):

```bash
gemini skill create bigquery-architect
```

### 2. Configure the Persona
The CLI will launch an **Interactive Wizard** that asks for the following:
- **Expert Persona:** A one-sentence summary of the agent's role (e.g., "A senior data engineer specializing in BigQuery schema optimization").
- **Temperature:** Set the model's creativity (e.g., `0.1` for precision-focused architects, `0.7` for creative brainstorming).
- **Required Tools:** Select which local tools the expert needs access to (e.g., `file_reader`, `shell_executor`, `mcp_client`).

### 3. Tuning the Configuration
If you need to adjust these settings later without manually editing files, use the specialized editor:

```bash
gemini skill edit bigquery-architect
```
This command opens a UI-lite editor to tune the `config.json` and other metadata parameters safely.

---

## Method 2: Manual Definition (Explicit)

For advanced users who prefer full control, you can create the skill directory and its required files manually.

### 1. Create the Directory Structure
Create a new folder for your skill within the project's local `.gemini/` directory:

```bash
mkdir -p ./.gemini/skills/bigquery-architect/
```

### 2. Define the Metadata and Instructions (`SKILL.md`)
The core of every skill is the `SKILL.md` file. This file uses **YAML frontmatter** for metadata and **Markdown** for procedural instructions.

**Example `SKILL.md`:**
```markdown
---
name: bigquery-architect
description: Senior BigQuery expert. Use when schema design, SQL optimization, or partition strategies are needed.
---

# BigQuery Architect Role

## Core Objectives
1. Always prioritize **Clustering** and **Partitioning** for tables over 1GB.
2. Use **Standard SQL** syntax exclusively.
3. Validate all schemas against the project's `docs/reference/schema.json`.

## Procedural Workflows
- **Step 1:** Analyze the source data structure.
- **Step 2:** Generate the DDL statement.
- **Step 3:** Perform a dry-run cost estimation.
```

### 3. Adding Bundled Resources (Optional)
You can further specialize your agent by adding subdirectories within the skill folder:
- **`scripts/`**: Deterministic scripts (Node/Python/Bash) for repetitive tasks.
- **`references/`**: Static documentation (e.g., `api_docs.md`) that the agent can read as needed.
- **`assets/`**: Templates or boilerplate files (e.g., `bigquery_template.sql`).

## Summary Checklist

| Action | Command / Location |
| :--- | :--- |
| **Interactive Setup** | `gemini skill create <name>` |
| **Manual Setup** | `./.gemini/skills/<name>/SKILL.md` |
| **Tuning Config** | `gemini skill edit <name>` |
| **Activation** | Use `/skills reload` in an active session to enable changes. |
