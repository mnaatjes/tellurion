# System Architecture: Modular Evolution Strategy

## 1. Vision Overview
The Tellurion Framework is designed as a modular ecosystem of specialized agents and engines. To maintain developer velocity while ensuring long-term scalability, the project follows a **Modular Monorepo** pattern, transitioning towards a **Polyrepo** architecture as components stabilize.

### Core Components
| Component | Role | Status |
| :--- | :--- | :--- |
| **`gemini-core`** | Shared DTOs, Blueprints, and Base Interfaces (The "Stitch"). | Planning |
| **`gemini-pipeline`** | The Ingestion engine (Registry-Catalog architecture). | In Development |
| **`gemini-factory`** | The Skill Architect (ETL-based skill generation). | Prototyping |
| **`gemini-manager`** | The Instance/Process Manager (Tmux/Process orchestration). | Prototyping |
| **`gemini-framework`**| The Main Orchestrator / CLI Entry-point. | Planning |

---

## 2. Multi-Repo Strategy Analysis
### The Problem: The "Big Ball of Mud"
In early-stage prototyping, it is tempting to keep all code in a single global namespace. However, as the Ingestion-Pipeline grows, its dependencies (LlamaIndex, heavy data tools) shouldn't bloat the Skill-Manager or the main CLI.

### The Solution: Monorepo-to-Polyrepo Evolution
We employ a **Monorepo-to-Polyrepo** evolution using **Python Workspaces**. This allows us to maintain clean boundaries and independent lifecycles without the friction of managing multiple Git repositories during the highly volatile design phase.

**Why this works:**
*   **Independent Lifecycles:** `gemini-pipeline` can have a rapid release cycle, while `gemini-core` remains stable.
*   **Zero-Friction Refactoring:** Using workspaces allows local "editable" linking, meaning changes in one package are reflected in others instantly.
*   **Ease of Extraction:** When a component is stable, moving it to a standalone repository is a simple `git move` operation.

---

## 3. Evolution Roadmap
1.  **Phase 1: Componentization (Current):** Enforce strict folder boundaries and internal package structures.
2.  **Phase 2: Workspace Integration:** Implement `uv` workspaces to manage internal dependencies as standalone packages.
3.  **Phase 3: Polyrepo Extraction:** Move stable components (starting with `gemini-pipeline`) to dedicated remote repositories.
4.  **Phase 4: Contract-First Orchestration:** Recombine components as external dependencies under a singular framework orchestration.

---

## 4. Development Methodology
*   **Contract-First Development:** Define schemas and interfaces (Pydantic models) before implementation.
*   **Strict Import Enforcement:** Packages may only depend on `gemini-core` or other sibling packages via defined interfaces.
*   **Hybrid Testing:** Per-package unit tests combined with root-level integration "Contract" tests.

---

## 5. Migration Workflow (The Tactical Path)
The following workflow outlines the transition from a single-repo prototype to a modular **`uv` Workspace** architecture.

### Phase 1: Workspace Initialization (The "Shell")
1.  **Initialize the Workspace:** Create a `packages/` directory at the root and initialize the workspace orchestrator using `uv init --workspace`.
2.  **Define Workspace Members:** Update the root `pyproject.toml` to include `tool.uv.workspace` with `members = ["packages/*"]`.

### Phase 2: Building "The Stitch" (`gemini-core`)
1.  **Initialize Core:** Create `packages/gemini-core` and initialize it as a library (`uv init --lib`).
2.  **Migrate Blueprints:** Move existing DTOs/Blueprints into `packages/gemini-core/src/gemini_core/models/`.
3.  **Define Exports:** Ensure the core package exposes these blueprints cleanly via `__init__.py`.

### Phase 3: Isolating the Ingestion Engine (`gemini-pipeline`)
1.  **Initialize Pipeline:** Create `packages/gemini-pipeline` and initialize as a library. Add heavy dependencies (e.g., `llama-index-core`, `google-genai`).
2.  **Establish the "Editable" Link:** Add `gemini-core` as a local, editable dependency to the pipeline package.
3.  **Migrate Logic:** Move the registries, ports, and builder services into the pipeline package.

### Phase 4: Refactoring Imports (The "Cleanup")
1.  **Update Imports:** Refactor all internal code to import Blueprints from `gemini_core` rather than local relative paths.
2.  **Verify Isolation:** Run tests specifically for the pipeline package to ensure no "leaks" from the root or other packages exist.

### Phase 5: Polyrepo Extraction (Finality)
1.  **Git Subtree Split:** When stable, use `git subtree split` to move the package to its own remote repository.
2.  **Remote Dependency:** Update the root `pyproject.toml` to point to the Git URL of the new repository instead of the local path.

---
**Related Documents:**
*   [Monorepo-to-Polyrepo Evolution](../explanation/architecture-evolution.md)
*   [Contract and Testing Standards](../reference/contract-and-testing-standards.md)
