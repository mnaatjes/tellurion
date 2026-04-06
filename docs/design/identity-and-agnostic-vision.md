# Identity and Agnostic Vision

## 1. Vision Summary
The framework is evolving from a specialized tool into an **agnostic orchestration ecosystem**. The core value proposition is providing a high-level "Stitch" between disparate data sources and expert agents, regardless of the underlying LLM or ingestion engine.

### Core Principles
*   **Model Agnosticism:** Interaction with any Model-CLI or Embedding provider.
*   **Engine Agnosticism:** The ability to swap LlamaIndex for other frameworks (e.g., LangChain, Haystack) or custom native engines.
*   **Contract-First Orchestration:** The "Skill Factory" and "Skill Manager" operate on stable internal schemas rather than external library types.

---

## 2. Branding Exploration
To reflect this agnostic vision, the project requires a name that implies structure, connectivity, and creation without being tied to a specific provider.

| Name | Theme | Rationale |
| :--- | :--- | :--- |
| **Lattice** | Structure | Implies a scalable, interconnected grid of skills and data. |
| **Synapse** | Communication | Focuses on the "Stitch" and the signal flow between agents. |
| **Nexus** | Central Point | Positions the framework as the central hub for disparate tools. |
| **Aperture** | Vision/Entry | Suggests a clean opening/interface into project data. |
| **Prism** | Refraction | Takes raw data and "refracts" it into specialized expert agents. |
| **Foundry** | Creation | Highlights the "Skill Factory" aspect—a place where experts are built. |
| **Vortex** | Centripetal | Implies pulling in data (ingestion) and spinning out agents. |
| **Bridge** | Connectivity | Explicitly addresses the goal of "Stitching" together different tools. |

---

## 3. Design Impact Analysis (Agnosticism)
Achieving full agnosticism requires the following architectural adjustments:

### A. Abstract Base Classes (ABCs) for Engines
*   **Change:** Introduce an `EngineAdapter` interface.
*   **Impact:** The Pipeline will call an abstract `BaseEngine`. Implementations like `LlamaIndexAdapter` will handle the library-specific logic.

### B. Purity of Blueprints (DTOs)
*   **Change:** Remove all external library references (e.g., `llama_index.core`) from DTOs.
*   **Impact:** Blueprints must use Python primitives or internal DTOs. Translation to engine-specific objects occurs only within the `Executor`.

### C. Adapter Pattern for Registries
*   **Change:** Registries (Readers, Parsers) will store "Metadata Definitions" rather than library instances.
*   **Impact:** The `Registrar` will maintain a mapping layer to resolve aliases to engine-specific components at runtime.

### D. Universal Translator (The Core)
*   **Change:** The `core` package defines the **Standard Agent Protocol**.
*   **Impact:** Any model or framework plugged into the system must adhere to these internal schemas, ensuring seamless interoperability.

### E. Standalone Synthesis Services
*   **Change:** Move metadata extraction (Title/Summary) to a decoupled service.
*   **Impact:** Logic for synthesizing data becomes portable and can be executed independently of the primary ingestion engine.
