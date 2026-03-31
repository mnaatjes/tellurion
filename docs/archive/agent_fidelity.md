# Agent Fidelity and Interaction

Fidelity in the context of Gemini CLI agents refers to the depth of their specialization, the breadth of their tool access, and the strictness of their operational boundaries.

## Levels of Agent Fidelity

| Fidelity Level | Characteristics | Interaction Model |
| :--- | :--- | :--- |
| **Low (Command)** | Stateless, simple text expansion or shell execution. | Invoked via `/command_name`. |
| **Medium (Skill)** | Context-aware, procedural, can be "activated" to change behavior. | Activated via `activate_skill`. Provides expert guidance for the current session. |
| **High (Subagent)** | Fully autonomous "persona" with dedicated system prompts, specific tools, and independent turn management. | Delegated to via tool call. Operates in a sub-loop until the goal is achieved. |

## Interaction Mechanisms

### 1. Automatic Delegation
The primary agent (Gemini CLI) monitors your requests. If a request matches the `description` of a defined **Subagent**, the primary agent will automatically delegate the task.
*   **Example:** If you have a `database-expert` subagent, and you ask about SQL optimization, the primary agent invokes the subagent tool.

### 2. Manual Activation
**Skills** are typically activated when the primary agent recognizes a task that benefits from specialized knowledge.
*   The primary agent calls `activate_skill(name="skill-name")`.
*   The instructions from `SKILL.md` are then injected into the context, guiding all subsequent actions.

### 3. Direct Command Execution
**Custom Commands** are triggered explicitly by the user.
*   User types `/deploy --env=prod`.
*   The CLI processes the TOML definition and executes the defined prompt or shell script.

## Core Interaction Principles

*   **Surgical Updates:** High-fidelity agents are designed to make precise, idiomatic changes rather than broad, destructive edits.
*   **Research-First:** Agents are programmed to investigate (using `grep`, `ls`, `read_file`) before proposing or executing a strategy.
*   **Validation Loop:** Interaction isn't complete until the agent verifies its work (e.g., running tests, linting, or checking build status).
*   **Transparency:** Every interaction includes a brief explanation of intent before tool execution to keep the user informed.
