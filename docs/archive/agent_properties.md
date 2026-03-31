# Gemini CLI Agent and Skill Properties

This document outlines the accepted, encouraged, and allowed properties for defining Subagents, Agent Skills, and Custom Commands in Gemini CLI.

## 1. Subagents
Subagents are specialized experts defined in `.md` files (e.g., `~/.gemini/agents/my-agent.md`) with YAML frontmatter.

| Property | Status | Description |
| :--- | :--- | :--- |
| `name` | **Required** | A unique identifier (slug) used as the tool name for delegation. |
| `description` | **Required** | **Highly Encouraged.** A clear explanation of what the agent does. This is the "trigger" the primary agent uses to decide when to call this expert. |
| `tools` | **Allowed** | A list of tool names the subagent can use (e.g., `["read_file", "run_shell_command"]`). |
| `max_turns` | **Allowed** | Limits the number of turns the subagent can take (default: 15). |
| `model` | **Allowed** | Specifies a particular AI model (defaults to `inherit` from the primary agent). |
| `kind` | **Allowed** | Defines if the agent is `local` (default) or `remote`. |
| `temperature` | **Allowed** | Controls the model's creativity/randomness (0.0 to 2.0). |
| `timeout_mins` | **Allowed** | Sets a time limit for the subagent's execution (default: 5). |

## 2. Agent Skills
Skills provide on-demand expertise and are defined in a `SKILL.md` file within a dedicated directory (e.g., `~/.gemini/skills/my-skill/SKILL.md`).

| Property | Status | Description |
| :--- | :--- | :--- |
| `name` | **Required** | The unique name of the skill (should match the directory name). |
| `description` | **Required** | **Highly Encouraged.** A detailed description of the expertise. The primary agent uses this to know when to `activate_skill`. |
| `version` | **Allowed** | Used for tracking updates and compatibility of the skill. |

## 3. Custom Commands
Commands are prompt or shell shortcuts defined in `.toml` files (e.g., `~/.gemini/commands/deploy.toml`).

| Property | Status | Description |
| :--- | :--- | :--- |
| `description` | **Required** | Explains what the command does when the user types `/help`. |
| `args` | **Allowed** | Defines expected arguments for the command. |
| `env` | **Allowed** | Sets specific environment variables for the command's execution. |

---

### Critical Field: `description`
The **`description`** property is the most important field for both Subagents and Skills. It serves as the primary mechanism for discovery. If the description is vague, the primary agent may not recognize when to delegate a task to the specialized expert or activate the relevant skill.

## 4. Storage and Configuration

To be recognized by Gemini CLI, subagents and skills **must** be stored in specific `.gemini/` directories. They cannot be placed in arbitrary project folders.

### Storage Locations
| Type | Path | Usage |
| :--- | :--- | :--- |
| **Project-Level** | `.gemini/agents/*.md` | Specific to the current workspace/repository. |
| **User-Level** | `~/.gemini/agents/*.md` | Global for the current user across all projects. |

### Configuration Requirement
Custom agents are currently an experimental feature. You must enable them in your `settings.json` file:

```json
{
  "experimental": {
    "enableAgents": true
  }
}
```

### Example Project Structure
If you are working in `/srv/agents/`, your custom agents should be organized as follows:

```text
/srv/agents/
├── .gemini/
│   ├── agents/
│   │   └── your-persona.md
│   └── skills/
│       └── your-skill/
│           └── SKILL.md
└── docs/
    └── agent_properties.md
```
