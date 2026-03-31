# Agent Reference Materials and Content Optimization

The "Data Digestion" phase is the process of converting large, messy documentation (PDFs, HTML, logs) into "High-Signal" Markdown files that are optimized for an agent's context window. This ensures that the agent's limited memory is spent on useful information, not on advertisements or formatting junk.

## 1. Synthesis Engines

Synthesis tools are ideal for extracting the "wisdom" from long manuals and technical specifications.

| Tool | Focus | Use Case |
| :--- | :--- | :--- |
| **Fabric** | Fact Extraction | Uses the `extract_wisdom` pattern to condense long texts into a bulleted list of facts, setup steps, and tips. |
| **LlamaIndex** | Knowledge Structuring | Creates a Vector Index or `knowledge_graph.json` from a massive library, summarizing the entire collection for the agent to reference. |

### Example Command (Fabric)
```bash
# Pipe a long technical manual into Fabric to generate a condensed reference file
cat salesforce_manual.txt | fabric --pattern extract_wisdom > .gemini/skills/sf-expert/references/core_logic.md
```

## 2. Document Cleaning and Transformation

For raw or scraped data, cleaning libraries are required to remove noise that would otherwise bloat the context window.

- **Unstructured.io:** A powerful Python library designed to "ingest" messy formats (HTML, PDF, DOCX) and transform them into clean, structured Markdown. It automatically removes navigation bars, advertisements, and other non-content elements that waste tokens.

## 3. Reference Material Best Practices

- **Signal-to-Noise Ratio:** Aim to reduce the size of reference materials by 90% or more (e.g., a 50MB PDF should be condensed into a 50KB high-signal Markdown file).
- **Structured Formatting:** Use headers, bullet points, and code blocks to make information easily scannable for the LLM.
- **Hierarchical Access:** Break massive references into smaller, domain-specific files (e.g., `api_v1.md`, `api_v2.md`) to be loaded only when needed.
