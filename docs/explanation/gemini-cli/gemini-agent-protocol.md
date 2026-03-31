# Gemini CLI Agent Protocol & Schema

The **Gemini CLI Agent Protocol** refers to the standardized schema defined in the **Agent Development Kit (ADK)** and the **Interactions API**. These schemas define the contract between your terminal environment and the Gemini model, ensuring that specialized agents (Skills) can maintain state, plan actions, and produce structured, type-safe output.

---

## 1. Core Schema: Identity and Instructions

Every agent skill is defined by an identity and a set of instructions that the model uses to determine its behavior and activation criteria.

- **`name`:** A unique identifier for the expert (e.g., `BigQueryExpert`).
- **`description`:** A high-level purpose summary. This is critical for "Router" agents to decide which expert should handle a specific query.
- **`instructions` (System Prompt):** The behavioral core. This string defines the agent's persona, constraints, and standard operating procedures.
  - **Variable Injection:** Use the `{var}` syntax to inject dynamic values from session states or external files.

---

## 2. Input/Output Schemas (Type Safety)

To enable reliable CLI automation and scripting, the protocol supports JSON schemas for predictable data exchange.

- **`input_schema`:** Defines the expected structure of the user message. If set, the agent expects a JSON string instead of raw text.
- **`output_schema`:** Defines the desired structure of the agent's final response. This allows Python scripts to parse the agent's "synthesis" directly as a dictionary or object.

---

## 3. Persistent State and Artifacts

This layer manages the "memory" of the agent within your project directory, ensuring that context is maintained efficiently.

- **`state`:** A key-value store that persists across turns. Reference these variables in prompts using `{state_key}`.
- **`artifacts`:** Specialized state variables for large bodies of text (documentation, code snippets).
  - **Token Efficiency:** Instead of re-sending entire documents, the agent points to a specific **Artifact ID** (referenced as `{artifact.name}`), keeping the context window focused.

---

## 4. Planner Configuration (Reasoning Logic)

The **Planner** defines the internal "thinking" logic of the agent, allowing for different levels of transparency and rigor.

- **`BuiltInPlanner`:** Uses the model's native "thinking" features (Gemini 2.0/3.0+).
  - **`thinking_budget`:** Maximum number of internal reasoning tokens allowed before responding.
  - **`include_thoughts`:** Boolean to determine if the raw internal reasoning is printed to the terminal.
- **`PlanReActPlanner`:** Forces a structured **Plan -> Action -> Reasoning -> Final Answer** loop. Best for complex technical troubleshooting where step-by-step transparency is required.

---

## 5. Tool and Skill Definitions (The "Hands")

This property represents the array of function declarations (tools) the agent can call to interact with your filesystem or external APIs.

- **`name`:** The function identifier (e.g., `list_directory`).
- **`description`:** Detailed guidance on when the agent should use this tool.
- **`parameters`:** A JSON Schema of the arguments the tool requires.

---

## 6. CLI-Native Management Properties

These properties, typically found in a `config.json` or `.geminirc`, are used to tune the agent session for maximum performance and cost-efficiency.

| Property | Description |
| :--- | :--- |
| **`maxSessionTurns`** | Maximum history length before the agent begins "summarizing" old turns to save tokens. |
| **`summarizeToolOutput`** | Instructs the CLI to use a smaller model (e.g., Gemini Flash) to synthesize large tool outputs before passing them to the main agent. |
| **`compressionThreshold`** | The percentage of context window utilization that triggers automatic history compression. |

### Why This Matters
By defining a strict **`output_schema`**, you ensure that your Python synthesis scripts receive clean, structured data for your ETL pipeline. By utilizing **Artifacts**, you ensure that the Gemini CLI only "looks" at the documentation when it is explicitly referenced in the current task, significantly reducing your daily token expenditure.
