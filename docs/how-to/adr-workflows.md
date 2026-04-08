# Architecture Decision Record (ADR) Workflows

This document outlines the mandatory procedures for making, documenting, and enforcing architectural decisions within the Tellurion project.

## 1. The Decision Workflow

Whenever a change to the architecture is proposed (e.g., adding a new package, changing a communication protocol, or adopting a new pattern), we must follow this sequence:

1.  **Modify the Law (`.tellurion/rules.yml`)**: Update the machine-readable rules to reflect the new state.
2.  **Update the Reflection (`docs/design/system-architecture.md`)**: Update the human-readable documentation to explain the change.
3.  **GEMINI.md Persistence**: The root `GEMINI.md` remains static unless the *way* the AI interacts with the law needs to change.

## 2. Creating and Tracking ADRs

All significant architectural decisions must be recorded in `docs/design/adr/`.

### Steps to create a new ADR:
1.  **Draft**: Create a new file in `docs/design/adr/` using the format `NNN-title-of-decision.md`.
2.  **Numbering**: Ensure the number is sequential (e.g., `001`, `002`).
3.  **Status**: Mark the status as `Proposed` initially.
4.  **Review**: Discuss the proposal. Once agreed upon, update the status to `Accepted`.
5.  **Superseding**: If a later ADR replaces an old one, update the old ADR's status to `Superseded` and link to the new one.

## 3. Enforcement
- **AI Enforcement**: The `GEMINI.md` file directs the AI to always check `.tellurion/rules.yml`.
- **Programmatic Enforcement**: Use `import-linter` and `Ruff` as described in `docs/reference/architecture/linter-rules.md`.
