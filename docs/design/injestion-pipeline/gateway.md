# Ingestion Pipeline Domain-Library Gateway

* **Domain Library**: Standalone packages unaware parent 'App' exists

`pipeline = IngestionPipeline()` - Gateway for Ingestion Pipeline Domain Library

* **Ingestion Flow**:
1. Ingestion Pipeline Initialization
    * User can use `pipeline.available.x()` to access available embedders, etc
2. Execute Builder DSL
    * `pipeline.build()...`
    * `.addSource()` [Required]
    * `addStorage()` [Required]
    * [Optional] User can add embedders, parsers, readers

## 1.0 Dependencies

### 1.0.1 `Bootstrap()`

**Class Properties**
* **`ServiceProvider(ABC)`** - 
* **`ServiceContainer`** - See below

**Notes**:

* Implement *Late Binding* approach where Service-Providers registers the *Potential* to create an object but only instantiates it if the user doesn't provide an override

```py
# Inside your Bootstrap / ServiceProvider
def register_defaults(container):
    # Registering a "Factory" or "Provider", not an instance
    container.register("READER:LOCAL", lambda: SimpleDirectoryReader())
    container.register("PARSER:SENTENCE", lambda: SentenceSplitter(chunk_size=1024))

    # TODO: Figure out how Bootstrapped settings like chunk_size=1024 above are added via a similar mechanism to the later Blueprints which will be utilized for communication between various pipeline.addX() methods
```

**Methods**
* **`register()`** - 
* **`boot()`** - 

---

### 1.0.2 `ServiceContainer()`

**Properties**:
* **`registry`** [Dict [instanceName|Instance]] - 

**Methods**:
* **`register()`** - 
* **`get()`** - 

---

### 1.0.3 `Builder()`

**Requirements**:
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

**Properties**
* **`global`** - `Settings()` Instance used to define global settings of Pipeline Instance

**Methods**:
* **`build()`** [Required] - Access to the Builder() instance
* **`addSource()`** [Required] - 
* **`addParser()`** [Optional] - 
* **`addReader()`** [Optional] - 
* **`addEmbedder()`** [Optional] - 
* **`addStorage()`** - [Required] Storage Context [sink]: Vector DB or a SimpleStore (local filesystem)
* **`addEnrichment()`** - 
* **`setup()`** [Required] - 


Use Case:

```py
# Adding a source to the pipeline
pipeline = IngestionPipeline()
pipeline.build() \
    .addSource(type:str, uri:Optional[str], bucket:Optional[str])
```
---

### 1.0.4 `Registry()`

**Methods**:
* **`register()`**
    * `.parser()` - 
    * `.embedder()` - 
    * `.reader()` - 
    * `.enrichment()`

```py
pipeline.register.parser("AdvancedSplitter", AdvancedSplitter())
```

* **Properties**
* **`available`** - list of all registered parsers, embedders, readers

```py
pipeline.available.Parsers() # Returns list of available Parsers
pipeline.available.Embedders() # Returns list of available Embedders
```

**Methods**:

### 1.0.5 `StrategyResolver()` Service


### 1.0.x `Executor()`

### 1.0.x ``
### 1.0.x ``