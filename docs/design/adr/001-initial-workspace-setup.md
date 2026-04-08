# 001. Initial Workspace Setup

**Status:** Accepted  
**Date:** 2026-04-08  
**Deciders:** Michael Naatjes

## Context
The project began as a flat structure, which posed a risk of "Big Ball of Mud" coupling as the ingestion pipeline (LlamaIndex) and CLI framework grew. We needed a modular architecture that supports:
- **Independent Lifecycles:** Allowing components like `tellurion-core` to remain stable while `tellurion-pipeline` iterates rapidly.
- **Strict Boundaries:** Preventing circular dependencies and ensuring clear responsibilities.
- **AI-Native Governance:** A machine-readable way to enforce architectural standards (Hexagonal, Contract-First) using the Gemini CLI.

## Decision
We have implemented a **Modular Monorepo** using **`uv` Workspaces**. 

### Key Implementation Details:
1.  **Orchestrator Root:** The root `pyproject.toml` acts as a non-package workspace orchestrator (`package = false`).
2.  **Package Structure:** All functional code is isolated in `packages/` (e.g., `tellurion-core`, `tellurion-pipeline`).
3.  **Code of Laws:** Established `.tellurion/rules.yml` as the machine-readable source of truth for architectural constraints.
4.  **Synchronized Versioning:** Used `bump-my-version` to manage versions across the root and all sub-packages simultaneously.
5.  **Tooling:** Adopted `uv` for its high-performance dependency resolution and native workspace support.

## Consequences
- **Positive:** 
    - Clean separation of concerns from day one.
    - Extremely fast dependency resolution and a single shared virtual environment.
    - Architecture is "AI-aware" via the `.tellurion/rules.yml` and `GEMINI.md` directive.
- **Negative:** 
    - Higher initial setup complexity compared to a flat repository.
    - Requires developer discipline to maintain absolute imports and package boundaries.
- **Neutral:** 
    - Shifted to a "Contract-First" workflow, requiring Pydantic models in `core` before implementation.
