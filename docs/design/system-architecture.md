# System Architecture: Modular Evolution

The Tellurion Framework is designed as a modular ecosystem of specialized agents and engines. This architecture follows a **Modular Monorepo** pattern, ensuring clean boundaries, independent package lifecycles, and a clear path toward potential polyrepo extraction.

## 1. Directory Structure

```text
tellurion/
├── pyproject.toml              # Workspace Root (Orchestrator)
├── uv.lock                     # Shared Dependency Lockfile
├── .venv/                      # Shared Virtual Environment
├── docs/                       # Global Documentation
├── tests/                      # Integration & Unit Tests
└── packages/
    ├── tellurion-core/         # The "Stitch" (Common Models & Interfaces)
    │   ├── pyproject.toml
    │   └── src/tellurion_core/
    ├── tellurion-pipeline/     # Ingestion & Data Management (LlamaIndex)
    │   ├── pyproject.toml
    │   └── src/tellurion_pipeline/
    ├── tellurion-factory/      # Skill Generation (ETL-based Architecture)
    │   ├── pyproject.toml
    │   └── src/tellurion_factory/
    ├── tellurion-manager/      # Instance & Process Management (Tmux/Process)
    │   ├── pyproject.toml
    │   └── src/tellurion_manager/
    └── tellurion-framework/    # Main CLI Entry-point (The "Skin")
        ├── pyproject.toml
        └── src/tellurion_framework/
```

## 2. Core Components

| Component | Responsibility | Current Phase |
| :--- | :--- | :--- |
| **`tellurion-core`** | Shared DTOs, Pydantic Blueprints, and Base Interfaces. | **Phase 3: Bootstrapping** |
| **`tellurion-pipeline`** | Data ingestion, Vector Store management, and ETL logic. | **Phase 4: Development** |
| **`tellurion-factory`** | The Skill Architect (generating agents and their behaviors). | **Phase 1: Scaffolding** |
| **`tellurion-manager`** | Orchestrating runtime processes and instance lifecycle. | **Phase 1: Scaffolding** |
| **`tellurion-framework`** | CLI user interface and cross-package orchestration. | **Phase 1: Scaffolding** |

## 3. Key Standards & Protocols
- **Versioning:** Synchronized via `bump-my-version` at the root.
- **Dependency Management:** Handled by `uv` Workspaces with a shared lockfile.
- **Contract-First:** Interfaces and models are defined in `tellurion-core` before implementation.

## 4. Related Documentation
- [Workspace Migration Roadmap](workspace-migration-roadmap.md)
- [Monorepo-to-Polyrepo Workflow](monorepo-to-polyrepo-workflow.md)
- [Versioning Baseline (Archived)](archive/versioning-roadmap-20260408.md)
- [Original Architecture (Archived)](archive/system-architecture-20260408.md)
