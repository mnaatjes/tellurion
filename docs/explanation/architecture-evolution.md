# Explanation: Monorepo-to-Polyrepo Evolution

## 1. The Strategy: "The Strangler Fig" Evolution
In the early phase of project growth, we utilize the **Modular Monorepo** approach. This allows for high developer velocity while maintaining clean architectural boundaries.

### The Stages of Extraction
1.  **Componentization:** Strictly enforce folder boundaries. Treat internal folders as if they were external libraries, preventing "spaghetti" imports.
2.  **Workspace Implementation:** Introduce a workspace manager (like **uv** or **Poetry**) to manage these folders as independent packages while they still live in one repo.
3.  **The Extraction:** One by one, the most stable or independent components (e.g., the `Ingestion-Pipeline`) are moved to their own dedicated Git repositories.
4.  **Dependency Linking:** The original project pulls the extracted component as a remote dependency (via Git URL or private PyPI) rather than a local path.

---

## 2. Python Workspaces
Python Workspaces allow us to manage a collection of related packages within a single environment. This is the core engine of our modular development strategy.

### Technical Mechanics
*   **Shared Virtual Environment:** Instead of each sub-project having its own `venv`, the workspace creates one "mega-environment" that contains all dependencies for all sub-packages.
*   **Local Cross-Pollination:** If the `Skill-Manager` depends on the `Skill-Factory`, the workspace tool marks the Factory as an **editable install**. Editing code in the Factory folder instantly updates the Manager’s behavior without requiring a re-install.
*   **Dependency Resolution:** The workspace tool calculates a single "solve" for all packages. This ensures all components use compatible versions of shared libraries (e.g., `pydantic`, `requests`), preventing runtime conflicts.

### Recommended Tooling
*   **uv:** Currently the fastest and most modern choice for Linux/Python workspaces.
*   **Poetry:** Uses "Multiproject" plugins or native workspace features to handle local path dependencies.

---

## 3. Benefits Comparison
| Feature | Standard Polyrepo | Monorepo w/ Workspaces |
| :--- | :--- | :--- |
| **Isolation** | High | High |
| **Refactoring** | Hard (requires versioning/re-installs) | Easy (local linking) |
| **Dev Velocity** | Slow (due to dependency overhead) | Fast (optimized linking) |
| **Deployment** | Independent | Independent |

---
**Next Steps:**
*   Review [Contract and Testing Standards](../reference/contract-and-testing-standards.md) for rules on inter-package communication.
