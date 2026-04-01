# Prototype of User Gateway / Client

## 2.0 Ingestion Pipeline Client

* **Components**:
    * `app.pipeline` - 
    * `app.pipeline.builder()` - DSL chain to assign global settings, add Parsers, 
    * `` - 

### 2.1 Pipeline Builder

`app.pipeline.builder()` - Builds the Pipeline and returns a Pipeline Instance

* **Requirements**
    * `PipelineBlueprint`
        * `Identity` - Identification DataClass Object
            * `trace_id` - User-supplied OR System Generated
            * `created_at` - Timestamp
            * `name` [Optional] - Name of pipeline for deliniation
        * `Settings` - A DataClass Object with global settings
            * `chunk_size` - Breakup sizes
            * `embed_model` - BaseEmbedding Model Instance
            * `` - 

#### 2.1.2 Assigning Globals

```py
pipeline = app.pipeline.build() \
    .globals(chunk_size=1024, embed_model="BaseEmbeddingInstance")
```

```py
# Init User Client
app = Gateway()

# Returns Builder
builder = app.pipeline.build()

# Builder global settings (Can be chained)
builder.includeMetadata() # Sets to true
builder.includeRelationships() # sets include_prev_next_rel to true
builder.assignCallManager = CallManagerInstance()


# Builder forms contracts

# Builder for Documents
builder.addDocument("file_path")
builder.addDocuments(**document_kwargs)
```