# Prototype Design outline for Agents Management / Orchestration Project

---

## 1.0 Token Efficiency: 

Sending entire manuals to an LLM is expensive and prone to "lost in the middle" errors. Synthesizing data beforehand is the standard way to maintain accuracy while minimizing costs.

### 1.1 The Strategy: "Just-in-Time" Context

Instead of sending a "dump" of all documentation (which causes the "lost in the middle" phenomenon), modern agents use a Layered Context approach.

**Layer 1 (The Anchor):** A permanent, high-level "System Instruction" or CLAUDE.md/CONVENTIONS.md file that defines the goal and rules. This stays in the window.
* **Static**:
* **Global**:
* **Contains**
    * *MCP*
    * `CONVENTIONS.md`: Defines the goal and rules
* **Operates**: Operates and stays within the *Window* and is limted by *Tokens*

**Layer 2 (The Working Set and Runbook):** Only the specific code files or manual chapters currently being edited or referenced.
* **Dynamic**
* **Context-Sensitive**: Lives where your active work is happening. Located in `<project_root>/`
* Managed by a combination of the *Project Level Configuration* and the *MCP*
* **Contains**: 
    * **Working Set**: Definition of Directories and Files which define the *Scope* of the project. 
        * The geographical state of the project
        * Determined by `cwd()`
    * **Runbooks**: Where to pull files from for a specific process
        * Defined in `./.gemini/<runbook>.ext`
        * Accepted File Formats: 
            * `.md` -  Complex, "agentic" workflows
            * `.json` - Strict, Programmatic Configurations
            * `.yml` - Middle-Ground between `.md` and `.json`

**Layer 3 (The Ephemeral):** Search results or tool outputs that are discarded or summarized once the sub-task is complete.

* **What is it?**: Short-term memory of your session
    * **Dynamic** in-memory during an acctive terminal session
    * **Location** `/tmp` (`/tmp/gemini-cli-cache-[hash]/`) directory in linux (e.g. when Gemini CLI performs `google_web_search` it downloads raw data)
* **What to do with it?**: Leave it alone. Don't monitor it - it isn't useful

---

### 1.2 The Technique: Data Synthesis & Compaction

This is where tools like Fabric shine. Synthesis reduces 100 pages of "raw" manual into a 2-page "distillation" of patterns and rules.

**Pre-Processing (The "Digestion" Phase):** Before the LLM even sees the manual, a script (or a specialized "summarizer" agent) extracts key facts, API signatures, and logic flows.

**Vector Embeddings (Semantic Search):** You convert the manual into mathematical vectors. When you ask a question, the CLI only retrieves the top 3 most relevant "chunks" rather than the whole book. This is the core of RAG (Retrieval-Augmented Generation).

**Adaptive Compaction:** As a conversation gets long, the CLI "summarizes" the previous 20 messages into a single paragraph to free up space for new reasoning tokens.

### 1.3 Implementation Tools and Handshakes

| Method | How it Saves Tokens |
|--------|---------------------|
| Re-ranking | Board Search to Smaller Model identifying best snippets (from 5,000 tokens of poor date to 500 tokens of high-quality data) |
| Model Context Protocol (MCP) | Agent calls a tool that returns Only the specific table definition it needs at the moment |
| Repo Mapping (Aider Style) | Aider sends a "map" of the project (file-names and function signatures) to the LLM knows the structure without reading every line of code |

---

## 2.0 Specialization Creating 

"Expert Agents" allows you to define strict system instructions for each domain (e.g., a "BigQuery Architect" vs. a "Salesforce Integration Specialist"), which prevents the model from giving generic or hallucinated advice.



## 3.0 Concepts and Steps to Consider

Vector Embeddings: This is the secret to token reduction. By pre-calculating embeddings for your documentation, you only pay for the tokens in the final prompt, not the entire library of resources.

Knowledge Graphs: While RAG is great for facts, a Knowledge Graph helps an agent understand relationships (e.g., how "Salesforce Custom Objects" relate to "REST API Endpoints"). This is helpful for the "Integration" roles you are targeting.

Evaluation (LLM-as-a-Judge): Create a small script that tests your agents. If you are learning BigQuery, have a "Professor" agent quiz you and another "Auditor" agent check if the expert agent’s explanation was technically accurate based on the source docs.

Memory Persistence: Ensure your agents have a "Session Context." If you are learning window functions in SQL, the agent should remember what you struggled with yesterday so it can adjust its "lesson plan" today.

The "Human-in-the-loop" pattern: Since you have 15 years of experience managing complex logistics in the hospitality industry, you can apply that "Manager" mindset here. Build a CLI interface that allows you to "veto" or "deep dive" into specific agent outputs, effectively acting as the project lead for your own education.