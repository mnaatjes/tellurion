# Workflow: Monorepo-to-Polyrepo Extraction

This workflow describes the technical steps to extract a stable workspace package into its own standalone repository.

## 1. Prerequisites
*   The package (e.g., `tellurion-pipeline`) must be in its own directory within `packages/`.
*   The package must have its own `pyproject.toml` and a passing test suite.
*   You must have an empty GitHub repository created for the new package.

## 2. Step 1: Isolation Check
Ensure the package only depends on `tellurion-core` or external libraries. It **must not** have hidden dependencies on other sibling packages.
```bash
# Verify no other internal packages are imported
grep -r "import tellurion_factory" packages/tellurion-pipeline
```

## 3. Step 2: Extracting History
We use `git subtree` to split the package's folder into a new branch containing only its history.

```bash
# Create a temporary branch with the package's history
git subtree split --prefix=packages/tellurion-pipeline -b extraction-branch
```

## 4. Step 3: Pushing to the New Remote
1.  **Initialize the New Remote:**
    ```bash
    git remote add pipeline-remote https://github.com/mnaatjes/tellurion-pipeline.git
    ```
2.  **Push the Branch:**
    ```bash
    git push pipeline-remote extraction-branch:main
    ```

## 5. Step 4: Updating the Monorepo (The "Strangler")
Now that the package is remote, we remove the local folder and update the workspace root to point to the new URL.

1.  **Delete Local Folder:**
    ```bash
    git rm -r packages/tellurion-pipeline
    git commit -m "refactor: extracted tellurion-pipeline to standalone repository"
    ```
2.  **Update Root `pyproject.toml`:**
    Change the dependency from a local workspace path to a Git URL.
    ```toml
    # packages/tellurion-framework/pyproject.toml
    [project]
    dependencies = [
        "tellurion-pipeline @ git+https://github.com/mnaatjes/tellurion-pipeline.git"
    ]
    ```
3.  **Sync the Workspace:**
    ```bash
    uv sync
    ```

## 6. Post-Extraction Maintenance
*   **Version Control:** The new repository now uses its own `.bumpversion.toml`.
*   **CI/CD:** Set up a GitHub Action in the new repository to run its tests independently.
*   **PR Workflow:** Changes to `tellurion-pipeline` now happen via PRs in its own repository.

---
**Related Documents:**
*   [Repository Strategy: The Evolution of Tellurion](../explanation/repository-strategy.md)
*   [Versioning Roadmap](versioning-roadmap.md)
*   [System Architecture](system-architecture.md)
