# Ingestion Pipeline: Builder

## 1.0 Overview

This is where the "Stitch" between Framework Configuration (the Registries) and User Intent (the Builder) gets interesting.

To answer your first question: No, there is not a strict 1:1 relationship between a Source and a Reader/Parser. Instead, it is a Many-to-One-to-Many relationship managed by Defaults and Overrides.

1. **The Relationship Logic** In a professional ingestion pipeline on your HP ProDesk, the logic should follow a "Waterfall" approach:
    * **The Source**: A raw location (Path, S3 Bucket, API Endpoint).
    * **The Reader**: The "Interpreter" that can turn that source into a Document.
    * **The Parser**: The "Transformer" that breaks that Document into Nodes/Chunks.

2. **The Use-Case: Avoiding Redundancy** You are exactly right—a user shouldn't have to specify a reader for every source if they are all just local directories. Your Builder should handle this via Sticky Defaults.
    * **Scenario A**: The "Global" Approach (Most Common)
    The user sets a default Reader and Parser for the whole pipeline. Every Source added after that automatically inherits them.

    ```py
    pipeline.build() \ 
        .addReader("simple_directory") \  # This is now the "Global" reader
        .addSource("path/to/dir1") \      # Inherits simple_directory
        .addSource("path/to/dir2")        # Inherits simple_directory
    ```

    * **Scenario B: Explicit Override** If the third source is different (e.g., a Database instead of a Folder), the user can override just that one.

    ```py
    pipeline.build() \
    .addReader("simple_directory") \
    .addSource("path/to/dir1") \
    .addSource("path/to/dir2") \
    .addSource("database_connection", reader="postgres_reader") # Overrides global for this source
    ```

3. **Implementation: The Builder's "Active State"** Inside your PipelineBuilder, you should maintain a "Current State" for these components.

4. **Why this works for the AgentCLI**
    * **Predictability**: The user controls the "State" of the builder. If they want to change readers halfway through a chain, they just call .addReader() again with a new alias.

    * **Validation**: Since you are in a Linux environment, your addSource can immediately check if the path exists and if the active_reader is compatible with that file type.

    * **Lean DTO**: The PipelineBlueprint that comes out of this will have a list of SourceEntries, each perfectly "Stitched" to its specific reader and parser.

5. **The "Smart" Shortcut (Optional Idea)** To make it even easier for your users, your addSource could attempt *Auto-Discovery:*

    "If no reader is set, look at the file extension. If it's .pdf, automatically fetch the pdf_reader from the Registry."

6. **Verdict:** Use Sticky Defaults. It respects the user's time while maintaining the granular control needed for complex ETL tasks.

### 1.1 Requirements

1. **Input Configuration**
    * `input_dir` | `input_files` [str|list]
    * `file_extractor` [Strategy] Mapping specific file exensions to specific parsers (`StrategyResolver()` Service)
2. **Transformation Configuration**
    * `chunk_size` [int] Default 1024
    * `include_metadata` [bool] Default False
3. **Model Configuration**
    * `embed_model` [BaseEmbedding] See `builder().addEmbedder()`
4. **Metadata** [Optional]
    * `extra_info` - Custom Tags

#### 1.2 Properties

* **`global`** - `Settings()` Instance used to define global settings of Pipeline Instance


#### 1.3 Methods

* **`build()`** [Required] - Access to the Builder() instance
* **`addSource()`** [Required] - 
* **`addParser()`** [Optional] - 
* **`addReader()`** [Optional] - 
* **`addEmbedder()`** [Optional] - 
* **`addStorage()`** - [Required] Storage Context [sink]: Vector DB or a SimpleStore (local filesystem)
* **`addEnrichment()`** - 
* **`setup()`** [Required] - 


#### 1.4 Class Implemenation

```py
class PipelineBuilder:
    def __init__(self, registries):
        self._regs = registries
        self._blueprint = PipelineBlueprint()
        
        # The "Sticky" defaults
        self._current_reader = None
        self._current_parser = None

    def addReader(self, alias: str):
        # Sets the default reader for all SUBSEQUENT sources
        self._current_reader = self._regs.readers.get(alias)
        return self

    def addSource(self, path: str, reader: str = None):
        # Use the override if provided, otherwise use the sticky default
        active_reader = self._regs.readers.get(reader) if reader else self._current_reader
        
        if not active_reader:
            raise ValueError(f"No reader defined for source: {path}")

        self._blueprint.sources.append(
            SourceEntry(path=path, reader=active_reader, parser=self._current_parser)
        )
        return self
```

#### 1.5 Instantiation

```py
# Adding a source to the pipeline
pipeline = IngestionPipeline()
pipeline.build() \
    .addReader("simple_directory") \
    .addSource("path/to/dir1") \
    .addSource("path/to/dir2") \
    .addSource("database_connection", reader="postgres_reader") # Overrides global for this source
```
---