
# x.1 Component Registry and Catalog

**Conceptual Logic Flow**:
1. **Bootstrap** - Registrar fills Registry with every LLM tool
2. **Selection** - `app.pipeline.build().addLLM()` Builder checks Catalog if `llm` exists
3. **Assembly** - `.addLLM()` a `ParserBlueprint` copied from `Registry` by `Registrar` into `PipelineBlueprint`
4. **Execution** - `Fascade.Executor.run(blueprint)` Executes

**Read and Write Heirarchies**:
```mermaid
graph TD
    subgraph "1. Bootstrap Process (Framework Startup)"
        SP[ServiceProvider ABC] --> C[Registrar]
        C --> E[(LLMRegistry)]
        C --> SC[ServiceContainer]
        E --- G[(RegistryCollection)]
    end

    subgraph "The App Facade (Core)"
        A[App Facade] --> SC
        A --> B[CatalogCollection]
        A --> H[PipelineBuilder]
    end

    subgraph "2. Runtime Process (User Selection)"
        B --> E
        B --> H
        H --> I[PipelineBlueprint DTO]
    end
```