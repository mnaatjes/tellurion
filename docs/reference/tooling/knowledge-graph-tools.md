# Knowledge Graph Tooling and Management

In the Gemini CLI ecosystem, Knowledge Graph (KG) management is built on the **Model Context Protocol (MCP)**. This architecture decouples "Reasoning" (the LLM) from "Structured Memory" (the Graph Database), allowing you to employ professional-grade graph tools while maintaining a terminal-centric workflow.

---

## 1. Neo4j Ecosystem (The Industry Standard)

Neo4j is the primary graph provider for Gemini CLI, offering a suite of specialized MCP servers that handle the entire graph lifecycle.

### The Neo4j Extension Suite
Rather than a single server, the Neo4j extension consists of several specialized components:

| Component | Function | Application |
| :--- | :--- | :--- |
| **`mcp-neo4j-data-modeling`** | **Interactive Modeling** | Ask Gemini to "design the schema" or "propose a new relationship" for your Salesforce data. |
| **`mcp-neo4j-cypher`** | **Natural Language Translation** | Translates prompts (e.g., "Find all ETL scripts dependent on the Leads table") into formal **Cypher** queries. |
| **`mcp-neo4j-memory`** | **Persistent Fact Storage** | The "Monitoring" hub for long-term memory, allowing the agent to store and retrieve project facts across sessions. |

### Neo4j Aura Console (External Monitoring)
While work happens in the CLI, the **Aura Console** (Web UI) acts as your visual "Control Tower":
- **Visual Monitoring:** Real-time visualization of nodes (entities) and edges (relationships) as they are created by the agent.
- **Health Checks:** Provides database performance metrics and storage limits, essential for resource management on local hardware like an HP ProDesk.

---

## 2. Local and Open-Source Alternatives

For developers who prefer a strictly local, privacy-focused, or lightweight setup on Linux, these tools offer advanced monitoring and synthesis capabilities.

### Graphiti (Temporal Knowledge Graph)
Designed specifically for AI agents, **Graphiti** adds a "Time" dimension to your graph data.
- **Temporal Tracking:** Monitors how relationships change over time (e.g., "The BigQuery schema looked like X yesterday but is now Y").
- **Linux Integration:** Operates as a Python library and MCP server. You can debug its performance using standard Linux tools like `journalctl` or by tailing the JSON logs in `./.gemini/logs/`.

### TrustGraph (The "Context OS")
TrustGraph provides an enterprise-grade approach to graph monitoring and ontology enforcement.
- **Ontology Management:** Enforces the "Rules of the Graph," ensuring the agent doesn't create invalid relationship types (e.g., a "BigQuery_Table" cannot "TRANSFORM" a "Salesforce_User").
- **Telemetry:** Built-in observability to track the token cost and execution time of individual graph queries.

---

## 3. CLI-Native Monitoring and Health

You can monitor your graph's health directly from within the Gemini CLI using these built-in commands:

- **`/mcp desc`**: Use this to check the status of your graph server. A "Ready" status indicates a healthy connection.
- **`/mcp call knowledge-graph list_nodes`**: A rapid way to "peek" into the database and verify that ingestion scripts are successfully creating entities.
- **`/stats session`**: Vital for maintaining **Token Efficiency**. It shows if graph retrieval is contributing to context window bloat, allowing you to tune your retrieval depth.

---

## Summary Reference Table

| Requirement | Recommended Tool | Rationale |
| :--- | :--- | :--- |
| **System Modeling** | `mcp-neo4j-data-modeling` | Collaborative "Whiteboarding" with Gemini. |
| **System Visualization** | Neo4j Aura Console | Best visual "x-ray" of Salesforce/BigQuery relationships. |
| **Local/Private Memory** | Graphiti or FalkorDB | Lightweight, high-performance, and runs natively on Linux. |
| **Tool Auditing** | Datadog MCP Server | Professional-grade monitoring of tool calls and usage patterns. |
