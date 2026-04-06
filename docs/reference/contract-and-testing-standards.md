# Reference: Contract and Testing Standards

## 1. Contract-First Development
Contract-First Development is the methodology of defining the "agreement" (the contract) between two services before any functional code is written.

### Key Attributes
*   **Schema Definition:** Uses formal specifications like Pydantic (for Python-to-Python) or OpenAPI (for cross-language).
*   **Parallelism:** Once the contract is set, the `Skill-Manager` and `Skill-Factory` teams can build simultaneously.
*   **Automated Mocking:** The contract allows for "mocking" services during development, enabling early integration tests.
*   **Single Source of Truth:** The contract is stored in a central location (e.g., `gemini-core`) and is the definitive documentation.

---

## 2. Shared Schemas (The "Stitch")
Schemas are the data structures used for inter-service communication, independent of business logic.

### Rules for Schema Design
1.  **The Forward-Compatibility Rule:** Never delete or rename a field. Only add optional fields. This ensures old versions don't break new ones.
2.  **The Primitive Rule:** Favor standard types (ISO 8601 dates, UUIDs, Strings) over custom, complex objects to ensure the schema remains language-agnostic.
3.  **The "No-Nulls" Rule:** Explicitly define whether a field is `Optional` or `Required`. Ambiguous nullability is a leading cause of runtime crashes.
4.  **Strict Versioning:** If a breaking change is required, version the schema (e.g., `/v1/process` to `/v2/process`).
5.  **Descriptive Naming:** Avoid generic names like `data` or `info`. Use `payload_metadata` or `processing_results`.

---

## 3. Testing Strategy
Our testing strategy follows a hybrid approach to ensure both isolation and compatibility.

### Per-Package `tests/` (Isolation)
Each package (e.g., `packages/gemini-pipeline/tests/`) must have its own unit tests.
*   **Goal:** Verifies internal business logic.
*   **Requirement:** When a component moves to its own repo, its tests go with it.

### Root-Level `tests/` (Integration/Contract)
We maintain a global `tests/` directory at the workspace root.
*   **Goal:** Verifies the "Contract" between components (e.g., ensuring `pipeline` output matches `manager` input).
*   **Requirement:** These tests must use the defined schemas to validate cross-package communication.

---

## 4. Repository & Growth Path
As the team and complexity grow, the repository structure evolves.

| Stage | Strategy | Git Setup |
| :--- | :--- | :--- |
| **Startup / MVP** | **Monorepo** | One remote. Everything in `packages/`. |
| **Scaling** | **Split-off** | Move the most stable component (e.g., `pipeline`) to its own remote repo. |
| **Enterprise** | **Polyrepo** | Each component has its own remote; the root becomes an "Orchestration" repo. |

### Growth Rules
*   **Avoid Git Submodules:** Use Python Workspaces for dependency linking. Submodules introduce complexity and "detached HEAD" states.
*   **Strict Import Enforcement:** Use tools (e.g., `ruff`, `import-linter`) to ensure code never crosses package boundaries except through `gemini-core` or defined interfaces.
*   **Independent CI Pipelines:** Configure CI to only run tests for the specific folder that changed.
*   **The Ownership Rule:** Once a package has a dedicated maintainer, it is time to move it to its own Polyrepo to allow for independent tagging and releases.
