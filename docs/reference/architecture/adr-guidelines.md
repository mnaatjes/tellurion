# Architecture Decision Records (ADR)

An Architecture Decision Record (ADR) is a document that captures an important architectural decision made along with its context and consequences.

## Why use ADRs?
- **Avoid "Architectural Archaeology":** Explains the "why" behind a decision months after it was made.
- **Onboarding:** Helps new developers understand the current state of the system.
- **Alignment:** Ensures the team agrees on the technical direction.

## The Nygard Template
We use the standard Nygard format for all Tellurion ADRs.

### [Number]. [Title]
**Status:** [Proposed | Accepted | Superseded]  
**Date:** YYYY-MM-DD  
**Deciders:** [List of names]

### Context
What is the problem we are solving? What are the constraints and technical limitations?

### Decision
What is the chosen solution? Be specific about technologies, patterns, or processes.

### Consequences
- **Positive:** What do we gain?
- **Negative:** What are the trade-offs or technical debt?
- **Neutral:** What changes in our environment?

## ADR Storage
ADRs should be stored in `docs/design/adr/` and numbered sequentially (e.g., `0001-initial-workspace-setup.md`).
