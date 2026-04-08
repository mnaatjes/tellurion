# Project Backlog: The Roadmap to Tellurion

This document tracks the long-term vision and major milestones for the Tellurion Framework.

## Phase 3: The Stitch (Core Implementation)
- Define standard schemas for Agents, Skills, and Data Sources.
- Establish the `BaseAgent` and `BaseSkill` abstract interfaces.

## Phase 4: The Engine (Pipeline Implementation)
- Port the LlamaIndex prototype into a modular, blueprint-aware ingestion engine.
- Implement the "Registry-Catalog" pattern for data management.

## Phase 5: The Skill Architect (Factory Implementation)
- Implement ETL-based skill generation.
- Allow agents to "learn" new behaviors by ingesting documentation.

## Phase 6: The Runtime (Manager Implementation)
- Orchestrate agent lifecycles via Tmux and OS-level processes.
- Implement an instance-based management system.

## Phase 7: The Skin (Framework Implementation)
- Build the unified CLI experience.
- Provide high-level "Quick Start" templates for end-users.

## Phase 8: Extraction (Polyrepo Transition)
- Evaluate each package for stability.
- Move stable packages to standalone repositories.
