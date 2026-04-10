# The Source Tree: Defining Workspace Scope

The **Source Tree** (often used interchangeably with "Working Tree" or "Working Directory") is the visible collection of folders and files on your local storage that constitute your active project.

While a Repository (the `.git` folder) is a compressed database of every change history, the Source Tree is the **checkout**—the specific version of those files currently being edited and observed by the agent.

---

## 1. Definition and Hierarchy
The Source Tree is the hierarchical arrangement of source code, configuration files, and assets that make up a software project. It "branches" out from a single **Project Root** into various subdirectories and files.

## 2. Professional Scope
In a professional workflow, the scope of the source tree includes everything necessary to build, test, and run the application, but it specifically excludes environmental noise.

- **Included:** Source code, build scripts (`pyproject.toml`, `Makefile`), documentation (`README.md`), and local configuration templates.
- **Excluded:** Version control metadata (the `.git` directory), compiled binaries (e.g., `__pycache__`), and external dependencies (e.g., `node_modules`, `venv`).

By excluding junk data, the Agent CLI remains focused and doesn't waste tokens on irrelevant "distractions."

---

## 3. Professional Example: Python ETL Framework
This high-legibility structure is specifically designed to be **token-efficient** for an Agent CLI.

```plaintext
my_etl_project/              <-- Project Root (The "Base" of the tree)
├── GEMINI.md                <-- Context State: Current progress and AI instructions
├── ARCHITECTURE.md          <-- Blueprint: Rules for the Agent CLI
├── pyproject.toml           <-- Build State: Dependencies and metadata
├── src/                     <-- The "Meat": Actual implementation logic
│   ├── __init__.py          <-- Map: Defines package exports for the agent
│   ├── extractor.py         <-- Module: Data ingestion logic
│   └── transformer.py       <-- Module: Data cleaning logic
├── tests/                   <-- Validation State: Unit and integration tests
├── logs/                    <-- Observability: Where the Agent looks for run errors
└── .gitignore               <-- Scope Control: Tells the Agent what to ignore
```

### Why this matters for the Agentic Workflow
- **The Root:** When you run `gemini` in `my_etl_project/`, the Agent CLI treats this root as its **"Home"** environment.
- **The Branches:** By observing the `src/` and `tests/` branches, the agent can logically conclude that a module like `extractor.py` has a corresponding test, implying a certain level of stability.
- **The Leaves:** If the agent sees an error entry in the `logs/error.log` leaf, it can immediately identify the current **State** of the last run without requiring manual explanation.
