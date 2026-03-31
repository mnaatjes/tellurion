# How-To: Setting Up Runbooks in Gemini CLI

A Runbook is a structured "instruction set" that the Gemini CLI uses to restrict its focus and follow specific procedures. This is particularly useful for complex workflows like ETL pipelines where you need the agent to follow a strict sequence of tasks and avoid distractions from irrelevant files.

## 1. Initializing the Configuration Directory

Ensure you are in the root of your project where you launch the CLI. Create the hidden `.gemini/` directory and a `runbooks/` subdirectory if they don't already exist:

```bash
mkdir -p ./.gemini/runbooks/
```

## 2. Creating the Runbook File

You can use either **Markdown** (best for readability and complex instructions) or **JSON** (best for programmatic strictness). Create a file named after your specific workflow phase, such as `synthesis_runbook.md`.

### Option A: Markdown (Recommended for ETL Workflows)
Markdown allows you to use headers to separate "Scoping" from "Instructions."

```markdown
# Runbook: Synthesis Phase

## Scoping (Working Set Constraints)
- **Primary Source:** `docs/reference/`
- **Logic Source:** `src/transformers/`
- **Output Target:** `src/output/`

## Phase Instructions
1. Analyze the schema definitions in `docs/reference/schema.json`.
2. Apply the transformation logic found in `src/transformers/clean_data.py`.
3. Synthesize a summary report of all mapping errors.

## Constraints
- Do NOT read files from `tests/` or `logs/`.
- Use the `Python` style guide defined in `.gemini/settings.json`.
```

### Option B: JSON (For Strict Agent Configuration)
Use this if you want the CLI to parse the constraints as hard data.

```json
{
  "phase": "Synthesis",
  "working_set": {
    "include": ["docs/reference/**", "src/transformers/**"],
    "exclude": ["**/tests/*", "**/tmp/*"]
  },
  "instructions": "Follow the transformation logic for the ETL pipeline as defined in documentation.",
  "required_tools": ["python_interpreter", "file_reader"]
}
```

## 3. Defining Scoping Logic

The most critical part of the setup is telling the agent exactly where to look. Use glob patterns or explicit paths to prevent the agent from hitting token limits or getting distracted by irrelevant files:

- **Positive Scoping:** `include: ["src/transformers/*.py"]`
- **Negative Scoping:** `exclude: ["node_modules/**", "*.log"]`

> **Tip:** Use absolute paths for scoping if you find that relative paths are causing issues when running the CLI from different subdirectories in a complex ETL pipeline.

## 4. Activation (How to Use It)

Once the file is saved in `./.gemini/runbooks/`, you can activate it in one of two ways:

### Direct Argument
Run the CLI with the `--runbook` flag followed by the path to your runbook:

```bash
gemini --runbook .gemini/runbooks/synthesis_runbook.md "Perform the data mapping."
```

### Contextual Trigger
If your `settings.json` supports command mapping, you can configure a specific alias to automatically pull in a runbook file. For example, typing `gemini synthesis` could be mapped to trigger `.gemini/runbooks/synthesis.md`.

## Summary Checklist for Setup

| Step | Action | Command / File |
| :--- | :--- | :--- |
| **1** | Create the config folder | `mkdir -p .gemini/runbooks/` |
| **2** | Create the Runbook file | `touch .gemini/runbooks/synthesis_runbook.md` |
| **3** | Define the "Working Set" | List your `src/` and `docs/` paths |
| **4** | Add Task logic | Write step-by-step instructions |

## 4. Example

```md
# Runbook: ETL Pipeline - Synthesis Phase

You let the agent know what is what by defining inclusion/exclusion rules and role assignments inside your `.gemini/runbook.md`.

**Defining Roles** in a Markdown Runbook
In a Markdown-based Runbook, you use headers to explicitly define the "Map" of your directory:

```yml
version: "1.0"
name: "ETL Synthesis Phase"

# 1. Core Project (The "Subject") - Permissions: Read/Write
subject:
  description: "Code to be analyzed and modified"
  directories:
    - "src/transformers/"
    - "src/models/"
  allow_mutations: true

# 2. Instruction Sets (The "Manual") - Permissions: Read-Only
manual:
  description: "Operational logic and coding standards"
  files:
    - ".gemini/prompts/synthesis_logic.md"
    - "docs/standards/pep8_guide.md"
  role: "system_instructions"

# 3. Ancillary Information (The "Context") - Permissions: Read-Only
context:
  description: "Background data and API references"
  sources:
    - "docs/reference/elite_dangerous_api.pdf"
    - "metadata/v1_schema_backup.json"
  usage: "reference_only"

# 4. Exclusions (The "Noise") - Permissions: None
noise:
  description: "Directories to ignore for token efficiency"
  exclude:
    - "logs/**"
    - "tests/raw_output/**"
    - "node_modules/**"
    - "*.log"
```

**Key YAML Properties to Note:**

* **Allow_mutations:** true: This tells the agent it has permission to propose code changes or refactors within these specific directories.

* **Role:** "system_instructions": This indicates that the content of these files should be treated as high-priority "rules" rather than just data.

* **Glob Patterns (`**`):** Using logs/** ensures that everything inside that folder is ignored, which is a standard Linux practice for efficiency.

* **Usage:** "reference_only": Explicitly prevents the agent from trying to "fix" your API documentation or legacy JSON files.