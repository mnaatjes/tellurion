# 003. System Architecture (The Five-Package Layout)

**Status:** Accepted  
**Date:** 2026-04-08  
**Deciders:** Michael Naatjes

## Context
The Tellurion project requires a clear separation between foundational logic, heavy data processing, behavioral generation, and user interaction. A flat or loosely coupled structure would lead to "Leaky Abstractions" where LlamaIndex dependencies infect the CLI or core models.

## Decision
We have adopted a **Fixed Five-Package Modular Structure** to isolate concerns:

1.  **`tellurion-core` (The Stitch)**: Contains only Pydantic Blueprints and Interfaces. No heavy logic.
2.  **`tellurion-pipeline` (The Ingestion Engine)**: Dedicated to LlamaIndex and Vector Store management.
3.  **`tellurion-factory` (The Skill Architect)**: Focused on ETL-based generation of agent skills.
4.  **`tellurion-manager` (The Runtime)**: Orchestrating Tmux and OS-level processes.
5.  **`tellurion-framework` (The Skin)**: The CLI entry-point that glues the other four together.

## Consequences
- **Positive:** 
    - **Dependency Isolation:** LlamaIndex (pipeline) or Tmux (manager) dependencies never bloat the `core` or `framework`.
    - **Parallel Development:** Each package can be developed and tested in isolation.
    - **Path to Polyrepo:** Each package is framed for future extraction into its own repository.
- **Negative:** 
    - Complex internal import management (requires absolute package-based imports).
    - Overhead of managing five separate `pyproject.toml` files.
- **Neutral:** 
    - Forces a "Domain-Driven" mindset where all interactions must pass through the `core` blueprints.
