# Architectural Decision Records (ADR)

<!-- AI_CONTEXT: This directory contains the historical log of significant architectural decisions for the project. Use these to understand the "Why" behind major technical pivots and current system constraints. -->

Architectural Decision Records (ADR) are used to capture significant technical decisions, along with their context and consequences. This provides a transparent history for current and future developers.

---

## 1. ADR Directory Map

### Current Records
- **[001: Initial Workspace Setup](./001-initial-workspace-setup.md):** Establishing the monorepo structure and initial project goals.
- **[002: Architecture Governance](./002-architecture-governance.md):** Defining the "Code of Laws" and enforcement mechanisms.
- **[003: System Architecture](./003-system-architecture.md):** Outlining the core hexagonal architecture and service container logic.

### Framework
- **[ADR Template](./TEMPLATE.md):** The mandatory structure for all new architectural proposals.

---

## 2. ADR Workflow
- **Proposal:** New decisions are drafted using the template.
- **Review:** The "Architectural Mentor" (AI Agent) and Human-in-the-Loop (HITL) review the proposal for architectural integrity.
- **Finalization:** Once approved, the ADR is assigned a number and stored in this directory.
