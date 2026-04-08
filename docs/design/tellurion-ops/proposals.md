# Proposal: tellurion-ops

The `tellurion-ops` package is an internal utility designed to automate project governance, maintain documentation sync, and provide a "Project Health" dashboard.

## 1. Objectives
- **Automate the Sync**: Programmatically update `system-architecture.md` when `.tellurion/rules.yml` or ADRs change.
- **Project Health**: Validate that all packages have the same version, all ADRs follow the template, and no forbidden imports exist.
- **Workflow Shortcuts**: Provide high-level commands (e.g., `uv run update`) that chain multiple lower-level operations.

## 2. Functional Domains

### A. The Synchronizer
- **Input**: `.tellurion/rules.yml`, `docs/design/adr/*.md`
- **Logic**: Parses YAML and Markdown frontmatter.
- **Output**: Re-generates tables and sections in `docs/design/system-architecture.md`.

### B. The Auditor
- **Logic**: Scans `packages/*/pyproject.toml` to ensure version parity.
- **Logic**: Checks for the existence of `src/` and `tests/` in each package.
- **Output**: Terminal report (using `rich`).

### C. The Version Wrapper
- **Logic**: Wraps `bump-my-version` to ensure a `CHANGELOG.md` entry is present before allowing a bump.

### D. The Context Manager
- **Input**: `.tellurion/state/*.yml`
- **Logic**: Automates the "Snapshot" process by archiving current state into `docs/reports/status/`.
- **Output**: Generates formatted Markdown reports from high-density YAML state.

## 3. Future "Dog-Fooding"
This package will eventually be refactored to use `tellurion-core` blueprints, serving as the first functional "test case" for the Tellurion Framework's ingestion and management logic.
