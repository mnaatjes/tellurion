# 002. Architecture Governance (The Code of Laws)

**Status:** Accepted  
**Date:** 2026-04-08  
**Deciders:** Michael Naatjes

## Context
As the Tellurion project scales, maintaining architectural integrity across multiple packages becomes difficult, especially when using AI assistance. We needed a system that:
- **Enforces Standards:** Ensuring Hexagonal and Contract-First principles are followed.
- **AI-Alignment:** Providing a machine-readable source of truth that the Gemini CLI can reference.
- **Synchronized Documentation:** Preventing drift between the actual rules, the AI's behavior, and the human-readable docs.

## Decision
We have implemented a **Three-Tier Governance System** (The "Code of Laws"):

1.  **The Machine Law (`.tellurion/rules.yml`)**: A structured YAML file containing foundational principles, package boundaries, and communication protocols.
2.  **The Enforcer (`GEMINI.md`)**: A root-level directive that commands the AI to prioritize the `.tellurion/rules.yml` over all other suggestions.
3.  **The Reflection (`docs/design/system-architecture.md`)**: A human-readable markdown file that mirrors the rules in a verbose format.

### Enforcement Workflow:
- Any architectural change must follow a strict order: Update Rule -> Update Reflection -> Update AI Mandate (if needed).

## Consequences
- **Positive:** 
    - Prevents architectural drift during AI-assisted development.
    - Provides a single, versioned source of truth for all project constraints.
    - Lowers the cognitive load for the developer by outsourcing boundary checking to the AI.
- **Negative:** 
    - Adds a layer of documentation "overhead" for every structural change.
    - Requires constant syncing between the YAML and the Markdown documentation.
- **Neutral:** 
    - The project is now "Self-Documenting" from an architectural standpoint.
