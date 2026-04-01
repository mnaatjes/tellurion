# Prototype of User Gateway / Client

## 1.0 Overall Flow / Lifecycle

### 1.1 LlamaIndex Linear Progression

1. Configure - Assigns BaseEmbedding with `Settings.embed_mode = OpenAIEmbedding()` 
2. Assign Reader Instance `reader = SimpleDirectoryReader()`
3. Read Content - `documents = reader.load_data()`
4. Parse - `nodes = get_nodes_from_documents(documents)`
5. Enrich / Extract Metadata - `TitleExtractor()`, `SummaryExtractor()`, etc.
6. Embed - Vectorize Nodes `get_text_embedding()`
7. Index - Build the Search Index `VectorStoreIndex(...)`
8. Persist - Save to Disk/DB `index.storage_context.persist()`

## 2.0 Ingestion Pipeline Client

* **Dependencies**:
    * `Bootstrap()` - Assembles system
    * `ServiceContainer` - Registers all *Available* **Providers**:
        * `ParserProvider` - contains all *Available* llamaIndex parser Instances
        * `EmbedderProvider` - Registers all *Available* Base Embedders
        * `ReaderProvider` - Registers all *Available* Readers

* **Gateway Methods**:
    * `app.available` Access to the lists map
        * `.Embedders()`
        * `.Parsers()`
        * `Readers()`
    * `app.register` - Access to ServiceContainer
        * `.Embedder()`
        * `.Parser()`
        * `.Reader()` -

* **Pipeline Methods**:
    * `app.pipeline` - 
    * `app.pipeline.builder()` - DSL chain to assign global settings, add Parsers, 
    * `` - 

### 2.1 Pipeline Builder

`app.pipeline.builder()` - Builds the Pipeline and returns a Pipeline Instance
* Factory pattern
* User-interface DSL Chain

* **Requirements**
    * `PipelineBlueprint`
        * `Identity` - Identification DataClass Object
            * `trace_id` - User-supplied OR System Generated
            * `created_at` - Timestamp
            * `name` [Optional] - Name of pipeline for deliniation
        * `Settings` - A DataClass Object with global settings
            * `chunk_size` [int] - Breakup sizes
            * `embed_model` [BaseEmbedding] - BaseEmbedding Model Instance
            * `include_metadata` [bool] - Enable metadata for ALL parsers and types
            * `include_relationships` [bool] - Include relationships between sequential nodes (links predecessor and successor)
            * `callbackManager` [Callable] - Used for tracing and logging
        * `Parsers` [List] - List of ParserBlueprints
    
    * `ParserBlueprint` - DataClass which defines required arguments
        * `instance_name` [Union [nickname|InstanceName]] - llamaIndex parsers [SimpleFile, HTML, JSON, Markdown, CodeSplitter, LangChain, Chunker, SentenceSplitter, SentenceWindow, SemanticSplitter, TokenText, Hierarchical]
        * `configuration` [Dict] - Waterfall of settings
        * `Parsers` [Dict]
        * `Embedders` [Dict]
        * `Readers` [Dict]

#### 2.1.2 Assigning Global Settings

```py
pipeline = app.pipeline.build() \
    .globals(chunk_size=1024, embed_model="BaseEmbeddingInstance")
```

#### 2.1.3 Adding Parsers

`app.pipeline.build().addParser()` - Generates `ParserBlueprint` DataClass

Parsers added to a global ServiceContainer during bootstrapping phase by ParserServiceProvider

```py
pipeline = app.pipeline.build() \
    .globals(...) \
    .addParser(
        instance_name="",
        **parser_configuration={}
    )
```

### 2.1.4 Pipeline Instance

User has used `app.pipeline.build()` DSL Chain to create their Pipeline.

`pipeline = app.pipeline.build().setup()` - Returns a Pipeline Instance

**Dependencies**: 
* `PipelineRegistry` - Registers assets for a whole pipeline
    * `ParserCatalog` [instanceName,ParserBlueprint] - via `builder.addParser(...)`
    * `FilesystemCatalog` [key,Path] - via `pipeline.addDocument()`, `pipeline.addDocuments()`, `pipeline.addDirectory()`

**Utility Methods**:
* `pipeline.list()` - Lists *Registered* Parsers and Documents from PipelineRegistry
* `pipeline.listParsers()` - Lists *Registered* Parsers
* `pipeline.listFilesystem()` - Lists *Registered* Directories AND Documents
* `pipeline.listDirectories()` - Lists *Registered* Directories
* `pipeline.listDocuments()` - Lists *Registered* Documents
* `pipeline.getParser()` - TBD

### 2.1.5 Resolution

`pipeline.execute()` - Hands all Blueprints off to the `PipelineEngine` which executes based on Blueprint

**Dependencies**
* `PipelineStrategy` [DataClass] - Object representing decided-upon Strategy Contract
* `PipelineStrategyResolver()` - Class which intakes Blueprints and resolves into PipelineStrategy dataclasses
    * `resolve()` - 
    * `execute()` - 

## x.x Integration

```py
# Init User Client
app = Gateway()

# Assign global settings

# Add Parsers

# Add Directories and Documents
```