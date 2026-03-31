# How-To: Configuring Knowledge Graphs (KG)

Configuring a Knowledge Graph for the Gemini CLI transforms your agent from a "document searcher" into a "systems thinker." While Vector RAG is excellent for finding specific text snippets, a Knowledge Graph allows the agent to understand the logical relationships and hierarchies within your complex systems (e.g., how a Salesforce Lead object eventually populates a BigQuery Landing Table).

On a Linux system, this is achieved by connecting a Graph Database to the Gemini CLI via the **Model Context Protocol (MCP)**.

---

## Step 1: Initialize the Graph Storage and Schema

Since you are working in a local Linux environment, you need a place for the graph data to live and a "schema" (ontology) that defines the types of entities and relationships the agent should recognize.

### 1. Create the Graph Directory
```bash
mkdir -p ./.gemini/knowledge-graph/data
```

### 2. Define the Schema (Ontology)
Create a file at `./.gemini/knowledge-graph/schema.json`. This tells the agent what "types" of things exist in your specific domain.

**Example `schema.json` for an ETL project:**
```json
{
  "entities": ["Salesforce_Object", "BigQuery_Table", "ETL_Script", "API_Endpoint"],
  "relationships": ["POPULATES", "DEPENDS_ON", "TRANSFORMS", "TRIGGERS"]
}
```

---

## Step 2: Configure the MCP Graph Server

The Gemini CLI does not communicate with graph databases natively; it uses an MCP Server as a translator.

1.  Open your global settings: `nano ~/.gemini/settings.json`.
2.  Add a new entry under the `mcpServers` object:

```json
"mcpServers": {
  "knowledge-graph": {
    "command": "npx",
    "args": [
      "-y", 
      "@modelcontextprotocol/server-knowledge-graph", 
      "--db-path", "./.gemini/knowledge-graph/data/graph.db"
    ],
    "env": { 
      "GRAPH_SCHEMA_PATH": "./.gemini/knowledge-graph/schema.json" 
    }
  }
}
```

---

## Step 3: Map Entities within Expert Skills

You must explicitly tell your expert agents (Skills) to prioritize the Knowledge Graph for structural or relationship-based questions.

Edit your skill's `SKILL.md` (e.g., `./.gemini/skills/bigquery-architect/SKILL.md`) to include **Graph Authority** instructions:

```markdown
## Knowledge Graph Authority
- All entities of type `BigQuery_Table` are defined in `docs/reference/schema.json`.
- Relationships of type `DEPENDS_ON` are derived from the `lineage.md` file.
- **Protocol:** Always query the `knowledge-graph` MCP server to verify system dependencies before proposing a schema or logic change.
```

---

## Step 4: Populate the Graph (Ingestion)

A Knowledge Graph is only useful once it has been "seeded" with the actual relationships of your project.

### 1. Run the Ingestion Command
You can use the CLI to call the MCP server's ingestion tools:
```bash
gemini mcp call knowledge-graph create_entities --from-file docs/reference/architecture_overview.md
```

### 2. Verify the Nodes
Confirm that the agent "sees" your objects as logical nodes:
```bash
/mcp call knowledge-graph list_nodes
```
If successful, the CLI will output a list of your system components (Salesforce objects, tables, etc.) and their defined relationships.

---

## Step 5: Monitoring, Visualization, and Maintenance

As your ETL scripts or system architectures evolve, the graph must stay in sync.

- **The "Janitor" Pattern:** Create a script in your `./.gemini/skills/<name>/scripts/` folder that triggers an update whenever a file in `docs/` or `src/` changes.
- **Visualization:** On Linux, you can export the graph data to a **DOT** file for viewing with Graphviz:

```bash
# Export the graph
gemini mcp call knowledge-graph export_dot > project_map.dot

# Convert to a viewable image
dot -Tpng project_map.dot -o project_map.png
```

---

## Summary of Architectural Authority

| Layer | Component | Role |
| :--- | :--- | :--- |
| **Global Logic** | **Knowledge Graph** | Maps "The Big Picture" and system-wide relationships. |
| **Local Facts** | **Vector Store (RAG)** | Retrieves specific paragraphs or code snippets. |
| **Orchestrator** | **Gemini CLI** | Decides which tool to use based on the user's query. |
