# Python Workspaces with `uv`

A **Workspace** is a collection of Python packages (projects) that are managed as a single unit. It is the core engine behind the "Modular Monorepo" strategy, allowing you to develop multiple independent libraries while maintaining a shared development environment.

## 1. What is a `uv` Workspace?
`uv` is a high-performance Python package manager that uses a workspace model to handle complex multi-package projects.

### Key Characteristics
*   **Single Lockfile:** All packages in the workspace share a single `uv.lock` file at the root. This guarantees version consistency across the entire project.
*   **Shared Virtual Environment:** A single `.venv` is created at the root, containing the union of all dependencies for all member packages.
*   **Editable Linking:** Member packages can depend on each other via "local paths." `uv` treats these as editable installs, meaning changes in a dependency are reflected instantly in the consumer.
*   **Dependency Isolation:** Each sub-package maintains its own `pyproject.toml`, ensuring it only "knows" about the specific libraries it needs to function.

---

## 2. The Relationship: Workspace vs. `.venv`

In a standard Python project, the `.venv` lives inside the project folder. In a **Workspace**, the relationship is hierarchical:

```text
tellurion-project/
├── pyproject.toml      # The "Workspace Root"
├── uv.lock             # The "Master Lockfile"
├── .venv/              # The "Shared Environment" (Contains ALL deps)
└── packages/
    ├── tellurion-core/
    │   └── pyproject.toml
    └── tellurion-pipeline/
        └── pyproject.toml
```

### Why this matters:
1.  **Disk Efficiency:** You don't have five different copies of `pydantic` or `llama-index` taking up space in five different virtual environments.
2.  **Global Resolution:** `uv` resolves all dependencies at once. If `core` needs `pydantic>=2.0` and `pipeline` needs `pydantic<2.5`, `uv` finds a version that satisfies both.
3.  **Cross-Package Testing:** When you run tests from the root, the `.venv` has access to every package, allowing for seamless integration testing.

---

## 3. Example Implementation

### Root `pyproject.toml`
The root file defines the workspace boundaries but usually contains no source code itself.

```toml
[project]
name = "tellurion-workspace"
version = "0.1.0"
description = "Modular orchestrator for specialized agents"
dependencies = [] # Root dependencies (optional)

[tool.uv.workspace]
members = ["packages/*"]
```

### Member `pyproject.toml` (`tellurion-pipeline`)
The member package defines its own metadata and points to other workspace members as dependencies.

```toml
[project]
name = "tellurion-pipeline"
version = "0.1.0"
dependencies = [
    "llama-index-core>=0.10.0",
    "tellurion-core", # This refers to a sibling package
]

[tool.uv.sources]
tellurion-core = { workspace = true } # Tells uv to look in the workspace members
```

---

## 4. Example Workflow

### Step 1: Initialization
Initialize the root as a workspace.
```bash
uv init --workspace
```

### Step 2: Adding a Member
Create a new library inside the `packages/` directory.
```bash
mkdir -p packages/tellurion-core
cd packages/tellurion-core
uv init --lib
```

### Step 3: Linking Packages
Add `tellurion-core` as a dependency to `tellurion-pipeline`.
```bash
cd ../tellurion-pipeline
uv add tellurion-core --workspace
```

### Step 4: Development Cycle
1.  Modify a model in `packages/tellurion-core/src/tellurion_core/models.py`.
2.  Immediately run a script in `tellurion-pipeline` that imports that model.
3.  The change is live **without** needing a reinstall or a build step.

### Step 5: Syncing
Ensure the global `.venv` and `uv.lock` are up to date after any changes to a `pyproject.toml`.
```bash
uv sync
```

---
**Related Documents:**
*   [System Architecture: Modular Evolution Strategy](../../design/system-architecture.md)
*   [CLI Native Utilities](cli-native-utilities.md)
