# Architectural Linter Rules

To ensure that the "Code of Laws" defined in `.tellurion/rules.yml` is not just a suggestion, we use programmatic linting to enforce boundaries.

## 1. Import Linter
`import-linter` is used to enforce high-level structural rules (Layers and Independence).

### Example Contract (Layers)
Enforces a one-way flow of dependencies.
```toml
[[tool.importlinter.contracts]]
name = "Core Isolation"
type = "layers"
layers = [
    "tellurion_framework",
    "tellurion_pipeline",
    "tellurion_core"
]
```

### Example Contract (Independence)
Ensures two packages never depend on each other.
```toml
[[tool.importlinter.contracts]]
name = "Package Independence"
type = "independence"
modules = [
    "tellurion_pipeline",
    "tellurion_factory"
]
```

## 2. Ruff (Boundary Enforcement)
Ruff provides fast, file-level enforcement for monorepos.

### Banning Relative Imports
In a modular monorepo, relative imports across package boundaries (e.g., `from ..core import ...`) are forbidden. They must be absolute.
```toml
[tool.ruff.lint.flake8-tidy-imports]
ban-relative-imports = "all"
```

### Import Sorting
Ensures that first-party (internal) packages are grouped together for visibility.
```toml
[tool.ruff.lint.isort]
known-first-party = ["tellurion_core", "tellurion_pipeline"]
```

## Implementation Strategy
- **Ruff:** Run on every save and in pre-commit hooks for speed.
- **Import Linter:** Run in CI (GitHub Actions) to catch structural violations before they are merged.
