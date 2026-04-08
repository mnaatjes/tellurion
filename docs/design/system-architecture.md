# System Architecture

The Tellurion Framework is a modular ecosystem of specialized agents and engines. This architecture follows a **Modular Monorepo** pattern, governed by strict package boundaries and the **"Code of Laws"** defined in `.tellurion/rules.yml`.

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
    ├── tellurion-pipeline/     # Ingestion & Data Management (LlamaIndex)
    ├── tellurion-factory/      # Skill Generation (ETL-based Architecture)
    ├── tellurion-manager/      # Instance & Process Management (Tmux/Process)
    └── tellurion-framework/    # Main CLI Entry-point (The "Skin")
```

## 2. Foundational Principles

These are the primary directives that govern all development within the project:

- **Contract-First Development**: All data structures and interfaces must be defined in `tellurion-core` before implementation.
- **Hexagonal Architecture**: Business logic is isolated from external adapters. Engines (like `tellurion-pipeline`) are adapters for the core domain.
- **Modular Monorepo**: Cross-package imports are strictly limited to the `core` package to prevent circular dependencies.

## 3. Package Governance & Responsibilities

| Package | Responsibility | Dependencies | Enforcement |
| :--- | :--- | :--- | :--- |
| **`tellurion-core`** | **Stitch**: Shared DTOs, Pydantic Blueprints, and Base Interfaces. | None | Strictly domain-only structure. |
| **`tellurion-pipeline`** | **Ingestion**: Adapting LlamaIndex to the Tellurion Domain. | `tellurion-core` | Focused on data and vector management. |
| **`tellurion-framework`** | **Skin**: CLI entry-point and orchestrator. | Any (*) | Logic-lite "glue" code only. |
| **`tellurion-factory`** | **Skill Architect**: Generating agent behaviors via ETL. | `tellurion-core` | Specialized in manufacturing skills. |
| **`tellurion-manager`** | **Runtime**: Process and instance orchestration. | `tellurion-core` | Managing Tmux/Process lifecycles. |

## 4. Communication Protocols

- **Blueprint-First**: All package-to-package communication MUST occur through Pydantic Blueprints defined in `tellurion-core`.
- **Abstraction**: Direct access to external systems (DB, filesystem) must be abstracted through a Blueprint-aware interface.

## 5. Related Documentation
- [Workspace Migration Roadmap](workspace-migration-roadmap.md)
- [Monorepo-to-Polyrepo Workflow](monorepo-to-polyrepo-workflow.md)
- [ADR Workflows](../how-to/adr-workflows.md)
- [Original Architecture (Archived)](archive/system-architecture-20260408.md)
