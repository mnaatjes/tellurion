# Repository Strategy: The Evolution of Tellurion

The Tellurion project employs a **Modular Monorepo** strategy that evolves into a **Polyrepo** architecture. This approach balances initial development speed with long-term scalability and component reusability.

## 1. The Modular Monorepo (Current Phase)
During the early and middle phases of development, all components live within a single Git repository. We use **Python Workspaces (`uv`)** to enforce boundaries.

### Why this works:
*   **Atomic Refactoring:** You can change a model in `tellurion-core` and update its usage in `tellurion-pipeline` in a single Git commit.
*   **Simplified CI/CD:** A single pipeline can test the entire ecosystem, ensuring no cross-package regressions.
*   **Low Overhead:** No need to manage multiple sets of credentials, issue trackers, or pull requests across different repositories.

## 2. Transition Milestones (The "Trigger")
We don't move to a Polyrepo just because it's "cleaner." We wait for specific **Milestones** to trigger an extraction:

| Milestone | Description | Trigger |
| :--- | :--- | :--- |
| **Interface Stability** | The component's API (defined in `tellurion-core`) hasn't had a breaking change in 3+ months. | Architectural Maturity |
| **External Demand** | A separate project needs to use `tellurion-pipeline` without pulling in the entire Tellurion framework. | External Reusability |
| **Dependency Heavyweight** | The component's dependencies (e.g., LlamaIndex, heavy ML libraries) are slowing down the CI/CD for the rest of the project. | CI/CD Performance |
| **Team Scaling** | Different developers or teams need independent control over release cycles and access permissions. | Organizational Scale |

## 3. The Evolution: Monorepo-to-Polyrepo
When a milestone is met, the component is "extracted."

### Identity & Visibility
The transition from `agents` (private) to `Tellurion` (public) is a key milestone in our strategy.
*   **Renaming:** Renaming the GitHub repository to `tellurion` signals the transition from a prototype to a framework.
*   **Public Visibility:** Making the repository public is a commitment to standard software practices (CI/CD, proper documentation, versioning) and facilitates its use as a dependency.

### Git & GitHub Implications
*   **Before Extraction:** One repository (`tellurion.git`), one set of branches, one history.
*   **During Extraction:** We use `git subtree split` to "carve out" the folder's history into a new repository.
*   **After Extraction:**
    *   The component gets its own GitHub repository (e.g., `tellurion-pipeline.git`).
    *   The main Tellurion repository deletes the local folder and updates its `pyproject.toml` to point to the new remote URL.
    *   **Import paths do NOT change:** Because we used the `src/<package_name>` layout, `import tellurion_pipeline` remains valid whether the code is local or remote.

---
**Related Documents:**
*   [Monorepo-to-Polyrepo Workflow](../design/monorepo-to-polyrepo-workflow.md)
*   [Workspace Migration Roadmap](../design/workspace-migration-roadmap.md)
*   [System Architecture](../design/system-architecture.md)
