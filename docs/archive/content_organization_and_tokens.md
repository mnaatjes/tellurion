# Content Organization and LLM Tokens

This document provides a strategy for organizing a substantial body of work (authored works, correspondence, etc.) for use with Gemini CLI subagents and explains the fundamental unit of LLM processing: the Token.

## 1. Organizing a Body of Work

To create a high-fidelity subagent that can accurately represent a persona or analyze a large dataset, the content must be organized for efficient "research" by the agent.

### Recommended Directory Structure
Use a hierarchical structure that allows the agent to navigate by category and chronology.

```text
/author_name/
├── bibliography.md          # Master index of all works with metadata
├── books/                   # Long-form works broken down by chapter
│   ├── book_1/
│   │   ├── chapter_01.md
│   │   └── chapter_02.md
├── essays/                  # Shorter, thematic works
│   ├── essay_title_A.md
│   └── essay_title_B.md
├── correspondence/          # Letters, sorted by date or recipient
│   ├── 1850_to_recipient_X.md
│   └── 1851_to_recipient_Y.md
└── themes/                  # Synthetic summaries of key concepts
    ├── philosophy_of_X.md
    └── recurring_motifs.md
```

### File Size and Scope Guidelines
*   **Target Size:** 2,000 to 5,000 words per Markdown file (approx. 10–20 pages).
*   **Why?** Files larger than this risk the "Lost in the Middle" phenomenon, where the LLM misses details in the center of the text. Smaller files increase the number of tool calls needed for context.
*   **Scope:** 
    *   **Books:** Break down by **Chapter**.
    *   **Essays/Letters:** One file per **Document**.
    *   **Thematic Layer:** Create a `themes/` directory to act as a "map" or "index" for the agent to find primary sources.

---

## 2. Understanding Tokens

A **token** is the fundamental unit of measurement for how an LLM "reads" and "writes" text. It measures computational cost and context capacity.

### Token Correlations (English Language)
While precise tokenization varies by model, use these standard approximations:

*   **1 Token ≈ 4 Characters** (including spaces).
*   **1 Token ≈ 0.75 Words.**
*   **1,000 Tokens ≈ 750 Words** (approx. 1.5 single-spaced pages).
*   **1,000 Tokens ≈ 4 KB of data** (uncompressed plain text).

### Reference Table
| Unit | Approximate Tokens |
| :--- | :--- |
| **Short Sentence** | 10–15 tokens |
| **Standard Paragraph** | 100–200 tokens |
| **300-Page Book** | 100,000–150,000 tokens |
| **Source Code** | Higher density due to special characters |

### Impact on Agents
1.  **Context Window:** The total tokens the agent can "remember" at once (e.g., 128k to 2M for Gemini 1.5).
2.  **Efficiency:** Reading only relevant sections of a file (using `start_line` and `end_line`) preserves the context window for more complex reasoning.
