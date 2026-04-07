# How-To: Updating Versions

This guide explains how to increment the version of a package within the Tellurion workspace. We use `bump-my-version` to ensure consistency and automate Git tagging.

## 1. Prerequisites
Ensure you have `bump-my-version` installed. It's usually part of your root `dev-dependencies`.
```bash
uv pip install bump-my-version
```

## 2. Choosing the Right Increment
We follow Semantic Versioning (SemVer):
*   **Patch (`patch`):** Bug fixes or small, backward-compatible updates. (e.g., `0.1.0` -> `0.1.1`)
*   **Minor (`minor`):** New features that are backward-compatible. (e.g., `0.1.1` -> `0.2.0`)
*   **Major (`major`):** Breaking changes or large architectural shifts. (e.g., `0.2.0` -> `1.0.0`)

## 3. Updating a Package Version

To update a specific package (e.g., `tellurion-core`), run the command from the root of the workspace.

### Increment the Patch
```bash
bump-my-version bump patch --package tellurion-core
```

### Increment the Minor
```bash
bump-my-version bump minor --package tellurion-core
```

## 4. What Happens Automatically?
1.  **File Update:** The `version = "..."` string in `packages/tellurion-core/pyproject.toml` is updated.
2.  **Git Commit:** A commit is created with a message like `bump: tellurion-core version 0.1.0 -> 0.1.1`.
3.  **Git Tag:** A scoped tag is created: `tellurion-core@v0.1.1`.

## 5. Pushing Changes
Always push both your commits and your tags to the remote repository.
```bash
git push origin main --tags
```

## 6. Verification
Confirm the version has been updated correctly.
```bash
cat packages/tellurion-core/pyproject.toml | grep version
```

---
**Troubleshooting:**
*   **Dry Run:** To see what will happen without actually making changes, add the `--dry-run` and `--verbose` flags.
    ```bash
    bump-my-version bump patch --package tellurion-core --dry-run --verbose
    ```
*   **Untracked Files:** Ensure all your changes are committed before bumping. `bump-my-version` will refuse to run on a "dirty" working directory.
