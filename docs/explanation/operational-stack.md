# The Operational Stack (The "Staff")

In a professional AI architecture, the **Operational Stack** sits on top of your **RAG Data Stack**. These components transform a simple retrieval script into a production-ready, autonomous, and secure system.

## 1. Agentic Orchestration
**Scope:** The logical brain and hands of the system.
**Role:** Acts as the "Project Manager" that breaks down complex user goals into executable steps.

*   **Planner:** Analyzes the request and creates a sequence of sub-tasks.
*   **ReAct Logic (Reason + Act):** A loop where the AI "thinks," acts (calls a tool), observes the result, and iterates.
*   **Tool/Function Library:** Authorized scripts or APIs (e.g., `tellurion-manager` functions) the agent can call.
*   **Short-term Memory:** A "scratchpad" for the current task's state.
*   **Output:** An executed action and a final report.

## 2. AI Guardrails
**Scope:** The security and compliance layer.
**Role:** Ensures inputs are safe and outputs are accurate, formatted, and secure.

*   **Input Scanner:** Filters prompt injections and PII before reaching the LLM.
*   **Output Validator:** Enforces schema compliance (e.g., valid JSON or Pydantic classes).
*   **Hallucination Check:** Cross-references LLM output against RAG context to ensure factual grounding.
*   **Topic Rail:** Restricts conversation to authorized domains (e.g., "Tellurion Project Only").
*   **Output:** Sanitized strings or "Blocked" notifications.

## 3. Observability & Evaluation
**Scope:** The telemetry and quality control center.
**Role:** Provides a "paper trail" for decisions and a mathematical score for performance.

*   **Tracer:** Logs the full request path from input to vector search to LLM call.
*   **Token Tracker:** Records real-time costs for API budgeting.
*   **LLM-as-a-Judge (Evals):** A high-reasoning model that grades responses for "Faithfulness" and accuracy.
*   **Latency Monitor:** Identifies bottlenecks in the pipeline "hops."
*   **Output:** Dashboards, cost reports, and accuracy scores.

## 4. Semantic Caching
**Scope:** The performance and cost-optimization layer.
**Role:** Avoids redundant LLM calls by recognizing "meaningfully similar" previous queries.

*   **Cache Database:** High-speed storage (Redis or local KV store) for Q&A pairs.
*   **Vector Similarity Check:** Uses an embedding model to match the *meaning* of a new query to a cached one.
*   **Threshold Manager:** Sets the strictness of matches (e.g., 98% similarity required).
*   **TTL (Time-to-Live):** Ensures the cache expires to prevent outdated information delivery.
*   **Output:** Near-instantaneous responses served from local memory.

---

## Summary Table
| Component | Role | Primary Output |
| :--- | :--- | :--- |
| **Orchestration** | Logical Execution | Completed Task / Plan |
| **Guardrails** | Security & Format | Validated / Safe Text |
| **Observability** | Tracking & Quality | Traces & Accuracy Scores |
| **Semantic Caching** | Speed & Savings | Pre-computed Response |
