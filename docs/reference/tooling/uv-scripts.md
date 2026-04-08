# Reference: uv Scripts Tooling

`uv` Scripts are a powerful mechanism to define, run, and manage project-specific commands within a `uv` workspace.

## 1. What are uv Scripts?
Unlike traditional `npm` or `poetry` scripts, `uv` scripts allow you to define high-level commands in your root `pyproject.toml` that run with the full context of the workspace's virtual environment.

### Why Use Them?
- **Unified Interface**: Run `uv run <command>` from any directory in the monorepo.
- **Dependency Aware**: Scripts can specify dependencies (like `rich` or `click`) that are automatically resolved before execution.
- **Portability**: They ensure every developer uses the same command-line flags and environments.

## 2. Implementation Context
In the Tellurion project, `uv` scripts serve as the **User Interface for the Governance Engine**.

### Example Configuration:
```toml
[tool.uv.scripts]
update = "python -m tellurion_ops.sync --all"
sync-docs = "python -m tellurion_ops.sync --docs"
status = "python -m tellurion_ops.audit --report"
```

## 3. Mentor's Recommendations
For this project, I recommend the following implementation standards:

1.  **Chaining**: Use `uv` scripts to chain multiple commands (e.g., `update` should run `bump-my-version` AND `sync-docs`).
2.  **Verbose Output**: Ensure all scripts use a tool like `rich` to provide a clean, color-coded status report in the terminal.
3.  **Fail-Fast**: Scripts should exit with a non-zero status if any part of the synchronization fails, preventing the "drift" of information.
