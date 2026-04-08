> **Status: COMPLETED / ARCHIVED**
> This document reflects the initial design phase and is preserved for historical context.

# System Architecture: Modular Evolution Strategy

## 1. Vision Overview
The Tellurion Framework is designed as a modular ecosystem of specialized agents and engines. To maintain developer velocity while ensuring long-term scalability, the project follows a **Modular Monorepo** pattern, transitioning towards a **Polyrepo** architecture as components stabilize.

*   **Strategy:** [Repository Strategy](../explanation/repository-strategy.md)
*   **Workflow:** [Monorepo-to-Polyrepo Workflow](monorepo-to-polyrepo-workflow.md)

### Core Components
| Component | Role | Status |
| :--- | :--- | :--- |
| **`tellurion-core`** | Shared DTOs, Blueprints, and Base Interfaces (The "Stitch"). | Planning |
| **`tellurion-pipeline`** | The Ingestion engine (Registry-Catalog architecture). | In Development |
| **`tellurion-factory`** | The Skill Architect (ETL-based skill generation). | Prototyping |
| **`tellurion-manager`** | The Instance/Process Manager (Tmux/Process orchestration). | Prototyping |
| **`tellurion-framework`**| The Main Orchestrator / CLI Entry-point. | Planning |

---

## 2. Multi-Repo Strategy Analysis
### The Problem: The "Big Ball of Mud"
In early-stage prototyping, it is tempting to keep all code in a single global namespace. However, as the Ingestion-Pipeline grows, its dependencies (LlamaIndex, heavy data tools) shouldn't bloat the Skill-Manager or the main CLI.

### The Solution: Monorepo-to-Polyrepo Evolution
We employ a **Monorepo-to-Polyrepo** evolution using **Python Workspaces**. This allows us to maintain clean boundaries and independent lifecycles without the friction of managing multiple Git repositories during the highly volatile design phase.

**Why this works:**
*   **Independent Lifecycles:** `tellurion-pipeline` can have a rapid release cycle, while `tellurion-core` remains stable.
*   **Zero-Friction Refactoring:** Using workspaces allows local "editable" linking, meaning changes in one package are reflected in others instantly.
*   **Ease of Extraction:** When a component is stable, moving it to a standalone repository is a simple `git move` operation.

---

## 3. Evolution Roadmap
1.  **Phase 1: Componentization (Current):** Enforce strict folder boundaries and internal package structures.
2.  **Phase 2: Workspace Integration:** Implement `uv` workspaces to manage internal dependencies as standalone packages.
3.  **Phase 3: Polyrepo Extraction:** Move stable components (starting with `tellurion-pipeline`) to dedicated remote repositories.
4.  **Phase 4: Contract-First Orchestration:** Recombine components as external dependencies under a singular framework orchestration.

---

## 4. Development Methodology
*   **Contract-First Development:** Define schemas and interfaces (Pydantic models) before implementation.
*   **Independent Versioning:** Each component manages its own release cycle and version number.
    *   **Refer to:** [Versioning Roadmap](versioning-roadmap.md)
*   **Strict Import Enforcement:** Packages may only depend on `tellurion-core` or other sibling packages via defined interfaces.
*   **Hybrid Testing:** Per-package unit tests combined with root-level integration "Contract" tests.

---

## 5. Migration Workflow (The Tactical Path)
The transition from a single-repo prototype to a modular **`uv` Workspace** architecture is detailed in the [Workspace Migration Roadmap](workspace-migration-roadmap.md).

### Planned Directory Structure (Framed-out)
```text
tellurion/
├── pyproject.toml              # Workspace Root (Orchestrator)
├── uv.lock                     # Shared Dependency Lockfile
├── .venv/                      # Shared Virtual Environment
├── docs/                       # Global Documentation
├── tests/                      # Integration/Contract Tests
└── packages/
    ├── tellurion-core/         # The "Stitch" (Models & Interfaces)
    │   ├── pyproject.toml
    │   └── src/tellurion_core/
    ├── tellurion-pipeline/     # Ingestion & Data Management
    │   ├── pyproject.toml
    │   └── src/tellurion_pipeline/
    ├── tellurion-factory/      # Skill Generation (ETL)
    │   ├── pyproject.toml
    │   └── src/tellurion_factory/
    ├── tellurion-manager/      # Instance & Process Management
    │   ├── pyproject.toml
    │   └── src/tellurion_manager/
    └── tellurion-framework/    # Main CLI Entry-point
        ├── pyproject.toml
        └── src/tellurion_framework/
```

---
**Related Documents:**
*   [Workspace Migration Roadmap](workspace-migration-roadmap.md)
*   [Monorepo-to-Polyrepo Evolution](../explanation/architecture-evolution.md)
*   [Contract and Testing Standards](../reference/contract-and-testing-standards.md)
