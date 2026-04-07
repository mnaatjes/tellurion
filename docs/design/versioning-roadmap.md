# Versioning Roadmap: Independent & Synchronized

In a **Modular Monorepo**, we must balance the need for independent component lifecycles with the clarity of a unified project. This document defines how we manage versions across the Tellurion ecosystem.

## 1. The Strategy: Independent Versioning
Each package in the `packages/` directory maintains its own version number. This allows `tellurion-core` to remain stable (v1.0.0) while `tellurion-pipeline` iterates rapidly (v0.5.0 -> v0.6.0).

*   **Single Source of Truth:** The `version` field in each package's `pyproject.toml` is the absolute authority.
*   **Git Tagging:** We use "Scoped Tags" in Git to distinguish between package releases (e.g., `tellurion-core@v1.0.0` vs `tellurion-pipeline@v0.5.0`).

## 2. Tooling: `bump-my-version`
We will use `bump-my-version` (the modern, maintained successor to `bumpversion`) to automate the incrementing of versions across files.

### Why `bump-my-version`?
*   It can update multiple files at once (e.g., `pyproject.toml` and a `__init__.py`).
*   It handles Git commits and tags automatically.
*   It supports complex versioning schemas (SemVer).

## 3. Configuration Plan
A `.bumpversion.toml` file will be placed at the root, containing configurations for each package.

```toml
[tool.bumpversion]
current_version = "0.1.0" # This acts as a global placeholder or for the framework itself
parse = "(?P<major>\\d+)\\.(?P<minor>\\d+)\\.(?P<patch>\\d+)"
serialize = ["{major}.{minor}.{patch}"]

# Example package override
[[tool.bumpversion.files]]
filename = "packages/tellurion-core/pyproject.toml"
search = 'version = "{current_version}"'
replace = 'version = "{new_version}"'
```

## 4. Transition to Polyrepo
When a package is extracted into its own repository:
1.  The Git history is split.
2.  The package keeps its current version number.
3.  The `.bumpversion.toml` is moved into the new repository and simplified to only track that package.

---
**Related Documents:**
*   [How-To: Updating Versions](../how-to/updating-versions.md)
*   [Workspace Migration Roadmap](workspace-migration-roadmap.md)
