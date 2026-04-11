# Context Hydration Subsystem Prototype

## 0. User Interface and Desired Results

* Form Project Context in Quick and Efficient Format
    - Single Source of Truth
    - Dynamic monitoring
    - Structured and coherent

* Ease of interaction with Agent-CLI
    - Command interface for Agent-CLI OR User?
    - Fulfill requirements of Prompt-Engineering:
        * Find: `Where is "x"?`
        * Explain: `What is "x"?`
        * Test: `Does "x" work?`
        * Debug: `Why is "x" not working?`
        * Deposit: `Take "x" content and place among source.`
        * Review: `Explain "x" within context of source`


* Background Processes
    - Monitor Context
    - Sync Changes to Source


## 1. Major Componenets and Steps

```yml
version: 1.0.0

components:
    source_knowledge: "massive library of code and docs"
    context_payload: "curated data"
        attributes:
            - Portable
            - Small
        

layers_of_hydration:
    structural_metadata: 
        # Domain and Scope
        properties:
            - Directory Structures
            - Manifests
        # Map-Makers: These provide directory and symbol indexes to show the agent where items are located
        tooling:
            - ls-R
            - ctags
            - pyclbr
    architectural_guardrails:
        properties:
            - ADRs
            - Project Rules
        # Diagnostic Indexers: Act as "guardrails" by enforcing organizational rules and security standards.
        tooling:
            - pylint
            - pip-audit
    semantic_summaries:
        properties:
            - Module maps
            - Symbol Tables
            - Pydantic Blueprints
            - API Awareness (without reading implementation details)
        # State Monitors & Indexers: Ssummarize dependencies, relationships, and environment state without revealing implementation.
        tooling:
            - uv
            - pylint
    just_in_time_retrieval: "Surgical read of specific file implementation only when area of interest identified"
        properties:
            - Surgical Reads
            - Research
        # Semantic Brain: Enable surgical, intent-based retrieval of specific code implementation snippets.
        tooling:
            - Vector DB
            - RAG
```


## 2. Tooling


### 2.1 Diagnostic Indexers


#### 2.1.1 `pylint`
* *Code Health Check* parses Abstract Syntax Tree (AST) and checks health base on project laws
    - looks for specific config files: 
        * `.pylintrc` or `pylintrc` most common
        * `[tool.pylint]` in the `pyproject.toml` file
        * `setup.cfg` or `tox.ini` older pakcaging/testing files
        * Environmental variables, specifically the `$PYLINTRC` variable
        * Default hard-coded et of rules shipped with `pylint`
    - Example rules"
        * `Variables must contain at least 3 characters`
        * `No more than 4 arguments per function`
    - `pylint` generates a report result on configuration alignment of code
    - Static Analysis Tool: Deterministic. does NOT require an embed_model or LLM
    - Can have heirarchical definitions of `pylintrc` files; e.g. `src/core/pylintrc` and `src/pylintrc`
    - Example `.pylintrc`:

    ```toml
    [MASTER]
    # Ignore the infrastructure/migrations folders to focus on core logic
    ignore=migrations,tests,venv

    [MESSAGES CONTROL]
    # Disable 'too-many-instance-attributes' for Adapters, but keep for Core
    # Note: In a professional setup, you'd override this in specific sub-directories
    disable=
        C0114, # missing-module-docstring (often noise in small scripts)
        W0511, # fixme (allow TODOs during development)

    [DESIGN]
    # --- API & INTERFACE STANDARDS ---
    # Enforce clean signatures: No more than 5 arguments per function
    max-args=5

    # Prevent "Fat Interfaces": Limit public methods on a class
    max-public-methods=10

    # Keep implementations lean: Maximum 15 local variables per function
    max-locals=15

    # Boolean "Trap" prevention: Max 2 boolean positional arguments
    max-bool-args=2

    [BASIC]
    # --- HEXAGONAL NAMING CONVENTIONS ---
    # Force "Ports" to be identifiable as Interfaces/Abstract Base Classes
    # This regex requires classes in 'core/ports' (if using per-dir config) 
    # or all abstract-looking classes to end in 'Port' or 'Repository'.
    class-rgx=[A-Z][a-z0-9]+(Port|Repository|Service|Adapter)$

    # Enforce clean variable names (Minimum 3 chars, except for common loops)
    variable-rgx=[a-z_][a-z0-9_]{2,30}$
    good-names=i,j,k,ex,Run,_

    [REPORTS]
    # Output a score (e.g., 8.5/10) to use as a "Quality Gate" in your CLI
    output-format=colorized
    score=yes
    ```

* CLI Technical Reference: 
```bash
# For a standard RC file
pylint --generate-rcfile > master_config.pylintrc

# For the modern TOML format
pylint --generate-toml-config > master_config.toml
```

* (View Technical Reference)[https://pylint.readthedocs.io/en/latest/user_guide/checkers/features.html]


---


#### 2.1.2 `pip-audit`

* *Dependency Guard* scans linux environment packages for known package/dependency issues or bugs
