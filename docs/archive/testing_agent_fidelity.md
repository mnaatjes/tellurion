# Testing Agent Fidelity

Fidelity refers to how accurately a subagent represents a persona or adheres to its operational rules. This document outlines manual and automated methods for testing fidelity in Gemini CLI.

## 1. Manual Persona Verification

Manual testing is the first step in ensuring your agent is operating within its defined persona (e.g., an author's voice and philosophy).

### The `/memory show` Command
Use this command to inspect the "concatenated memory" of the agent. This allows you to verify:
*   **System Prompt:** Is the custom persona being loaded?
*   **Imported Works:** Are the author's specific texts and chapters actually in the context?
*   **Hierarchical Priority:** Are the project-specific rules in `GEMINI.md` correctly overriding or supplementing the global persona?

### UI Indicators
When a custom system prompt or a specialized subagent is active, the Gemini CLI displays a **`|⌐■_■|`** (sunglasses) icon. If this icon is missing, the agent is using its default behavior instead of your custom persona.

### Adversarial Prompting (Red Teaming)
Test the limits of the persona by:
*   Asking questions that are out of character or contradict the author's views.
*   Prompting the agent to ignore its system instructions.
*   A high-fidelity agent should resist these attempts or respond to them through the lens of its specific philosophy.

---

## 2. Automated Fidelity Testing (Model Goldens)

Gemini CLI supports **Model Goldens**, which are baselines of "correct" responses used for regression testing.

### How it Works
1.  **Baseline Generation:** Provide a set of 10–20 standard prompts and record the agent's responses once you are satisfied with its performance.
2.  **Regression Testing:** Run the test suite after any changes to the agent's source material or system prompt.
3.  **Failure Analysis:** If the new responses deviate significantly from the "Golden" baseline, the test fails, signaling a loss of fidelity.
4.  **Command:** `REGENERATE_MODEL_GOLDENS="true" npm run test:e2e` (Typically used by developers to maintain CLI standards).

---

## 3. Operational Fidelity (The Validation Loop)

High-fidelity agents do not just generate text; they perform actions and verify their own work.

*   **Research-First:** The agent should use `grep_search` or `read_file` to find evidence in its source material before answering a question.
*   **Surgical Updates:** When editing files, the agent should only change the relevant lines, adhering strictly to the project's existing style and conventions.
*   **Verification:** The interaction is not complete until the agent runs a validation step (e.g., checking a build status or confirming a fact against another source).

## 4. Qualitative Metrics

For persona-based agents, create a **"Golden Dataset"** of 10–20 complex questions with "Ideal Answers" derived directly from the source texts.

| Metric | Testing Method |
| :--- | :--- |
| **Consistency** | Ask the same question three times; the reasoning should remain identical. |
| **Tone Check** | Compare the agent's vocabulary and sentence structure against the author's original works. |
| **Evidence-Based** | Every claim made by the agent should be traceable to a specific source in its provided bibliography. |
