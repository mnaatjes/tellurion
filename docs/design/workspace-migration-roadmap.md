# Workspace Migration Roadmap: The Modular Pivot

This document outlines the tactical steps to transition the `agents` project from a flat structure into a **Tellurion-based `uv` Workspace**.

## Phase 1: Preparation (The "Clean Slate")
1.  **Deactivate and Delete `.venv`**: Remove the existing virtual environment to prevent path conflicts.
    ```bash
    rm -rf .venv
    ```
2.  **Deprecate `requirements.txt`**: Move the information into the appropriate `pyproject.toml` files (see Phase 2 & 3).
3.  **Prepare the Directory Structure**:
    ```bash
    mkdir -p packages/tellurion-core/src/tellurion_core
    mkdir -p packages/tellurion-pipeline/src/tellurion_pipeline
    ```

## Phase 2: Root Workspace Initialization
1.  **Initialize `uv` Workspace**: Convert the root `pyproject.toml` into a workspace orchestrator.
    ```bash
    uv init --workspace
    ```
2.  **Establish Versioning Baseline**: Create a root `.bumpversion.toml` to manage package versions.
    *   **Refer to**: [Versioning Roadmap](versioning-roadmap.md)
3.  **Update Root `pyproject.toml`**:
    *   Set `name = "tellurion-workspace"`.
    *   Add `[tool.uv.workspace]` with `members = ["packages/*"]`.
    *   **Keep Global Dev Tools**: Move `pytest`, `httpx`, and `rich` to the root's `dev-dependencies` if applicable.

## Phase 3: Bootstrapping "The Stitch" (`tellurion-core`)
1.  **Initialize Core**: Create the library structure.
    ```bash
    cd packages/tellurion-core
    uv init --lib
    ```
2.  **Define Core Dependencies**: `tellurion-core` should be lightweight.
    *   **Add**: `pydantic` (for models/blueprints).
    *   **Avoid**: Do NOT add `llama-index` here.
3.  **Migrate Blueprints**: Move any existing DTOs or model definitions into `packages/tellurion-core/src/tellurion_core/models/`.

## Phase 4: Isolating the Ingestion Engine (`tellurion-pipeline`)
1.  **Initialize Pipeline**:
    ```bash
    cd ../tellurion-pipeline
    uv init --lib
    ```
2.  **Migrate Heavy Dependencies**:
    *   Move `llama-index-core`, `llama-index-readers-file`, `llama-index-embeddings-google`, and `llama-index-vector-stores-chroma` into the `tellurion-pipeline` `pyproject.toml`.
3.  **Link to Core**:
    ```bash
    uv add tellurion-core --workspace
    ```

## Phase 5: Refactoring & Verification
1.  **Update Imports**: Replace all relative imports with absolute package imports:
    *   `from tellurion_core.models import ...`
2.  **Sync Workspace**: Run the global resolution.
    ```bash
    uv sync
    ```
3.  **Run Tests**: Ensure `pytest` still passes across the new boundaries.
    ```bash
    pytest tests/
    ```

## Phase 6: Post-Migration (Evolution)
The workspace is now a modular monorepo. As components stabilize, we will transition to a polyrepo structure.
*   **Refer to:** [Repository Strategy](../explanation/repository-strategy.md)
*   **Refer to:** [Extraction Workflow](monorepo-to-polyrepo-workflow.md)

---
**Status Indicators:**
*   [ ] Phase 1: Preparation
*   [ ] Phase 2: Workspace Init
*   [ ] Phase 3: Core Bootstrap
*   [ ] Phase 4: Pipeline Isolation
*   [ ] Phase 5: Verification
*   [ ] Phase 6: Extraction (Optional/Future)
