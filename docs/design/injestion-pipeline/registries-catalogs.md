# Ingestion Pipeline: Registries

## 1.0 Overview

### 1.1 Terminology: What do we call the parts?

In a Registry/Catalog pattern, consistent naming is the "Stitch" that holds the framework together. Here is the standard industry terminology:

* **Key (or Alias)**: The unique string identifier (e.g., "google_flash").
* **Entry (or Record)**: The actual item stored. In your case, this is the Blueprint DTO.
* **Registry**: The collection itself.
* **Store (Internal)**: The underlying data structure (usually a dict).


## 2.0 Components

Constituent Parts of the Registry System

### 2.1 Abstract `Registry()`

* **Location**: `src/core/registries/`

**Directory Tree**

```
src/
└── core/
    └── registries/
        ├── base.py         # The Abstract BaseRegistry
        ├── llms.py         # The LLMRegistry class
        ├── parsers.py      # The ParserRegistry class
        └── collection.py   # The RegistryCollection class (The "Stitch")
```

#### 2.1.1 Creation of Abstract Class

* **Location**: `src/core/registries/base.py`
```py
from abc import ABC, abstractmethod
from typing import Dict, Generic, TypeVar, List, Any

# T represents the specific Blueprint DTO type
T = TypeVar("T")

class BaseRegistry(ABC, Generic[T]):
    def __init__(self):
        self._store: Dict[str, T] = {}

    def add(self, key: str, entry: T) -> None:
        """Adds a Blueprint to the vault."""
        if key in self._store:
            raise KeyError(f"Entry '{key}' already exists in {self.__class__.__name__}")
        self._store[key] = entry

    def get(self, key: str) -> T:
        """Retrieves a Blueprint by its Alias/Key."""
        if key not in self._store:
            raise KeyError(f"Entry '{key}' not found in {self.__class__.__name__}")
        return self._store[key]

    def list_keys(self) -> List[str]:
        """Returns all registered aliases (used by the Catalog)."""
        return list(self._store.keys())

    def get_all(self) -> Dict[str, T]:
        """Returns the entire store (used by the Registrar/Bootstrap)."""
        return self._store.copy()
```

#### 2.2 Implementation of Registry Classes
* **Locations**: 
    * Registry - `src/core/registries/llm.py`
    * Blueprint - `src/domain/models/blueprints/llm.py`
```py
class LLMRegistry(BaseRegistry[LLMBlueprint]):
    """Specific vault for LLM configurations."""
    pass

class EmbedRegistry(BaseRegistry[EmbedModelBlueprint]):
    """Specific vault for Embedding configurations."""
    pass
```
### 2.2 `RegistryCollection()`

If the Registries are individual "Vaults" (LLM Vault, Parser Vault), the RegistryCollection is the Warehouse Floor that holds them all in one place.

* **It is a Container:** It exists solely to provide a single, unified reference to all available "Vaults."
* **It is a Dependency Root:** Instead of your App facade needing to track five different variables, it tracks one (the Collection).
* **It is NOT a Registry:** A Registry has logic for add() and get(). The Collection is usually a simple object with Properties (e.g., self.llms, self.parsers).

* **Location**: `src/core/registries/collection.py`

```py
class RegistryCollection:
    """The 'Engine Block' - Pure state storage."""
    def __init__(self):
        self.llms = LLMRegistry()
        self.parsers = ParserRegistry()
        self.embeddings = EmbeddingRegistry()
```

### 2.3 `Registrar()`

* **Location**: `src/core/ports/input/registar.py`

```py
class Registrar:
    """The 'Accelerator' - Logic for writing."""
    def __init__(self, registries: RegistryCollection):
        self._regs = registries

    def llm(self, alias, bp):
        # The Registrar focuses on VALIDATION logic
        self._regs.llms.add(alias, bp)
        return self
```


### 2.2 `Catalog()`

**Directory Tree**

```
src/
└── core/
    ├── registries/           # The "Vaults" (Internal State)
    │   ├── base.py           # BaseRegistry[T]
    │   └── llm_registry.py
    └── ports/
        └── output/           # The "Lenses" (Output Ports)
            └── catalog/            # The "Lenses" (Output Ports)
                ├── base.py         # BaseCatalog[T]
                ├── llm_catalog.py
                └── collection.py   # CatalogCollection (The "Menu")
```

#### 2.2.1 Abstract

* **Location**: `src/ports/output/catalog/base.py`

```py
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
from src.core.registries.base import BaseRegistry

# T represents the Blueprint DTO type
T = TypeVar("T")

class BaseCatalog(ABC, Generic[T]):
    def __init__(self, registry: BaseRegistry[T]):
        # The Catalog holds a reference to the Registry (The "Stitch")
        self._registry = registry

    def names(self) -> List[str]:
        """Returns the raw list of registered aliases."""
        return self._registry.list_keys()

    @abstractmethod
    def list_all(self) -> Any:
        """
        Abstract method to return a formatted view of all entries.
        Implementation will vary (e.g., a Rich Table or a simple List).
        """
        pass

    def get_info(self, alias: str) -> T:
        """Proxies the 'get' call but usually returns a sanitized version."""
        return self._registry.get(alias)
```

#### 2.2.2 Implementations

* **Location**: `src/ports/output/catalog/<name>.py`

```py
class LLMCatalog(BaseCatalog[LLMBlueprint]):
    def list_all(self):
        """Returns a human-readable summary of available LLMs."""
        aliases = self.names()
        # Logic to return a pretty list for your Kalamazoo terminal
        return [f"LLM: {a} (Model: {self.get_info(a).model_name})" for a in aliases]

class ParserCatalog(BaseCatalog[ParserBlueprint]):
    def list_all(self):
        """Specific view for Parsers."""
        return [f"Parser: {a}" for a in self.names()]
```

### 2.3 `CatalogCollection()`

#### 2.3.1 Port Implementation

* **Location**: `src/ports/output/catalog/collection.py`

```py
class CatalogCollection:
    def __init__(self, registries: RegistryCollection):
        # We wrap each registry in its specific Catalog Lens
        self.llms = LLMCatalog(registries.llms)
        self.parsers = ParserCatalog(registries.parsers)
        self.embeddings = EmbeddingCatalog(registries.embeddings)
```

#### 2.3.2 Relationship to Fascade

Because the CatalogCollection is the Output Port, the Facade holds a live instance of it. When a user (the "Actor") wants to see what is available, they touch the Facade, which delegates the request directly to the Collection.

1. **The Communication "Stitch"** - The Facade does not "talk" to the Catalog via a complex protocol; it simply owns it. It acts as the gatekeeper.

    * **Internal Storage**: The Facade holds the RegistryCollection (The Data).
    * **The Lens**: The Facade initializes the CatalogCollection (The Port) and passes it the data.
    * **The Exposure**: The Facade provides a @property named available that returns the Catalog.

2. **Fascade Flow**:
```py
class IngestionApp:
    def __init__(self, container: ServiceContainer):
        # 1. Resolve the "Warehouse Floor" from the Container
        self._registries = container.get(RegistryCollection)

        # 2. Initialize the "Menu" (Catalog) by giving it the Data
        # This is the "Stitch" where the Port meets the Core
        self._catalog = CatalogCollection(self._registries)

    @property
    def available(self) -> CatalogCollection:
        """
        The Communication Bridge. 
        Provides the User with a Read-Only view of the Framework.
        """
        return self._catalog
```

3. **The Flow of the "Conversation"** - When you are in your Kalamazoo terminal and you run a command, the communication follows this chain:
    * **User**: app.available.llms.list_all()
    * **Facade**: Receives the .available call and returns the CatalogCollection instance.
    * **CatalogCollection**: Navigates to the .llms attribute (the LLMCatalog).
    * **LLMCatalog**: Reaches into the LLMRegistry it was given during __init__.
    * **Output**: The data is formatted and returned to the User.